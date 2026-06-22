import os
import re
import json
import hashlib
import hmac
import base64
import uuid
import random
import threading
from pathlib import Path
from datetime import datetime, timezone

from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse

load_dotenv()

app = FastAPI(title="Swarm Resolution Assistant")

TEAMS_HMAC_SECRET = os.getenv("TEAMS_HMAC_SECRET", "")
KB_PATH = Path(__file__).parent / "knowledge.json"
knowledge_base = json.loads(KB_PATH.read_text(encoding="utf-8"))

# ── Session store (in-memory) ────────────────────────────────────────────────

_sessions: dict = {}
_lock = threading.Lock()

_ADJ  = ["Swift", "Sharp", "Calm", "Clear", "Bold", "Keen", "Agile", "Cool"]
_NOUN = ["Falcon", "Tiger", "Eagle", "Hawk", "Wolf", "Lynx", "Raven", "Bear"]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _gen_uid() -> str:
    return f"{random.choice(_ADJ)}-{random.choice(_NOUN)}-{random.randint(100, 999)}"


def _sentiment(rating, comment: str = "") -> str:
    if not rating:
        return "unknown"
    neg = {"bad","poor","terrible","awful","slow","wrong","broken","useless","disappointed","frustrated","horrible"}
    pos = {"great","good","excellent","helpful","amazing","perfect","quick","love","awesome","fantastic","brilliant","clear"}
    words = set(re.findall(r"\b\w+\b", comment.lower()))
    n_hits = len(words & neg)
    p_hits = len(words & pos)
    if rating >= 4 and n_hits == 0:
        return "positive"
    if rating <= 2:
        return "negative"
    if p_hits > n_hits:
        return "positive"
    if n_hits > p_hits:
        return "negative"
    return "neutral"


def _create_session(source: str = "browser") -> dict:
    sid = uuid.uuid4().hex[:8]
    sess = {
        "id":         sid,
        "user_id":    _gen_uid(),
        "started_at": _now(),
        "ended_at":   None,
        "status":     "active",
        "messages":   [],
        "feedback":   {"rating": None, "comment": "", "sentiment": None},
        "source":     source,
    }
    with _lock:
        _sessions[sid] = sess
    return sess


def _get_session(sid: str):
    with _lock:
        return _sessions.get(sid)


def _all_sessions() -> list:
    with _lock:
        return sorted(_sessions.values(), key=lambda s: s["started_at"], reverse=True)


# ── Knowledge base ───────────────────────────────────────────────────────────

def search_knowledge(query: str) -> list:
    qwords = set(re.findall(r"\b\w+\b", query.lower()))
    results = []
    for entry in knowledge_base:
        score = len(set(entry["topic"].lower().split()) & qwords)
        if score > 0:
            results.append((score, entry))
    results.sort(key=lambda x: x[0], reverse=True)
    return [e for _, e in results]


def mock_llm(user_text: str) -> str:
    matches = search_knowledge(user_text)
    if not matches:
        return (
            "No matching swarm pattern found in the historical resolution database.\n\n"
            "Try describing the symptom more specifically — for example: "
            "*login failures*, *call drops*, *recording unavailable*, *API 500 errors*, "
            "*queue overflow*, *IVR routing*, *certificate expiry*, "
            "*pending upload*, *PCI masking*, or *screen recording blank*."
        )
    parts = []
    for m in matches[:2]:
        label = " ".join(m["topic"].split()[:4]).title()
        parts.append(f"**Swarm Pattern Match: {label}**\n\n{m['content']}")
    return "\n\n---\n\n".join(parts)


# ── Teams webhook (also logs to session store) ───────────────────────────────

def _verify_hmac(body: bytes, auth_header: str) -> bool:
    if not TEAMS_HMAC_SECRET:
        return True
    try:
        key = base64.b64decode(TEAMS_HMAC_SECRET)
        mac = hmac.new(key, body, hashlib.sha256)
        expected = f"HMAC {base64.b64encode(mac.digest()).decode()}"
        return hmac.compare_digest(expected, auth_header)
    except Exception:
        return False


@app.post("/webhook")
async def teams_webhook(request: Request):
    body = await request.body()
    if not _verify_hmac(body, request.headers.get("authorization", "")):
        raise HTTPException(status_code=401, detail="Invalid HMAC signature")
    payload = json.loads(body)
    raw_text = payload.get("text", "")
    user_text = re.sub(r"<[^>]+>", "", raw_text).strip()
    teams_user = payload.get("from", {}).get("name", "Teams User")
    conv_id = payload.get("conversation", {}).get("id", uuid.uuid4().hex[:8])

    with _lock:
        if conv_id not in _sessions:
            _sessions[conv_id] = {
                "id": conv_id[:8], "user_id": teams_user,
                "started_at": _now(), "ended_at": None, "status": "active",
                "messages": [], "feedback": {"rating": None, "comment": "", "sentiment": None},
                "source": "teams",
            }
        sess = _sessions[conv_id]

    if not user_text:
        reply = "Describe the swarm symptom and I'll surface root causes, investigation steps, and historical playbooks."
    else:
        reply = mock_llm(user_text)
        with _lock:
            sess["messages"].extend([
                {"role": "user", "text": user_text, "ts": _now()},
                {"role": "bot",  "text": reply,     "ts": _now()},
            ])
    return JSONResponse({"type": "message", "text": reply})


# ── Session API ───────────────────────────────────────────────────────────────

@app.post("/api/session/new")
async def api_session_new():
    sess = _create_session(source="browser")
    return JSONResponse({"session_id": sess["id"], "user_id": sess["user_id"]})


@app.get("/api/session/{sid}/messages")
async def api_session_messages(sid: str):
    sess = _get_session(sid)
    if not sess:
        raise HTTPException(status_code=404, detail="Session not found")
    return JSONResponse({
        "status":   sess["status"],
        "user_id":  sess["user_id"],
        "messages": sess["messages"],
    })


@app.post("/api/session/{sid}/chat")
async def api_session_chat(sid: str, request: Request):
    sess = _get_session(sid)
    if not sess:
        raise HTTPException(status_code=404, detail="Session not found")
    if sess["status"] != "active":
        return JSONResponse({"reply": "This thread has ended. Please start a new thread."})
    payload = await request.json()
    user_text = payload.get("message", "").strip()
    if not user_text:
        return JSONResponse({"reply": "Please describe the swarm symptom."})
    reply = mock_llm(user_text)
    with _lock:
        sess["messages"].extend([
            {"role": "user", "text": user_text, "ts": _now()},
            {"role": "bot",  "text": reply,     "ts": _now()},
        ])
    return JSONResponse({"reply": reply})


@app.post("/api/session/{sid}/end")
async def api_session_end(sid: str):
    sess = _get_session(sid)
    if not sess:
        raise HTTPException(status_code=404, detail="Session not found")
    with _lock:
        sess["status"]   = "awaiting_feedback"
        sess["ended_at"] = _now()
    return JSONResponse({"ok": True})


@app.post("/api/session/{sid}/feedback")
async def api_session_feedback(sid: str, request: Request):
    sess = _get_session(sid)
    if not sess:
        raise HTTPException(status_code=404, detail="Session not found")
    payload = await request.json()
    rating  = payload.get("rating")
    rating  = int(rating) if rating else None
    comment = payload.get("comment", "").strip()
    sent    = _sentiment(rating, comment)
    with _lock:
        sess["feedback"] = {"rating": rating, "comment": comment, "sentiment": sent}
        sess["status"]   = "ended"
    return JSONResponse({"ok": True, "sentiment": sent})


@app.get("/api/threads")
async def api_threads():
    sessions = _all_sessions()
    threads  = []
    for s in sessions:
        dur = None
        if s["ended_at"] and s["started_at"]:
            try:
                d = int((datetime.fromisoformat(s["ended_at"]) -
                         datetime.fromisoformat(s["started_at"])).total_seconds())
                dur = f"{d // 60}m {d % 60}s"
            except Exception:
                pass
        msgs = s["messages"]
        threads.append({
            "id":         s["id"],
            "user_id":    s["user_id"],
            "source":     s["source"],
            "started_at": s["started_at"].replace("T", " ").replace("+00:00", " UTC"),
            "ended_at":   (s["ended_at"] or "").replace("T", " ").replace("+00:00", " UTC"),
            "duration":   dur,
            "status":     s["status"],
            "msg_count":  sum(1 for m in msgs if m["role"] == "user"),
            "feedback":   s["feedback"],
            "preview":    msgs[-1]["text"][:90] + ("…" if len(msgs[-1]["text"]) > 90 else "") if msgs else "",
        })
    ended   = [s for s in sessions if s["status"] == "ended" and s["feedback"]["rating"]]
    ratings = [s["feedback"]["rating"] for s in ended]
    sents   = [s["feedback"]["sentiment"] for s in ended]
    stats   = {
        "total":        len(sessions),
        "active":       sum(1 for s in sessions if s["status"] == "active"),
        "ended":        sum(1 for s in sessions if s["status"] == "ended"),
        "avg_rating":   round(sum(ratings) / len(ratings), 1) if ratings else None,
        "positive":     sents.count("positive"),
        "neutral":      sents.count("neutral"),
        "negative":     sents.count("negative"),
        "with_feedback": len(ended),
    }
    return JSONResponse({"threads": threads, "stats": stats})


@app.get("/health")
async def health():
    return {"status": "ok", "kb_entries": len(knowledge_base), "sessions": len(_sessions)}


@app.get("/teams", response_class=HTMLResponse)
async def teams_page():
    html_path = Path(__file__).parent / "teams-dashboard.html"
    return HTMLResponse(html_path.read_text(encoding="utf-8"))


# ── Chat UI ───────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index():
    return r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Swarm Resolution Assistant</title>
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:'Segoe UI',sans-serif;background:#f3f2f1;height:100vh;display:flex;flex-direction:column}
  .hidden{display:none!important}

  /* ── LANDING ── */
  #v-landing{flex:1;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#0f3460 0%,#16213e 100%)}
  .land-card{background:white;border-radius:20px;padding:48px 56px;text-align:center;max-width:480px;box-shadow:0 20px 60px rgba(0,0,0,0.3)}
  .land-logo{font-size:48px;margin-bottom:16px}
  .land-card h1{font-size:22px;font-weight:700;color:#0f3460;margin-bottom:8px}
  .land-card p{font-size:13px;color:#666;margin-bottom:6px}
  .land-badge{display:inline-block;background:#e94560;color:white;font-size:11px;font-weight:700;padding:3px 10px;border-radius:10px;margin-bottom:28px;letter-spacing:.5px}
  .btn-start{width:100%;background:#e94560;color:white;border:none;border-radius:10px;padding:14px;font-size:16px;font-weight:700;cursor:pointer;letter-spacing:.3px;transition:background .2s}
  .btn-start:hover{background:#c73652}
  .dash-link{display:block;margin-top:16px;font-size:13px;color:#6264a7;text-decoration:none}
  .dash-link:hover{text-decoration:underline}

  /* ── CHAT ── */
  #v-chat{flex:1;display:flex;flex-direction:column}
  header{background:#0f3460;color:white;padding:12px 20px;display:flex;align-items:center;gap:12px;box-shadow:0 2px 6px rgba(0,0,0,.25)}
  .h-logo{width:38px;height:38px;background:#e94560;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
  .h-info h1{font-size:15px;font-weight:700}
  .h-info p{font-size:11px;opacity:.75;margin-top:1px}
  .h-right{margin-left:auto;display:flex;align-items:center;gap:10px}
  .h-badge{background:#e94560;color:white;font-size:10px;font-weight:700;padding:3px 8px;border-radius:10px;letter-spacing:.5px}
  .btn-end{background:transparent;border:1.5px solid rgba(255,255,255,.5);color:white;padding:6px 14px;border-radius:8px;font-size:12px;font-weight:700;cursor:pointer;transition:all .2s}
  .btn-end:hover{background:rgba(255,255,255,.15);border-color:white}
  #msgs{flex:1;overflow-y:auto;padding:20px;display:flex;flex-direction:column;gap:12px}
  .bubble{max-width:78%;padding:12px 16px;border-radius:14px;font-size:14px;line-height:1.6}
  .user{background:#0f3460;color:white;align-self:flex-end;border-bottom-right-radius:4px}
  .bot{background:white;color:#242424;align-self:flex-start;border-bottom-left-radius:4px;box-shadow:0 1px 4px rgba(0,0,0,.1);white-space:pre-wrap}
  .bot strong{color:#0f3460;font-weight:700}
  .bot em{font-style:italic;color:#555}
  .bot hr{border:none;border-top:1px solid #e0deda;margin:8px 0}
  .typing{background:white;align-self:flex-start;padding:12px 16px;border-radius:14px;box-shadow:0 1px 4px rgba(0,0,0,.1)}
  .typing span{display:inline-block;width:7px;height:7px;background:#999;border-radius:50%;animation:blink 1.2s infinite;margin:0 2px}
  .typing span:nth-child(2){animation-delay:.2s}
  .typing span:nth-child(3){animation-delay:.4s}
  @keyframes blink{0%,80%,100%{opacity:.2}40%{opacity:1}}
  .chips-label{padding:4px 20px 2px;font-size:11px;font-weight:600;color:#999;letter-spacing:.5px;text-transform:uppercase}
  .chips{display:flex;flex-wrap:wrap;gap:7px;padding:0 20px 8px}
  .chip{background:white;border:1px solid #d0cece;border-radius:16px;padding:5px 13px;font-size:12px;color:#0f3460;cursor:pointer;transition:all .15s;font-weight:500}
  .chip:hover{background:#e8f0fe;border-color:#0f3460}
  .chat-form{display:flex;gap:8px;padding:12px 20px;background:white;border-top:1px solid #e1dfdd}
  .chat-form input{flex:1;border:1px solid #c8c6c4;border-radius:8px;padding:10px 14px;font-size:14px;outline:none}
  .chat-form input:focus{border-color:#0f3460;box-shadow:0 0 0 2px rgba(15,52,96,.12)}
  .chat-form button{background:#e94560;color:white;border:none;border-radius:8px;padding:10px 22px;font-size:14px;cursor:pointer;font-weight:700}
  .chat-form button:hover{background:#c73652}

  /* ── FEEDBACK ── */
  #v-feedback{flex:1;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#0f3460 0%,#16213e 100%)}
  .fb-card{background:white;border-radius:20px;padding:44px 52px;text-align:center;max-width:440px;width:100%;box-shadow:0 20px 60px rgba(0,0,0,.3)}
  .fb-card h2{font-size:20px;font-weight:700;color:#0f3460;margin-bottom:8px}
  .fb-card p{font-size:13px;color:#777;margin-bottom:24px}
  .stars{display:flex;justify-content:center;gap:10px;margin-bottom:20px}
  .star{font-size:36px;color:#ddd;cursor:pointer;transition:color .15s;user-select:none}
  .star.lit{color:#f5c518}
  .star:hover{transform:scale(1.15)}
  .fb-card textarea{width:100%;height:90px;border:1px solid #ddd;border-radius:8px;padding:10px 14px;font-size:13px;font-family:inherit;resize:none;outline:none;margin-bottom:20px}
  .fb-card textarea:focus{border-color:#0f3460}
  .btn-fb{width:100%;background:#e94560;color:white;border:none;border-radius:10px;padding:13px;font-size:15px;font-weight:700;cursor:pointer;margin-bottom:10px}
  .btn-fb:hover{background:#c73652}
  .btn-skip{background:transparent;border:none;color:#999;font-size:13px;cursor:pointer;text-decoration:underline}
  .rating-label{font-size:13px;font-weight:600;color:#0f3460;height:20px;margin-bottom:10px}

  /* ── COMPLETE ── */
  #v-complete{flex:1;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#0f3460 0%,#16213e 100%)}
  .done-card{background:white;border-radius:20px;padding:48px 56px;text-align:center;max-width:420px;box-shadow:0 20px 60px rgba(0,0,0,.3)}
  .done-icon{font-size:52px;margin-bottom:16px}
  .done-card h2{font-size:20px;font-weight:700;color:#0f3460;margin-bottom:8px}
  .done-card p{font-size:13px;color:#666;margin-bottom:28px}
  .done-sentiment{display:inline-block;padding:6px 18px;border-radius:20px;font-size:13px;font-weight:700;margin-bottom:24px}
  .sent-positive{background:#e6f4ea;color:#1e7e34}
  .sent-neutral{background:#fff3cd;color:#856404}
  .sent-negative{background:#fde8e8;color:#c0392b}
  .sent-unknown{background:#f0f0f0;color:#666}
</style>
</head>
<body>

<!-- ─── LANDING ─────────────────────────────────────────────────────────── -->
<div id="v-landing" class="hidden">
  <div class="land-card">
    <div class="land-logo">⚡</div>
    <h1>Swarm Resolution Assistant</h1>
    <p>Customer Swarms &amp; Supportability</p>
    <div class="land-badge">84 PATTERNS</div>
    <button class="btn-start" onclick="startThread()">Start New Thread</button>
    <a class="dash-link" href="/dashboard">View Dashboard →</a>
  </div>
</div>

<!-- ─── CHAT ─────────────────────────────────────────────────────────────── -->
<div id="v-chat" class="hidden">
  <header>
    <div class="h-logo">⚡</div>
    <div class="h-info">
      <h1>Swarm Resolution Assistant</h1>
      <p id="session-label">Initialising…</p>
    </div>
    <div class="h-right">
      <span class="h-badge">84 PATTERNS</span>
      <button class="btn-end" onclick="confirmEnd()">End Thread</button>
    </div>
  </header>

  <div id="msgs"></div>

  <div class="chips-label">Quick examples</div>
  <div class="chips">
    <div class="chip" onclick="send('Agents cannot log in — authentication failure')">🔐 Login failure</div>
    <div class="chip" onclick="send('Calls are dropping and call quality is degraded')">📞 Call drops</div>
    <div class="chip" onclick="send('API returning 500 internal server errors')">💥 API 500 errors</div>
    <div class="chip" onclick="send('Playback unavailable error 8203 9002 CXone')">⚠️ Playback error</div>
    <div class="chip" onclick="send('Recording corrupt packets stops early ffmpeg')">🔊 Corrupt audio</div>
    <div class="chip" onclick="send('Recordings stuck pending upload File Storage')">⏫ Upload stuck</div>
    <div class="chip" onclick="send('PCI pause resume not masking sensitive audio')">🔐 PCI masking</div>
    <div class="chip" onclick="send('Supervisors cannot play recordings permission scope')">🚫 Permission denied</div>
    <div class="chip" onclick="send('IVR and routing failure — calls not routing to agents')">🔀 Routing failure</div>
    <div class="chip" onclick="send('Real-time reporting dashboard lag and delay')">📊 Reporting lag</div>
  </div>

  <form class="chat-form" onsubmit="handleSubmit(event)">
    <input id="inp" type="text" placeholder="Describe the swarm symptom…" autocomplete="off">
    <button type="submit">Analyse</button>
  </form>
</div>

<!-- ─── FEEDBACK ─────────────────────────────────────────────────────────── -->
<div id="v-feedback" class="hidden">
  <div class="fb-card">
    <div style="font-size:40px;margin-bottom:12px">💬</div>
    <h2>Rate this session</h2>
    <p>How useful was the Swarm Resolution Assistant?</p>
    <div class="stars" id="star-row">
      <span class="star" data-v="1" onclick="setRating(1)">★</span>
      <span class="star" data-v="2" onclick="setRating(2)">★</span>
      <span class="star" data-v="3" onclick="setRating(3)">★</span>
      <span class="star" data-v="4" onclick="setRating(4)">★</span>
      <span class="star" data-v="5" onclick="setRating(5)">★</span>
    </div>
    <div class="rating-label" id="rating-label">&nbsp;</div>
    <textarea id="fb-text" placeholder="Optional: any comments about this session…"></textarea>
    <button class="btn-fb" onclick="submitFeedback()">Submit Feedback &amp; Close Thread</button>
    <button class="btn-skip" onclick="skipFeedback()">Skip feedback</button>
  </div>
</div>

<!-- ─── COMPLETE ─────────────────────────────────────────────────────────── -->
<div id="v-complete" class="hidden">
  <div class="done-card">
    <div class="done-icon" id="done-icon">✅</div>
    <h2>Thread Closed</h2>
    <p id="done-msg">Thank you for your feedback!</p>
    <div id="done-sentiment" class="done-sentiment sent-unknown hidden"></div>
    <br>
    <button class="btn-start" style="margin-top:8px" onclick="startThread()">Start New Thread</button>
    <a class="dash-link" href="/dashboard">View Dashboard →</a>
  </div>
</div>

<script>
let sid = null;
let selectedRating = 0;
const LABELS = ['','Not helpful','Somewhat helpful','Neutral','Helpful','Very helpful'];

function view(name) {
  ['landing','chat','feedback','complete'].forEach(n =>
    document.getElementById('v-'+n).classList.add('hidden')
  );
  document.getElementById('v-'+name).classList.remove('hidden');
}

async function init() {
  const stored = localStorage.getItem('sra_sid');
  if (!stored) { view('landing'); return; }
  try {
    const r = await fetch('/api/session/'+stored+'/messages');
    if (!r.ok) throw new Error();
    const d = await r.json();
    sid = stored;
    if (d.status === 'ended') {
      view('complete');
    } else if (d.status === 'awaiting_feedback') {
      view('feedback');
    } else {
      document.getElementById('session-label').textContent =
        'Thread: '+sid+' · '+d.user_id;
      d.messages.forEach(m => addBubble(m.text, m.role === 'user' ? 'user' : 'bot', false));
      view('chat');
    }
  } catch(e) {
    localStorage.removeItem('sra_sid');
    view('landing');
  }
}

async function startThread() {
  try {
    const r = await fetch('/api/session/new', {method:'POST'});
    const d = await r.json();
    sid = d.session_id;
    localStorage.setItem('sra_sid', sid);
    document.getElementById('session-label').textContent =
      'Thread: '+sid+' · '+d.user_id;
    document.getElementById('msgs').innerHTML = '';
    selectedRating = 0;
    addBubble(
      "Hi! I'm your Swarm Resolution Assistant.\n\n" +
      "Describe the active swarm symptom and I'll return **ranked root cause hypotheses**, " +
      "**investigation steps**, and a **historical resolution playbook** from 84 real swarm patterns.\n\n" +
      "Click a chip below or type your own description.",
      'bot', false
    );
    view('chat');
  } catch(e) {
    alert('Could not start a session. Is the server running?');
  }
}

async function send(message) {
  if (!message.trim() || !sid) return;
  document.getElementById('inp').value = '';
  addBubble(message, 'user');
  const t = addTyping();
  try {
    const r = await fetch('/api/session/'+sid+'/chat', {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({message})
    });
    const d = await r.json();
    t.remove();
    addBubble(d.reply, 'bot');
  } catch(e) {
    t.remove();
    addBubble('Error reaching server.', 'bot');
  }
}

function handleSubmit(e) {
  e.preventDefault();
  send(document.getElementById('inp').value);
}

function confirmEnd() {
  if (confirm('End this thread? You\'ll be asked for a quick rating before it closes.')) {
    endThread();
  }
}

async function endThread() {
  if (!sid) return;
  await fetch('/api/session/'+sid+'/end', {method:'POST'});
  selectedRating = 0;
  setRating(0);
  document.getElementById('fb-text').value = '';
  view('feedback');
}

function setRating(v) {
  selectedRating = v;
  document.querySelectorAll('.star').forEach((s, i) => {
    s.classList.toggle('lit', i < v);
  });
  document.getElementById('rating-label').textContent = v ? LABELS[v] : ' ';
}

async function submitFeedback() {
  if (!selectedRating) {
    alert('Please select a star rating (1–5).');
    return;
  }
  const comment = document.getElementById('fb-text').value;
  const r = await fetch('/api/session/'+sid+'/feedback', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({rating: selectedRating, comment})
  });
  const d = await r.json();
  localStorage.removeItem('sra_sid');
  sid = null;
  showComplete(selectedRating, d.sentiment, comment);
}

async function skipFeedback() {
  await fetch('/api/session/'+sid+'/feedback', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({rating: null, comment: ''})
  });
  localStorage.removeItem('sra_sid');
  sid = null;
  showComplete(null, null, '');
}

function showComplete(rating, sentiment, comment) {
  const iconEl = document.getElementById('done-icon');
  const msgEl  = document.getElementById('done-msg');
  const sentEl = document.getElementById('done-sentiment');
  if (rating) {
    iconEl.textContent = rating >= 4 ? '✅' : rating === 3 ? '🙂' : '💡';
    msgEl.textContent  = rating >= 4
      ? 'Thank you — glad it was helpful!'
      : rating === 3 ? 'Thank you for the feedback.'
      : 'Thank you. We\'ll use your feedback to improve.';
    if (sentiment && sentiment !== 'unknown') {
      sentEl.className = 'done-sentiment sent-' + sentiment;
      sentEl.textContent =
        sentiment === 'positive' ? '😊 Positive sentiment detected'
        : sentiment === 'neutral'  ? '😐 Neutral sentiment detected'
        : '😕 Negative sentiment detected';
      sentEl.classList.remove('hidden');
    }
  } else {
    iconEl.textContent = '🏁';
    msgEl.textContent  = 'Thread closed.';
  }
  view('complete');
}

function addBubble(text, cls, scroll=true) {
  const c = document.getElementById('msgs');
  const d = document.createElement('div');
  d.className = 'bubble ' + cls;
  d.innerHTML = cls === 'bot' ? renderMd(text) : esc(text);
  c.appendChild(d);
  if (scroll) c.scrollTop = c.scrollHeight;
  return d;
}

function addTyping() {
  const c = document.getElementById('msgs');
  const d = document.createElement('div');
  d.className = 'typing';
  d.innerHTML = '<span></span><span></span><span></span>';
  c.appendChild(d);
  c.scrollTop = c.scrollHeight;
  return d;
}

function renderMd(t) {
  return t
    .replace(/---/g, '<hr>')
    .replace(/[*][*](.+?)[*][*]/g, '<strong>$1</strong>')
    .replace(/[*](.+?)[*]/g, '<em>$1</em>');
}

function esc(t) {
  return t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

init();
</script>
</body>
</html>"""


# ── Dashboard ─────────────────────────────────────────────────────────────────

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    return r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dashboard — Swarm Resolution Assistant</title>
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:'Segoe UI',sans-serif;background:#0d1117;color:#e6edf3;min-height:100vh}
  header{background:#161b22;border-bottom:1px solid #30363d;padding:14px 28px;display:flex;align-items:center;gap:14px}
  .h-logo{width:36px;height:36px;background:#e94560;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px}
  header h1{font-size:16px;font-weight:700;color:#e6edf3}
  header p{font-size:12px;color:#8b949e}
  .h-right{margin-left:auto;display:flex;align-items:center;gap:14px}
  .refresh-info{font-size:11px;color:#6e7681}
  .btn-chat{background:#e94560;color:white;border:none;border-radius:7px;padding:7px 16px;font-size:12px;font-weight:700;cursor:pointer;text-decoration:none}

  main{padding:24px 28px;max-width:1400px;margin:0 auto}

  /* ── stat cards ── */
  .cards{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:24px}
  .card{background:#161b22;border:1px solid #30363d;border-radius:12px;padding:20px 24px}
  .card-label{font-size:11px;font-weight:600;color:#8b949e;text-transform:uppercase;letter-spacing:.6px;margin-bottom:8px}
  .card-value{font-size:32px;font-weight:700;color:#e6edf3}
  .card-sub{font-size:12px;color:#6e7681;margin-top:4px}
  .card.c-active .card-value{color:#3fb950}
  .card.c-pos    .card-value{color:#3fb950}
  .card.c-neg    .card-value{color:#f85149}
  .card.c-rating .card-value{color:#d29922}

  /* ── sentiment bar ── */
  .sent-section{background:#161b22;border:1px solid #30363d;border-radius:12px;padding:20px 24px;margin-bottom:24px}
  .sent-title{font-size:13px;font-weight:600;color:#8b949e;margin-bottom:14px;text-transform:uppercase;letter-spacing:.5px}
  .sent-bar-wrap{display:flex;height:12px;border-radius:6px;overflow:hidden;background:#21262d;margin-bottom:10px}
  .sb-pos{background:#3fb950;height:100%;transition:width .4s}
  .sb-neu{background:#d29922;height:100%;transition:width .4s}
  .sb-neg{background:#f85149;height:100%;transition:width .4s}
  .sent-legend{display:flex;gap:20px}
  .leg{display:flex;align-items:center;gap:6px;font-size:12px;color:#8b949e}
  .dot{width:10px;height:10px;border-radius:50%}
  .dot.pos{background:#3fb950}
  .dot.neu{background:#d29922}
  .dot.neg{background:#f85149}

  /* ── table ── */
  .table-wrap{background:#161b22;border:1px solid #30363d;border-radius:12px;overflow:hidden}
  .table-header{padding:14px 20px;border-bottom:1px solid #30363d;display:flex;align-items:center;justify-content:space-between}
  .table-title{font-size:14px;font-weight:600;color:#e6edf3}
  .table-count{font-size:12px;color:#8b949e}
  table{width:100%;border-collapse:collapse}
  th{padding:10px 14px;font-size:11px;font-weight:600;color:#8b949e;text-transform:uppercase;letter-spacing:.5px;text-align:left;border-bottom:1px solid #21262d;background:#161b22}
  td{padding:11px 14px;font-size:13px;color:#c9d1d9;border-bottom:1px solid #21262d;vertical-align:top}
  tr:last-child td{border-bottom:none}
  tr:hover td{background:#1c2128}

  .badge{display:inline-block;padding:2px 9px;border-radius:10px;font-size:11px;font-weight:600;letter-spacing:.3px}
  .b-active   {background:rgba(63,185,80,.15); color:#3fb950}
  .b-ended    {background:rgba(139,148,158,.12);color:#8b949e}
  .b-awaiting {background:rgba(210,153,34,.15); color:#d29922}
  .b-positive {background:rgba(63,185,80,.15); color:#3fb950}
  .b-neutral  {background:rgba(210,153,34,.15); color:#d29922}
  .b-negative {background:rgba(248,81,73,.15);  color:#f85149}
  .b-unknown  {background:rgba(139,148,158,.12);color:#8b949e}
  .b-browser  {background:rgba(88,166,255,.12); color:#58a6ff}
  .b-teams    {background:rgba(88,96,255,.15);  color:#8b96ff}

  .stars-cell{color:#d29922;letter-spacing:1px;font-size:13px}
  .preview{color:#6e7681;font-style:italic;font-size:12px;max-width:220px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .uid{font-family:'Courier New',monospace;font-size:12px}
  .ts{font-size:11px;color:#6e7681}
  .no-data{text-align:center;padding:40px;color:#6e7681;font-size:14px}

  .pulse{display:inline-block;width:7px;height:7px;background:#3fb950;border-radius:50%;animation:pulse 1.5s infinite;margin-right:4px}
  @keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
</style>
</head>
<body>

<header>
  <div class="h-logo">⚡</div>
  <div>
    <h1>Swarm Resolution Assistant — Dashboard</h1>
    <p>All conversation threads · Live sentiment analysis</p>
  </div>
  <div class="h-right">
    <span class="refresh-info"><span class="pulse"></span>Auto-refresh every 5s · Last: <span id="last-ts">–</span></span>
    <a class="btn-chat" style="background:#6264a7;margin-right:4px" href="/teams">Teams Analytics →</a>
    <a class="btn-chat" href="/">Open Bot →</a>
  </div>
</header>

<main>

  <!-- stat cards -->
  <div class="cards">
    <div class="card">
      <div class="card-label">Total Threads</div>
      <div class="card-value" id="c-total">–</div>
      <div class="card-sub" id="c-sub-total">No activity yet</div>
    </div>
    <div class="card c-active">
      <div class="card-label">Active Now</div>
      <div class="card-value" id="c-active">–</div>
      <div class="card-sub" id="c-sub-active">Live sessions</div>
    </div>
    <div class="card c-rating">
      <div class="card-label">Avg Rating</div>
      <div class="card-value" id="c-rating">–</div>
      <div class="card-sub" id="c-sub-rating">From feedback</div>
    </div>
    <div class="card c-pos">
      <div class="card-label">Positive Sentiment</div>
      <div class="card-value" id="c-pos">–</div>
      <div class="card-sub" id="c-sub-pos">Of rated threads</div>
    </div>
  </div>

  <!-- sentiment bar -->
  <div class="sent-section">
    <div class="sent-title">Sentiment Distribution — Rated Threads</div>
    <div class="sent-bar-wrap">
      <div class="sb-pos" id="sb-pos" style="width:0%"></div>
      <div class="sb-neu" id="sb-neu" style="width:0%"></div>
      <div class="sb-neg" id="sb-neg" style="width:0%"></div>
    </div>
    <div class="sent-legend">
      <div class="leg"><div class="dot pos"></div><span id="leg-pos">Positive: 0</span></div>
      <div class="leg"><div class="dot neu"></div><span id="leg-neu">Neutral: 0</span></div>
      <div class="leg"><div class="dot neg"></div><span id="leg-neg">Negative: 0</span></div>
      <div class="leg" style="margin-left:auto;color:#6e7681" id="leg-total">0 threads rated</div>
    </div>
  </div>

  <!-- thread table -->
  <div class="table-wrap">
    <div class="table-header">
      <span class="table-title">All Conversation Threads</span>
      <span class="table-count" id="tbl-count">–</span>
    </div>
    <table>
      <thead>
        <tr>
          <th>User</th>
          <th>Source</th>
          <th>Started (UTC)</th>
          <th>Duration</th>
          <th>Queries</th>
          <th>Status</th>
          <th>Rating</th>
          <th>Sentiment</th>
          <th>Last Message Preview</th>
        </tr>
      </thead>
      <tbody id="tbl-body">
        <tr><td colspan="9" class="no-data">No threads yet. Open the bot to start a session.</td></tr>
      </tbody>
    </table>
  </div>

</main>

<script>
async function load() {
  try {
    const r = await fetch('/api/threads');
    const d = await r.json();
    const s = d.stats;

    // Cards
    document.getElementById('c-total').textContent  = s.total;
    document.getElementById('c-active').textContent = s.active;
    document.getElementById('c-rating').textContent = s.avg_rating ? s.avg_rating + ' ★' : '–';
    document.getElementById('c-sub-total').textContent  = s.ended + ' ended, ' + s.active + ' active';
    document.getElementById('c-sub-active').textContent = s.active === 1 ? '1 live session' : s.active + ' live sessions';
    document.getElementById('c-sub-rating').textContent = s.with_feedback ? 'From ' + s.with_feedback + ' rated thread(s)' : 'No ratings yet';

    const pct = s.with_feedback > 0 ? Math.round(s.positive / s.with_feedback * 100) : 0;
    document.getElementById('c-pos').textContent = pct + '%';
    document.getElementById('c-sub-pos').textContent = s.with_feedback ? s.positive + ' of ' + s.with_feedback + ' rated' : 'No ratings yet';

    // Sentiment bar
    if (s.with_feedback > 0) {
      const t = s.with_feedback;
      document.getElementById('sb-pos').style.width = (s.positive/t*100)+'%';
      document.getElementById('sb-neu').style.width = (s.neutral /t*100)+'%';
      document.getElementById('sb-neg').style.width = (s.negative/t*100)+'%';
    }
    document.getElementById('leg-pos').textContent   = 'Positive: ' + s.positive;
    document.getElementById('leg-neu').textContent   = 'Neutral: '  + s.neutral;
    document.getElementById('leg-neg').textContent   = 'Negative: ' + s.negative;
    document.getElementById('leg-total').textContent = s.with_feedback + ' thread(s) rated';

    // Table
    document.getElementById('tbl-count').textContent = d.threads.length + ' thread(s)';
    const tbody = document.getElementById('tbl-body');
    if (d.threads.length === 0) {
      tbody.innerHTML = '<tr><td colspan="9" class="no-data">No threads yet.</td></tr>';
    } else {
      tbody.innerHTML = d.threads.map(t => {
        const fb   = t.feedback;
        const sent = fb.sentiment || 'unknown';
        const stat = t.status;
        const stars = fb.rating
          ? '★'.repeat(fb.rating) + '<span style="color:#30363d">' + '★'.repeat(5-fb.rating) + '</span>'
          : '<span style="color:#6e7681">–</span>';
        const liveTag = stat === 'active'
          ? '<span class="pulse"></span>'
          : '';
        return `<tr>
          <td class="uid">${esc(t.user_id)}</td>
          <td><span class="badge b-${t.source}">${t.source}</span></td>
          <td class="ts">${esc(t.started_at)}</td>
          <td class="ts">${t.duration || (stat === 'active' ? liveTag+'live' : '–')}</td>
          <td style="text-align:center">${t.msg_count}</td>
          <td><span class="badge b-${stat}">${stat.replace('_',' ')}</span></td>
          <td class="stars-cell">${stars}</td>
          <td><span class="badge b-${sent}">${sent}</span></td>
          <td class="preview">${esc(t.preview)}</td>
        </tr>`;
      }).join('');
    }

    document.getElementById('last-ts').textContent = new Date().toLocaleTimeString();
  } catch(e) {
    console.error(e);
  }
}

function esc(t) {
  return String(t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

load();
setInterval(load, 5000);
</script>
</body>
</html>"""
