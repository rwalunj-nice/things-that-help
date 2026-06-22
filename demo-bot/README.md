# Swarm Resolution Assistant — Demo

**Category:** Customer Swarms & Supportability

Suggests probable root causes and step-by-step remediation actions for active swarms by mining historical resolution patterns.

**Output per query:**
- Ranked root cause hypotheses
- Recommended investigation steps
- Historical resolution playbooks

```
Browser / Teams → FastAPI → Knowledge Base (84 swarm patterns)
                              ↘ Session Store → /dashboard (live)
```

---

## Quick Start (5 minutes)

### 1. Install dependencies

```bash
cd demo-bot
pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
# TEAMS_HMAC_SECRET is optional — leave blank for local testing
```

### 3. Start the server

```bash
python -m uvicorn main:app --reload
# Server runs at http://localhost:8000
```

### 4. Open the browser UI

Navigate to **http://localhost:8000** — you'll see the landing screen.

- Click **Start New Thread** to begin a conversation session
- Each session gets an auto-generated anonymous ID (e.g. `Swift-Falcon-483`)
- Use the **End Thread** button to close the session and submit a star rating
- Navigate to **http://localhost:8000/dashboard** to see all threads with live sentiment analysis

### 5. Expose to the internet (for Teams)

```bash
ngrok http 8000
# Copy the https URL, e.g. https://abc123.ngrok.io
```

### 6. Create a Teams Outgoing Webhook

In any Teams channel:
1. Click `···` → **Manage channel** → **Outgoing Webhooks** tab
2. Click **Add an outgoing webhook**
3. **Name**: `Swarm Assistant`
4. **Callback URL**: `https://<your-ngrok-id>.ngrok.io/webhook`
5. Copy the **HMAC security token** → paste into `.env` as `TEAMS_HMAC_SECRET`
6. Restart the server

### 7. Demo it in Teams

```
@Swarm Assistant agents cannot log in
@Swarm Assistant calls are dropping — quality degraded
@Swarm Assistant recording playback error 8203
@Swarm Assistant recordings stuck pending upload
@Swarm Assistant PCI masking not working
```

---

## Test without Teams (Session API)

```bash
# 1. Create a new session
curl -X POST http://localhost:8000/api/session/new
# → {"session_id": "abc12345", "user_id": "Swift-Falcon-483"}

# 2. Send a message in that session
curl -X POST http://localhost:8000/api/session/abc12345/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "agents cannot log in authentication failure"}'

# 3. End the session
curl -X POST http://localhost:8000/api/session/abc12345/end

# 4. Submit feedback
curl -X POST http://localhost:8000/api/session/abc12345/feedback \
  -H "Content-Type: application/json" \
  -d '{"rating": 5, "comment": "Very helpful, identified the issue immediately"}'

# 5. Check all threads on the dashboard API
curl http://localhost:8000/api/threads
```

---

## Features

| Feature | Details |
|---|---|
| **Thread management** | Each user gets an auto-generated anonymous session ID; threads persist until explicitly ended |
| **Stop button** | "End Thread" button in the chat UI; thread does not close automatically |
| **Feedback & rating** | 1–5 star rating + optional comment collected on thread close |
| **Dashboard** | Open at `/dashboard` — shows all threads from all users (browser + Teams) |
| **Sentiment analysis** | Keyword + rating analysis per thread; aggregate stats (% positive, avg rating, distribution bar) |
| **Teams webhook** | Stateless Q&A via Teams Outgoing Webhook; Teams sessions also appear on the dashboard |
| **Live refresh** | Dashboard auto-refreshes every 5 seconds |

---

## Knowledge Base — 84 Swarm Patterns

### Platform / Infrastructure (66 patterns)

| # | Swarm Type | Key Signals |
|---|---|---|
| 1 | Login / Authentication failure | SSO, session, Redis |
| 2 | SSO / SAML / IdP failure | SAML cert, clock skew |
| 3 | API 500 internal server errors | Stack traces, deploys |
| 4 | API 429 rate limiting / throttling | Quota, retry storm |
| 5 | Call drop / quality degradation | SIP trunk, RTP, QoS |
| 6 | Recording unavailable | Storage, firewall, license |
| 7 | IVR / routing failure | Skill groups, CTI, dial plan |
| 8 | High latency / slow response | DB queries, GC, APM |
| 9 | Database connection timeout | Pool exhaustion, HPA |
| 10 | CRM integration sync failure | OAuth, API version |
| 11 | Certificate / TLS expiry | Cert chain, LB listeners |
| 12 | Outbound dialer failure | DNC list, TCPA, pacing |
| 13 | Queue overflow / wait time spike | Volume surge, overflow rules |
| 14 | Real-time reporting lag | Kafka, Redis, WebSocket |
| 15 | Historical reporting failure | ETL, timezone, warehouse |
| 16 | Agent desktop freeze / crash | Memory leak, extensions |
| 17 | Chat / digital channel failure | Broker, CDN, bot handoff |
| 18 | Email channel / delivery failure | SPF/DKIM, relay quota |
| 19 | Speech analytics / ASR failure | Codec, model regression |
| 20 | WFM scheduling failure | Data feed, publish, Erlang-C |
| 21 | Redis cache failure | OOM, cluster slots, config |
| 22 | Kafka consumer lag | Partition, poison pill, I/O |
| 23 | Kubernetes pod crash loop | OOMKill, liveness probe |
| 24 | CPU spike / throttling | cgroup limit, HPA cooldown |
| 25 | Disk storage exhaustion | Logs, core dumps, temp files |
| 26 | DNS resolution failure | CoreDNS, Route 53, split-horizon |
| 27 | Load balancer unhealthy (502/503) | Health check path, SG |
| 28 | Microservice timeout cascade | Bulkhead, circuit breaker |
| 29 | Config deployment / rollback | Env vars, migrations, flags |
| 30 | Elasticsearch failure | Shard health, JVM heap |
| 31 | Webhook delivery failure | Endpoint, signing secret |
| 32 | LDAP / AD sync failure | Service account, LDAPS cert |
| 33 | NTP / clock drift | JWT, SAML, Chrony |
| 34 | Multi-tenant data isolation | Cache keys, tenant_id filter |
| 35 | Screen recording failure | Agent service, GPO, disk buffer |
| 36 | Voicemail failure | Storage quota, dial plan |
| 37 | Quality monitoring failure | Metadata, routing, scoring |
| 38 | Data pipeline / ETL failure | Schema change, memory, creds |
| 39 | Database replication lag | Redo log, I/O, bulk inserts |
| 40 | Health check / liveness failure | Probe config, deep check |
| 41 | TLS handshake failure | Cipher suite, mTLS |
| 42 | Thread pool exhaustion | Blocking I/O, bulkhead |
| 43 | JVM GC / heap pressure | Full GC, memory leak, MAT |
| 44 | Deadlock / lock contention | OLTP vs analytics, Redis lock |
| 45 | CDN / static asset failure | Cache invalidation, origin |
| 46 | Secret rotation credential failure | Vault, cache TTL |
| 47 | Canary deployment regression | Traffic weight, metric threshold |
| 48 | Third-party dependency timeout | External SLA, fallback mode |
| 49 | Network packet loss / jitter | MTR, BGP, QoS, transceiver |
| 50 | Audit log / compliance failure | Fluent Bit, SIEM, HEC token |
| 51 | Backup job failure | IAM, staging disk, timeout |
| 52 | API Gateway 504 timeout | Gateway vs upstream timeout |
| 53 | IdP (Okta/Azure AD) outage | OIDC, JWK, emergency auth |
| 54 | WebSocket connection drops | ALB idle timeout, proxy config |
| 55 | Batch / scheduled job failure | Lock TTL, poison pill, schema |
| 56–66 | Additional platform patterns | Database, network, storage edge cases |

### CXone Recording-Specific (18 patterns — derived from real incident CSV)

| # | Pattern | Recurrence | Key Signals |
|---|---|---|---|
| 67 | Playback unavailable (Error 8203/9002/8101/8210) | 9 | Short recordings, SIPREC, File Storage |
| 68 | Corrupt audio / early stop | 7 | ffmpeg, File Storage, packet loss |
| 69 | Search & Replay indexing gap | 6 | Replay service, Elasticsearch |
| 70 | SIPREC / RTP missing audio channel | 5 | SBC config, audio channel |
| 71 | Contact History recording missing | 5 | Queue not in profile |
| 72 | Transcription / analytics not generated | 4 | Profile not enabled |
| 73 | Upload service token expiry (Pending Upload backlog) | 8 | Token TTL, File Storage |
| 74 | Encryption key rotation not propagated to playback | 3 | Key rotation, playback |
| 75 | Archive rehydration lifecycle policy mismatch | 4 | Glacier, lifecycle, S3 |
| 76 | On-demand recording — Do Not Record profile override | 3 | Profile, override |
| 77 | Screen Agent blank/black screen | 5 | GPU driver, Screen Agent |
| 78 | Recording truncated — RTP stream loss mid-call | 6 | RTP, stream, truncated |
| 79 | Voice/screen out of sync — NTP clock drift | 4 | NTP, clock, sync |
| 80 | PCI pause/resume latency — DTMF audible | 7 | PCI, DTMF, masking |
| 81 | Supervisor view scope missing post-reorg agents | 3 | Permission, scope, supervisor |
| 82 | Bulk export empty files — packager timeout | 4 | Export, packager, timeout |
| 83 | Segment association stitching error on transferred calls | 5 | Transfer, segment, stitching |
| 84 | UserHub/ACD sync — null hireDate from InData lambda | 3 | UserHub, ACD, lambda |

---

## How the Knowledge Base Works

Each pattern entry has:
- `topic`: space-separated keywords used for matching against the query
- `content`: structured response with Root Cause Hypotheses, Investigation Steps, and Historical Playbook

To add a new pattern:
1. Add an object to `knowledge.json`
2. Set `topic` to keywords that would appear in a natural swarm description
3. Structure `content` with the three sections using `**bold**` markdown headings
4. Restart the server

---

## Production Path

| Demo component | Production equivalent |
|---|---|
| FastAPI local server | AWS Lambda + Function URL |
| ngrok tunnel | Amazon API Gateway |
| Keyword search | Vector similarity search (Bedrock KB + embeddings) |
| knowledge.json | Structured incident database (RDS + JIRA history) |
| mock_llm() | Claude on AWS Bedrock (`invoke_model`) |
| In-memory session store | DynamoDB with TTL |
| Teams Outgoing Webhook | Azure Bot Service + Power Automate |
| Static patterns | Live ML model trained on incident resolution history |
| Basic sentiment (rating + keywords) | NLP sentiment model (Comprehend, or Claude) |
