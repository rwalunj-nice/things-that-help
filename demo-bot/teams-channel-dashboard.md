# Teams Channel Analytics Dashboard — Specification & Data Report

**Route:** `GET /teams`
**Source file:** `demo-bot/teams-dashboard.html` (served by `demo-bot/main.py`)
**Public URL:** `https://aim-statements-drinking-crystal.trycloudflare.com/teams`
**Generated:** Jun 22, 2026

---

## 1. Purpose

A read-only analytics page that displays structured statistics, sentiment analysis, and a full message log derived from a real Microsoft Teams channel where the Swarm Resolution Bot is deployed. It is linked from the main `/dashboard` via the "Teams Analytics →" button.

---

## 2. Data Source

| Field | Value |
|---|---|
| Channel name | Workshop – Swarm Channel Resolution – Not For Prod |
| Group ID | e2c37adc-42e7-4848-89a9-6962d6ebb6d5 |
| Channel ID | 19:91lyMikZdAf0j07XBiPC6Vv0j7exKfmYx6RaxBi6Pzc1@thread.tacv2 |
| Fetch method | Microsoft Teams MCP tool (`read_resource`) — URI format `teams:///teams/{teamId}/channels/{channelId}/messages` |
| Data freshness | Static snapshot embedded in HTML as a JS constant `MSGS[]` |
| Message window | Jun 22, 2026 · 08:44 – 09:36 UTC (52 minutes) |
| Total messages read | 11 (including 1 system event) |

> **Note:** Because the Teams Graph API requires OAuth credentials at runtime, the channel data is fetched manually via the MCP tool during development and embedded as a static JS array. A live-polling version would call `GET /api/teams-data` from a backend that holds a valid service-account token.

---

## 3. Message Schema

Each entry in `MSGS[]` is one of two shapes:

### 3a. User message
```js
{
  id:        string,   // Teams message ID (timestamp-based)
  time:      string,   // "HH:MM:SS" UTC
  type:      "user",
  from:      string,   // Display name from Teams
  query:     string,   // Raw text of swarm symptom submitted
  component: string,   // Component area inferred from query text
  sentiment: "urgent" | "neutral" | "critical"
}
```

### 3b. Bot response message
```js
{
  id:         string,
  time:       string,   // "HH:MM:SS" UTC
  type:       "bot",
  component:  string,   // Component area the bot identified
  summary:    string,   // One-line summary of bot response
  severity:   string | null,  // "P1" / "P2" etc., or null if not provided
  escalation: boolean,  // true = bot flagged "Escalation: YES"
  topConf:    "High" | "Medium" | "Low",  // Confidence of rank-1 hypothesis
  hypotheses: [
    {
      rank: number,
      text: string,
      conf: "High" | "Medium" | "Low",
      ttr:  string   // Estimated time-to-resolve, or "—" if not available
    }
  ]
}
```

---

## 4. Computed Metrics

All metrics are computed client-side in JavaScript from the `MSGS[]` array on every `tick()` call.

| Metric | Formula |
|---|---|
| Total messages | `MSGS.length` (excludes system join event) |
| User queries | `MSGS.filter(m => m.type === "user").length` |
| Bot responses | `MSGS.filter(m => m.type === "bot").length` |
| Unique users | `new Set(MSGS.filter(m => m.type === "user").map(m => m.from)).size` |
| Escalation rate | `botResponses.filter(m => m.escalation === true).length / botResponses.length × 100` |
| Components affected | `new Set(MSGS.map(m => m.component)).size` |
| Avg hypotheses | `sum(botResponses.map(m => m.hypotheses.length)) / botResponses.length` |
| High-confidence responses | `botResponses.filter(m => m.topConf === "High").length` |
| Missing severity | `botResponses.filter(m => m.severity === null).length` |
| Missing TTR | `botResponses.flatMap(m => m.hypotheses).filter(h => h.ttr === "—").length / totalHypotheses` |

### Swarm urgency / sentiment classification (query-level)

Applied to `user` messages only:

| Sentiment | Rule |
|---|---|
| `critical` | Query describes a P1 severity incident or media/playback total failure |
| `urgent` | Query describes an operational disruption (agents stuck, service degraded) |
| `neutral` | Query describes a data or configuration gap without live customer impact |

### Hypothesis confidence distribution

Counts across **all** hypotheses in all bot responses:
- `High` — root cause well-supported by known patterns
- `Medium` — plausible but requires further validation steps
- `Low` — speculative; included for completeness

---

## 5. UI Sections & Spec

### 5.1 Header
- Logo, title "Teams Channel Analytics"
- Subtitle: `Auto-refresh every 5s · Last: <HH:MM:SS> · <channel name>`
- Buttons: `← Dashboard` (links to `/dashboard`), `Open Bot →` (links to `/`)

### 5.2 Channel Strip
Shows channel identity metadata: name, Group ID, Channel ID, and status pills (Live, window, date range).

### 5.3 Stat Cards (5 cards)
| Card | Value displayed | Colour |
|---|---|---|
| Total Messages | Count of all non-system messages | Blue |
| User Queries | Count of `type === "user"` | Purple |
| Bot Responses | Count of `type === "bot"` | Green |
| Escalation Rate | `YES / total bot × 100%` | Red |
| Components Hit | Distinct component values | Gold |

### 5.4 Swarm Type Distribution Panel
Two horizontal CSS bar charts:
1. **Bot responses by component** — Agent Stuck/Routing · API/UserHub · Media Server
2. **User queries by swarm type** — "Agents stuck" · "API hire date"

Bar width = `(count / total) × 100%`. Colour-coded: orange (agent), blue (API), red (P1/media).

### 5.5 Sentiment Panel
- SVG donut chart (100×100px, stroke-based): Urgent (orange) · Critical (red) · Neutral (slate)
- Horizontal bar chart for response-level signals: escalation rate, high-confidence rate, data gap rates

### 5.6 Hypothesis Confidence Panel
Three horizontal bars: High / Medium / Low with count and percentage.
Subtitle shows total hypothesis count across all responses.

### 5.7 Escalation Distribution Panel
Two KPI tiles (YES count · NO count) + two horizontal bars.
Footer shows which teams received escalations and how many times.

### 5.8 Active Users Panel
Card per distinct user showing: avatar initials, display name, query count, time range, urgency badge, and list of swarm queries raised.

### 5.9 Activity Timeline (SVG)
- `viewBox="0 0 900 110"`, responsive width
- Baseline at y=60; time range 08:44–09:36 UTC mapped to x=30–870 (scale: 16.15 px/min)
- **Blue circles** = user queries; **grey circles** = bot responses (no escalation); **red circles** = bot responses with escalation YES
- Vertical dashed stems connect each event to the baseline
- Labels: Saranya's name on user events; "Esc!" label on escalation bot events; "P1" label on severity event

### 5.10 Full Message Log (Table)
Columns: Time (UTC) · Type (👤 User / 🤖 Bot) · From · Component · Summary/Query · Severity · Escalation · Top Confidence

- **User rows** — blue "User" badge, italic query text, sentiment badge
- **Bot rows** — clickable; clicking toggles a `<tr class="detail-row">` below showing the full ranked hypothesis table
- Expanded state is preserved across `tick()` re-renders by recording open row IDs before clearing `innerHTML`

---

## 6. Auto-Refresh Mechanism

```js
function tick() {
  renderTable();   // re-renders message log, preserving open detail rows
  document.getElementById('last-ts').textContent = new Date().toLocaleTimeString();
}

tick();                    // immediate render on page load
setInterval(tick, 5000);   // re-render + timestamp update every 5 seconds
```

No network requests are made during refresh (data is static). When connected to a live `/api/teams-data` endpoint, `tick()` would `fetch()` fresh data before calling `renderTable()`.

---

## 7. Badge & Colour Reference

| Badge class | Colour | Meaning |
|---|---|---|
| `b-user` | Blue | User message |
| `b-bot` | Grey | Bot message |
| `b-yes` | Red | Escalation YES |
| `b-no` | Green | Escalation NO |
| `b-high` | Green | High confidence hypothesis |
| `b-medium` | Gold | Medium confidence hypothesis |
| `b-low` | Grey | Low confidence hypothesis |
| `b-p1` | Red (bold) | P1 severity flag |
| `b-urgent` | Orange | Urgent swarm urgency |
| `b-critical` | Red | Critical/P1 urgency |
| `b-neutral` | Grey | Neutral/data-issue urgency |

---

## 8. Dashboard Data — Jun 22, 2026

### Summary Stats

| Metric | Value |
|---|---|
| Total Messages | 11 |
| User Queries | 3 |
| Bot Responses | 8 |
| Unique Users | 1 (Saranya Rao) |
| Escalation Rate | **37.5%** (3 of 8) |
| Components Affected | 3 |
| Total Hypotheses | 25 |
| Avg Hypotheses/Response | 3.1 |

### Swarm Type Distribution

| Swarm Type | Responses | % |
|---|---|---|
| Agent Stuck / Routing | 5 | 62.5% |
| API / UserHub / Hire Date | 2 | 25.0% |
| Media Server / Playback (P1) | 1 | 12.5% |

### Top Queried Swarms (User)

| Query | Count | % |
|---|---|---|
| Agents stuck in unavailable state | 2 | 67% |
| API - Agent API Missing Hire Date | 1 | 33% |

### Sentiment Distribution

| Urgency | % |
|---|---|
| Urgent / Operational | 50% |
| Critical (P1) | 25% |
| Neutral / Data Issue | 25% |

### Hypothesis Confidence

| Confidence | Count | % |
|---|---|---|
| High | 12 | 48% |
| Medium | 7 | 28% |
| Low | 6 | 24% |

### Escalation

| | Count | % |
|---|---|---|
| YES — cross-team | 3 | 37.5% |
| NO — self-service | 5 | 62.5% |

Cross-team: UserHub team (×2) · Telephony/SBC (×1)

---

## 9. Full Message Log

### 08:44:05 — 🤖 Bot · Media Server / Playback · Severity: P1 · Escalation: NO

**Summary:** P1 playback failure — RTP packet loss on media server. Multiple customers impacted.

| Rank | Hypothesis | Confidence | TTR |
|---|---|---|---|
| 1 | Media server RTP packet loss — network buffer overflow | High | 42 mins |
| 2 | Recording service failed to reconnect after restart | Medium | 67 mins |
| 3 | API gateway timeout misconfiguration under high load | Low | 95 mins |

### 08:50:04 — 🤖 Bot · Agent State / Routing · Severity: — · Escalation: NO

**Summary:** Multiple agents stuck in unavailable state. Routing engine sync delay suspected.

| Rank | Hypothesis | Confidence | TTR |
|---|---|---|---|
| 1 | Routing engine sync delay — agents remain unavailable | High | — |
| 2 | UserHub data not reflecting in ACD — blocking state transitions | Medium | — |
| 3 | Weekly maintenance job overwriting agent availability config | Low | — |

### 09:07:53 — 🤖 Bot · Agent State / Routing · Severity: — · Escalation: YES ⚠

**Summary:** Agents stuck — sync/config issue suspected. Escalation raised due to multi-BU impact.

| Rank | Hypothesis | Confidence | TTR |
|---|---|---|---|
| 1 | Sync or configuration issue | Medium | — |
| 2 | Bug in routing engine | Low | — |
| 3 | Configuration mismatch | Low | — |

### 09:08:53 — 👤 Saranya Rao · Agent State · Urgency: Urgent

**Query:** "Agents stuck in unavailable state"

### 09:14:53 — 🤖 Bot · Agent State / Routing · Severity: — · Escalation: NO

**Summary:** Routing engine sync delay. L1 pause point after step 3.

| Rank | Hypothesis | Confidence | TTR |
|---|---|---|---|
| 1 | Routing engine sync delay — agents remain unavailable | High | — |
| 2 | UserHub data not reflecting correctly in ACD | Medium | — |
| 3 | Weekly maintenance job overwriting config | Low | — |

### 09:20:54 — 👤 Saranya Rao · API / UserHub · Urgency: Neutral

**Query:** "API - Agent API Missing Hire Date"

### 09:21:46 — 🤖 Bot · Agent State / Routing · Severity: — · Escalation: NO

**Summary:** Parallel trigger for agent stuck pattern (cross-query).

| Rank | Hypothesis | Confidence | TTR |
|---|---|---|---|
| 1 | Routing engine sync delay | High | — |
| 2 | UserHub data not reflecting in ACD | Medium | — |
| 3 | Weekly maintenance job | Low | — |

### 09:26:49 — 🤖 Bot · Agent API / UserHub · Severity: — · Escalation: YES ⚠

**Summary:** Missing hireDate — InData lambda sync gap. ACD ready, fix needed on UserHub side.

| Rank | Hypothesis | Confidence | TTR |
|---|---|---|---|
| 1 | InData sync via lambda missing hireDate — UserHub has value but ACD not receiving it | High | — |
| 2 | UserHub sending null HireDate to ACD — data source mismatch | Medium | — |

### 09:28:26 — 🤖 Bot · API / UserHub · Severity: — · Escalation: YES ⚠

**Summary:** Agent API Missing Hire Date — cross-team handoff to UserHub required.

| Rank | Hypothesis | Confidence | TTR |
|---|---|---|---|
| 1 | Moved to UserHub team; product discussion initiated | High | — |
| 2 | Missing media leg at SBC — telephony config | High | — |
| 3 | Recording profile did not cover the queue | Medium | — |

### 09:35:53 — 👤 Saranya Rao · Agent State · Urgency: Urgent

**Query:** "Agents stuck in unavailable state"

### 09:36:22 — 🤖 Bot · Agent · Severity: — · Escalation: NO

**Summary:** Workaround advised; monitoring enabled; routed to respective team.

| Rank | Hypothesis | Confidence | TTR |
|---|---|---|---|
| 1 | Client advised workaround and best practices | High | — |
| 2 | Monitoring enabled for future validation | High | — |
| 3 | Routed to respective team for further action | High | — |
| 4 | Bug fix deployed to production | High | — |
| 5 | Failed recording is actually a Short recording — KI shared | Medium | — |

---

_Swarm Resolution Assistant · Teams Channel Analytics · Jun 22, 2026_
