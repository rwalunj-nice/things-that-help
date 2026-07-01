---
name: daily-email-brief
description: "Generates a structured daily briefing by scanning Outlook inbox, Microsoft Teams chat messages, Outlook Calendar, and Jira — then renders the results as an interactive visual dashboard with linked action items, a meeting timeline, security alerts, and summary stats. Trigger this skill whenever the user asks for: \"daily briefing\", \"daily email brief\", \"morning briefing\", \"catch me up\", \"what's on my plate today\", \"what do I have today\", \"what's happening today\", \"email briefing\", \"briefing for today\", or any variation that implies a cross-source summary of the user's day. When in doubt, use this skill — it is always better to run a full briefing than to answer from memory alone."
---

# Daily email brief

Generate a structured daily briefing for the signed-in user. Follow all four
phases below in order. The final output is always a `show_widget` call — never
output the briefing as markdown text.

---

## Phase 1 — Fetch data (parallel)

Call all four sources **simultaneously** in a single round of tool calls:

| Source | Tool | Parameters |
|---|---|---|
| Outlook inbox | `outlook_email_search` | `afterDateTime`: 3 days ago, `folderName`: Inbox, `limit`: 25 |
| Teams chat | `chat_message_search` | `query`: *, `afterDateTime`: 3 days ago, `limit`: 25 |
| Calendar | `outlook_calendar_search` | `query`: *, `afterDateTime`: today, `beforeDateTime`: tomorrow, `limit`: 25 |
| Jira | `searchJiraIssuesUsingJql` | JQL: `assignee = currentUser() AND updatedDate >= -7d ORDER BY updated DESC`, `maxResults`: 15, cloudId: `nice-ce-cxone-prod.atlassian.net` |

If a source errors, note it and continue. A partial briefing is better than none.

---

## Phase 2 — Process

Apply these steps in order to the raw data:

### Noise filtering
Remove: automated/noreply senders, booking confirmations, marketing emails,
Confluence daily digests, calendar accept/decline with no body, one-word Teams
acknowledgements not directed at the user.

### Signal extraction
Classify surviving items into:
- **Action items** — direct requests, approvals, @mentions with a question,
  open incident threads, assigned tasks
- **Security alerts** — emails from Synack/CSOC/security tooling with CVSS
  scores or incident IDs
- **Meeting facts** — all calendar events for today
- **FYI updates** — awareness items needing no action

### Priority scoring
Score each action item:
- **Urgent**: explicit EOD deadline, direct @mention with ask, approval request
  with count, active incident with recent back-and-forth
- **Medium**: open incident active today but no deadline, setup tasks before a
  scheduled event, permission requests
- **Low**: tasks with no due date, Confluence tasks without deadline

### Conflict detection
Compare calendar start/end times. Flag overlapping events.

### IST conversion
Convert all calendar UTC timestamps to IST (UTC+5:30). Compute decimal hours:
e.g. 2:30 PM IST = 14.5.

---

## Phase 3 — Build JSON

Construct a single JSON object matching this exact schema. Every field is
required (use empty arrays `[]` where no items exist):

```json
{
  "meta": {
    "date": "Wednesday, July 1 2026",
    "dateKey": "2026-07-01",
    "user": "Rahul Walunj"
  },
  "stats": {
    "meetings": 16,
    "actionItems": 9,
    "securityAlerts": 0,
    "emailsTotal": 52,
    "emailsUnread": 15
  },
  "meetings": [
    {
      "subject": "Devgiri Daily Scrum",
      "start": 9.5,
      "end": 10.0,
      "type": "confirmed",
      "conflict": false
    }
  ],
  "conflicts": [
    "1-1:SM vs Torna Scrum · 11:00–11:15 IST"
  ],
  "actions": [
    {
      "id": "o-approve-q2-headcount",
      "pri": "urgent",
      "src": "O",
      "title": "Approve Q2 headcount request by EOD",
      "detail": "VP Engineering needs approval for 3 new headcount in the platform team. Deadline is end of business today.",
      "search": "RE: Q2 Headcount Request - Platform Team",
      "link": "https://outlook.office.com/..."
    }
  ],
  "alerts": [
    {
      "title": "Critical XSS in Portal",
      "cvss": 8.5,
      "cat": "Web Application · XSS",
      "tool": "Synack",
      "date": "Jul 1"
    }
  ],
  "fyi": [
    {
      "icon": "✅",
      "text": "Tanmay: Fix packaging job → DONE · Deployment job → DONE"
    }
  ],
  "summary": "Daily briefing generated for Jul 1 2026. 4 urgent action items..."
}
```

**Field rules:**
- `meetings[].start` / `.end` — decimal hours in IST (9.5 = 9:30 AM)
- `meetings[].type` — one of: `confirmed`, `tentative`, `oof`, `cancelled`
- `meetings[].conflict` — `true` if this event overlaps another
- `actions[].id` — stable slug: lowercase source letter + hyphenated subject
  (e.g. `o-approve-q2-headcount`). Must be deterministic for localStorage.
- `actions[].pri` — one of: `urgent`, `medium`, `low`
- `actions[].src` — one of: `O` (Outlook), `T` (Teams), `J` (Jira), `C` (Confluence)
- `actions[].search` — the raw subject/summary from the API (for clipboard copy)
- `actions[].link` — the `webLink` from the source API response
- `actions[].detail` — 2–3 sentence executive summary of the content
- `fyi[].icon` — one emoji that fits the content
- `summary` — 2–4 sentence prose summary of the day's key signals. Do NOT wrap
  in XML tags. Plain text only.

---

## Phase 4 — Render

1. Read the template file: `view /mnt/skills/user/daily-email-brief/template.html`
2. In the template source, find the token `__BRIEFING_JSON__` and replace it
   with the JSON object from Phase 3 (valid JS object literal, on one line).
3. Call `show_widget` with:
   - `title`: `daily_briefing_YYYY_MM_DD` (today's date)
   - `widget_code`: the template HTML with data injected
   - `loading_messages`: `["Scanning four sources…", "Filtering signal from noise…", "Assembling your dashboard…"]`

**Critical rules:**
- Do NOT modify the template HTML/CSS/JS in any way. Only replace the data
  placeholder.
- Do NOT output the briefing as markdown text. The widget IS the output.
- Do NOT wrap any text in XML tags like `<run-summary>`.
- If all sources return empty, output a plain text message instead.

---

## Example trigger phrases
- "Daily Email Briefing"
- "Give me my daily brief"
- "Morning briefing"
- "What's on my plate today?"
- "Catch me up on everything"
- "What do I have today?"
- "Run my briefing"
