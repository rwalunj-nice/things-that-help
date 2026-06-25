---
name: daily-email-brief
description: >
  Generates a structured daily briefing by scanning Outlook inbox, Microsoft Teams
  chat messages, Outlook Calendar, and Jira — then renders the results as an
  interactive visual dashboard with linked action items, a meeting timeline,
  security alerts, and summary stats.

  Trigger this skill whenever the user asks for: "daily briefing", "daily email
  brief", "morning briefing", "catch me up", "what's on my plate today",
  "what do I have today", "what's happening today", "email briefing",
  "briefing for today", or any variation that implies a cross-source summary
  of the user's day. When in doubt, use this skill — it is always better to
  run a full briefing than to answer from memory alone.
---

# Daily email brief

Generate a structured daily briefing across all connected sources and render it
as an interactive visual dashboard. Follow the four sections below in order.

---

## 1. Data sources scan

Query all four sources **in parallel** (single round of simultaneous API calls).
Do not wait for one to finish before starting another.

| Source | Tool | Criteria |
|---|---|---|
| Outlook inbox | `outlook_email_search` | `afterDateTime: yesterday`, `folderName: Inbox`, `limit: 20` |
| Teams chat | `chat_message_search` | `query: *`, `afterDateTime: yesterday`, `limit: 30` |
| Outlook calendar | `outlook_calendar_search` | `query: *`, `afterDateTime: today`, `beforeDateTime: tomorrow`, `limit: 20` |
| Jira issues | `searchJiraIssuesUsingJql` | `assignee = currentUser() AND updatedDate >= -7d ORDER BY updated DESC`, `maxResults: 15` |

If a source is unavailable or returns an error, note it briefly and continue
with the remaining sources. A partial briefing is better than no briefing.

---

## 2. Parameters extracted

Use only these fields from each source's API response. Fields marked **key**
appear directly in the briefing output; others inform filtering and scoring.

**Outlook inbox**
- **key**: `subject`, `sender`, `importance`, `isRead`, `receivedDateTime`, `summary`, `webLink`
- filtering: `hasAttachments`, `recipients`, `internetMessageId`

**Teams chat**
- **key**: `summary` (or body text), `from.displayName`, `createdDateTime`, `importance`
- filtering: `chatId`, `lastModifiedDateTime`

**Outlook calendar**
- **key**: `subject`, `start`, `end`, `showAs`, `importance`, `isCancelled`, `organizer`, `location`
- filtering: `attendees`, `recurrence`, `webLink`

**Jira**
- **key**: `summary`, `status`, `priority`, `updated`
- filtering: `issuetype`, `assignee`

---

## 3. Process

Apply these steps in order after the data fetch completes.

### Step 1 — Noise filtering
Remove items that do not require user attention:
- Automated/system senders: `noreply`, `no-reply`, booking confirmations, marketing
- Digest-only emails (e.g. Confluence daily digest, promotional newsletters)
- Calendar acceptance/decline notifications with no body content
- Teams messages that are one-word acknowledgements from others (e.g. "ok", "yes", "done") unless directed at the user

### Step 2 — Personal action filter (Rahul-specific rules)
Before classifying action items, apply these personal filtering rules. Items that
fail any rule are demoted to **FYI** or dropped entirely:

1. **Direct name mention required** — An item is only an action item for Rahul if
   he is explicitly @mentioned by name ("Rahul" or "Rahul Walunj") in the message
   body. Group channel mentions (e.g. @Cloud Operations, @WFM Team) do **not**
   qualify as personal action items, even if Rahul is a member of that group.

2. **Team approval / change requests via group channels** — Change requests, CAB
   approvals, CHG tickets, or any approval requests posted in group channels are
   **not** action items. They are only actionable if someone pings Rahul directly
   1-1 and explicitly asks for his approval.

3. **Incident / P2 / Major Incident Teams notifications** — P2, Major Incident, or
   large-scale incident notifications that arrive as Teams missed-activity emails
   (sender: `365-noreply@nice.com`) are **not** action items. Only surface these
   if Rahul receives a direct email (not a Teams notification redirect) about the
   incident.

4. **Ask must be on Rahul, not on others** — If a message names Rahul in context
   (e.g. "Rahul said…") but the ask is directed at other people, it is **not** an
   action item for Rahul. Only classify as an action item when Rahul is the one
   expected to respond or act.

### Step 3 — Signal extraction
Classify remaining items into four buckets:

- **Action items** — direct requests explicitly addressed to Rahul by name, open
  incidents where Rahul's team owns the fix and action is expected from him, tasks
  assigned directly to Rahul
- **Security alerts** — emails from security tooling (Synack, CSOC, etc.)
  containing CVSS scores, incident IDs, or open vulnerability threads
- **Meeting facts** — all calendar events for today, including cancelled ones
  (note cancellation)
- **FYI updates** — awareness items requiring no immediate action (org
  announcements, weekly reports, Confluence page updates, group channel mentions,
  incident notifications via Teams email)

### Step 4 — Priority scoring
Score each action item as **urgent**, **medium**, or **low**:

- **Urgent**: explicit EOD deadline with Rahul as the named recipient, direct 1-1
  question or ask directed at Rahul, active incident thread where Rahul's team
  owns the fix and CSOC/external is waiting
- **Medium**: open incident thread active today but no explicit deadline,
  setup/install tasks needed before a scheduled event today
- **Low**: tasks with no due date, Confluence tasks without a deadline

### Step 5 — Conflict detection
Compare calendar event start times. If two or more events share the same start
slot, flag them with a conflict badge in the output and stack them visually on
the timeline.

### Step 6 — Link resolution
For each action item, attach the `webLink` from its source API record.
Teams-sourced items that arrived as notification emails should use the Outlook
`webLink` (which contains a "View in Teams" redirect). This is the link that
appears on click.

### Step 7 — Time conversion
Convert all calendar UTC timestamps to IST (UTC+5:30) before rendering. Compute
each meeting's position on the timeline as a percentage of a 9 AM–9:30 PM IST
window:

```
left%  = ((start_IST - 9) / 12.5) * 100
width% = ((end_IST - start_IST) / 12.5) * 100
```

---

## 4. Visualization strategy

Render a single self-contained HTML widget using the `show_widget` tool.
Structure it in this exact order:

### Summary stat cards (top row)
Four metric cards in a responsive grid:
- **Meetings today** — total calendar events (source: calendar count)
- **Action items** — count of extracted action items (source: signal extraction)
- **Security alerts** — count of security-classified items (source: signal extraction)
- **Emails (inbox)** — total emails scanned, with unread count as subtext (source: `isRead` flag)

Highlight meetings in blue, action items in amber, security in red, emails in neutral.

### Meeting timeline
- Horizontal axis: 9 AM to 9:30 PM IST, 14 equal columns
- One row per meeting, height 26–28px
- Bar width and left offset computed from IST start/end times (see Step 7)
- Color encodes `showAs`: confirmed = blue `#B5D4F4`, tentative = gray `#D3D1C7`,
  high importance = coral `#F5C4B3`, OOF = green `#C0DD97`,
  conflict = `#FAECE7` with coral border
- Show event label inside the bar if the bar is wide enough (>8% width);
  otherwise surface via `title` tooltip
- Conflict badge below the timeline if any overlaps were detected
- Include a color legend above the timeline

### Action items (linked list)
- Ordered: urgent first, then medium, then low
- Each item is an `<a>` anchor tag linking to its `webLink`
- Left: colored priority dot (red = urgent, amber = medium, gray = low)
- Center: item title + inline source badge (O = Outlook, T = Teams, C = Confluence)
- Right: ↗ arrow indicating it is a link
- On hover: subtle background change to confirm interactivity

### Security alerts
- One card per alert with CVSS score displayed prominently
- Proportional fill bar: width = (CVSS / 10) × 100%
- Sub-text: category, sub-category, source tool, date

### FYI section (if items exist)
- Simple flat list, no links required
- Muted styling to visually de-emphasise relative to action items

### Footer
Single line: count summary + sources scanned + date range covered.

---

## 5. Output format

The complete briefing is delivered as one `show_widget` call producing a
self-contained HTML dashboard. Do not split it across multiple widget calls.
Do not reproduce the briefing as markdown text — the widget is the output.

If Jira returns no results, omit the Jira row silently; do not show an error.
If all sources return empty, tell the user in plain text rather than rendering
an empty dashboard.

---

## Example trigger phrases

- "Daily Email Briefing"
- "Give me my daily brief"
- "Morning briefing"
- "What's on my plate today?"
- "Catch me up on everything"
- "What do I have today?"
- "Run my briefing"
