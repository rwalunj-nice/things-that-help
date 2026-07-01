# Daily Email Brief — Setup Guide

A Claude skill that generates an interactive daily briefing dashboard every morning by scanning your Outlook inbox, Microsoft Teams messages, Outlook Calendar, and Jira — and rendering the results as a dark-themed visual dashboard with linked action items, a meeting timeline, conflict detection, and a FYI section.

---

## What It Looks Like

The output is a self-contained interactive HTML dashboard with:

- **4 stat cards** — Meetings today, Action items (with live progress tracking), Security alerts, Inbox emails
- **Meeting timeline** — Gantt-style IST timeline (9 AM–9:30 PM) with color-coded confirmed/tentative/OOF/conflict bars and named rows
- **Action items** — Accordion list grouped by priority (Urgent / Medium / Low), with source badges (Outlook / Teams / Jira), check-off buttons, clipboard copy, and localStorage persistence across the day
- **Security alerts** — CVSS score cards with proportional fill bars
- **FYI section** — Awareness items needing no action
- **Summary footer** — Natural language summary of the day's key signals

---

## Files in This Folder

| File | Purpose |
|---|---|
| `SKILL.md` | The skill definition Claude reads to know how to run the briefing |
| `template.html` | The fixed HTML/CSS/JS dashboard template. Claude reads this at runtime and injects data — it never generates the UI from scratch |
| `README.md` | This file |

---

## How It Works (Architecture)

The skill uses a **template-based approach** to ensure consistent output every run:

1. Claude fetches data from 4 sources in parallel
2. Claude processes the data (noise filter → signal extraction → priority scoring → conflict detection → IST conversion)
3. Claude builds a structured JSON object from the processed data
4. Claude reads `template.html`, replaces the `__BRIEFING_JSON__` token with the JSON, and calls `show_widget`

The UI never changes between runs — only the data does. This eliminates the rendering variance that plagued earlier prompt-only approaches (theme flipping, XML tag leakage, layout regressions).

---

## Prerequisites

Before setting this up, the following must be connected in your Claude account:

| Connector | What it provides | Where to connect |
|---|---|---|
| **Microsoft 365** | Outlook email, Outlook Calendar, Teams messages | Claude.ai → Settings → Integrations |
| **Atlassian** | Jira issues | Claude.ai → Settings → Integrations |

Both connectors must be **authorized** (not just installed) — the skill will call them at runtime using your credentials.

---

## Step-by-Step Setup

### Step 1 — Deploy the skill files to Cowork

The skill files need to live in Cowork's persistent skill directory so Claude can read them at runtime. You cannot copy files there from Windows directly — you must do it through a Cowork session.

1. Open Claude → start a **Cowork session**
2. Upload both `SKILL.md` and `template.html` from this folder
3. In the Cowork chat, ask Claude to deploy them:

```
Please deploy these two files to /mnt/skills/user/daily-email-brief/
- SKILL.md
- template.html
```

4. Verify by asking:

```
List the files in /mnt/skills/user/daily-email-brief/
```

You should see both files listed.

> **Note:** `/mnt/skills/user/` is Cowork's **persistent** storage — files here survive across sessions. Do not place them in `/home/claude/` which resets every session.

---

### Step 2 — Personalise the skill for yourself

Open `SKILL.md` and update these two things before deploying:

**1. Your name and email** (Phase 1, first line):
```
Generate a daily email briefing for [Your Name] ([your.email@company.com]).
```

**2. Your Jira cloud ID** (Phase 1, Jira row):
```
cloudId: `your-jira-instance.atlassian.net`
```

To find your Jira cloud ID, go to your Jira instance URL — it's the subdomain before `.atlassian.net`. For example if your Jira is at `acme.atlassian.net`, your cloudId is `acme.atlassian.net`.

**3. Your timezone** (Phase 2, IST conversion section):

The default is IST (UTC+5:30). If you're in a different timezone, update the offset and the decimal hour conversion example. For example for SGT (UTC+8):
```
Convert all calendar UTC timestamps to SGT (UTC+8). Compute decimal hours: e.g. 2:30 PM SGT = 14.5.
```

Also update the timeline window in `template.html` if your working hours differ from 9 AM–9:30 PM. Search for `minH=9,maxH=21.5` and adjust.

---

### Step 3 — Test interactively first

Before scheduling, run it manually to verify everything works:

1. Open a **new Claude chat** (not Cowork)
2. Set model to **Claude Sonnet 4.6, Medium effort, no extended thinking**
3. Type any of these phrases:
   - `daily email brief`
   - `morning briefing`
   - `what's on my plate today`

The skill triggers automatically from the natural language. You should see the loading messages:
- *Scanning four sources…*
- *Filtering signal from noise…*
- *Assembling your dashboard…*

Followed by the interactive dark-theme dashboard.

If the dashboard looks correct across 2–3 test runs, proceed to Step 4.

---

### Step 4 — Set up the scheduled Cowork task

This makes the briefing run automatically every morning.

1. Open **Cowork** in Claude
2. Go to **Scheduled Tasks** (or the equivalent scheduling UI)
3. Create a new scheduled task with these settings:

| Setting | Value |
|---|---|
| **Schedule** | Daily, 9:00 AM (your local time) |
| **Model** | Claude Sonnet 4.6 |
| **Effort** | Medium |
| **Extended thinking** | Off |
| **Prompt** | Paste the full contents of the scheduled prompt (see below) |

4. Make sure the Microsoft 365 and Atlassian connectors are **enabled** for the scheduled task (some Cowork setups require you to explicitly toggle connectors on per task)
5. Save and activate the task

---

### Step 5 — Verify the first scheduled run

The next morning after 9 AM, check Cowork for the output. Confirm:

- Dark background throughout (no white sections)
- All 4 stat cards populated with real numbers
- Meeting timeline shows today's actual meetings
- Action items reflect real emails/messages
- No `<run-summary>` or other XML tags visible in the summary text
- Loading messages match: *Scanning four sources…* etc.

If anything looks off, run it interactively first to debug, then re-check the scheduled task prompt.

---

## The Scheduled Task Prompt

Paste this entire block as the prompt in your scheduled Cowork task. Replace `[Your Name]` and `[your.email@company.com]` and `[your-jira.atlassian.net]` with your own values before pasting.

```
Generate a daily email briefing for [Your Name] ([your.email@company.com]). Follow all four phases below precisely.

## Phase 1 — Fetch data (parallel)

Call all four sources simultaneously in a single round of tool calls:

| Source | Tool | Parameters |
|---|---|---|
| Outlook inbox | `outlook_email_search` | `afterDateTime`: 3 days ago, `folderName`: Inbox, `limit`: 25 |
| Teams chat | `chat_message_search` | `query`: *, `afterDateTime`: 3 days ago, `limit`: 25 |
| Calendar | `outlook_calendar_search` | `query`: *, `afterDateTime`: today, `beforeDateTime`: tomorrow, `limit`: 25 |
| Jira | `searchJiraIssuesUsingJql` | JQL: `assignee = currentUser() AND updatedDate >= -7d ORDER BY updated DESC`, `maxResults`: 15, cloudId: `[your-jira.atlassian.net]` |

If a source errors, note it and continue. A partial briefing is better than none.

## Phase 2 — Process

Apply in order:

**Noise filtering** — Remove: automated/noreply senders, booking confirmations, marketing emails, Confluence daily digests, calendar accept/decline with no body, one-word Teams acknowledgements not directed at the user.

**Signal extraction** — Classify surviving items into:
- Action items: direct requests, approvals, @mentions with a question, open incident threads, assigned tasks
- Security alerts: emails from Synack/CSOC/security tooling with CVSS scores or incident IDs
- Meeting facts: all calendar events for today
- FYI updates: awareness items needing no action

**Priority scoring** — Score each action item:
- Urgent: explicit EOD deadline, direct @mention with ask, approval request with count, active incident with recent back-and-forth
- Medium: open incident active today but no deadline, setup tasks before a scheduled event, permission requests
- Low: tasks with no due date, Confluence tasks without deadline

**Conflict detection** — Compare calendar start/end times. Flag overlapping events.

**IST conversion** — Convert all calendar UTC timestamps to IST (UTC+5:30). Compute decimal hours: e.g. 2:30 PM IST = 14.5.

## Phase 3 — Build JSON

Construct a single JSON object matching this exact schema:

{
  "meta": {
    "date": "Wednesday, July 1 2026",
    "dateKey": "2026-07-01",
    "user": "[Your Name]"
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
      "subject": "Daily Scrum",
      "start": 9.5,
      "end": 10.0,
      "type": "confirmed",
      "conflict": false
    }
  ],
  "conflicts": [
    "Meeting A vs Meeting B · 11:00–11:15 IST"
  ],
  "actions": [
    {
      "id": "o-approve-q2-headcount",
      "pri": "urgent",
      "src": "O",
      "title": "Approve Q2 headcount request by EOD",
      "detail": "2-3 sentence executive summary of the email content.",
      "search": "RE: Q2 Headcount Request - Platform Team",
      "link": "https://outlook.office.com/..."
    }
  ],
  "alerts": [],
  "fyi": [
    { "icon": "✅", "text": "Description text here" }
  ],
  "summary": "Daily briefing for [date]. Key signals: ..."
}

Field rules:
- meetings[].start / .end — decimal hours in IST (9.5 = 9:30 AM)
- meetings[].type — one of: confirmed, tentative, oof, cancelled
- meetings[].conflict — true if this event overlaps another
- actions[].id — stable slug: lowercase source letter + hyphenated subject (e.g. o-approve-q2-headcount)
- actions[].pri — one of: urgent, medium, low
- actions[].src — one of: O (Outlook), T (Teams), J (Jira), C (Confluence)
- actions[].search — raw subject/summary from API (used for clipboard copy)
- actions[].link — webLink from source API response
- actions[].detail — 2-3 sentence executive summary
- fyi[].icon — one emoji that fits
- summary — 2-4 sentence prose summary. Do NOT wrap in XML tags. Plain text only.

## Phase 4 — Render

1. Read the template file: view /mnt/skills/user/daily-email-brief/template.html
2. In the template source, find the token __BRIEFING_JSON__ and replace it with the JSON object from Phase 3 (valid JS object literal, on one line).
3. Call show_widget with:
   - title: daily_briefing_YYYY_MM_DD (today's date)
   - widget_code: the template HTML with data injected
   - loading_messages: ["Scanning four sources…", "Filtering signal from noise…", "Assembling your dashboard…"]

Critical rules:
- Do NOT modify the template HTML/CSS/JS. Only replace the data placeholder.
- Do NOT output the briefing as markdown. The widget IS the output.
- Do NOT wrap any text in XML tags.
- If all sources return empty, output a plain text message instead.
```

---

## Model Recommendations

| Use case | Model | Effort | Extended thinking |
|---|---|---|---|
| **Scheduled daily run** | Claude Sonnet 4.6 | Medium | Off |
| **Interactive run / testing** | Claude Sonnet 4.6 | Medium | Off |
| **Debugging output issues** | Claude Opus 4.6 | High | On |
| **Modifying the skill/template** | Claude Opus 4.6 | High | On |

---

## Troubleshooting

**White/light background on the dashboard**
The `@media(prefers-color-scheme:light)` block has been removed from `template.html` and the body background is explicitly set to `#16161a`. If you see a white background, the old template is being used — redeploy `template.html` to `/mnt/skills/user/daily-email-brief/`.

**`<run-summary>` tags visible in the summary text**
The scheduled prompt is missing the "Do NOT wrap any text in XML tags" critical rule in Phase 4. Repaste the full prompt from the section above.

**Action items show as unreadable light text**
Same root cause as white background — old template in use. Redeploy.

**Briefing shows correct structure but wrong/empty data**
Check that both Microsoft 365 and Atlassian connectors are enabled for the scheduled task. Some Cowork configurations require connectors to be explicitly toggled on per task, not just globally.

**Wrong timezone on the meeting timeline**
Update the IST conversion instruction in Phase 2 of the prompt to match your timezone offset. Also update `minH` and `maxH` in `template.html` if your working hours fall outside 9 AM–9:30 PM.

**Skill not triggering in interactive chat**
The skill triggers on natural language phrases. Make sure `SKILL.md` is deployed to `/mnt/skills/user/daily-email-brief/SKILL.md` (not `/home/claude/` which resets). Verify with: `list /mnt/skills/user/daily-email-brief/` in a Cowork session.

**Jira returns no results**
Verify your `cloudId` is correct — it should be the full subdomain of your Jira instance (e.g. `acme.atlassian.net`). Also confirm the Atlassian connector is authorized with an account that has Jira access.

---

## Customisation Reference

| What to change | Where |
|---|---|
| Your name / email | Line 1 of the scheduled prompt and `SKILL.md` |
| Jira cloud ID | Phase 1 table in the scheduled prompt and `SKILL.md` |
| Timezone offset | Phase 2 IST conversion section in both files |
| Timeline hours (9 AM–9:30 PM) | `minH` and `maxH` in `template.html` (search for `minH=9,maxH=21.5`) |
| Dark background color | `background:#16161a` on the `body` rule in `template.html` |
| Email lookback window | `afterDateTime: 3 days ago` in Phase 1 (change to e.g. `yesterday` for 1 day or `-7d` for a week) |
| Teams lookback window | `afterDateTime: 3 days ago` in Phase 1 (same options as above) |
| Jira lookback window | `updatedDate >= -7d` in the JQL query |
| Number of emails fetched | `limit: 25` in the Outlook inbox row |

---

## File Version History

| Date | Change |
|---|---|
| Jul 1 2026 | Initial template-based approach — replaces prompt-only HTML generation |
| Jul 1 2026 | Forced dark theme — removed `prefers-color-scheme:light` override, set `body` background to `#16161a` |
| Jul 1 2026 | Outlook and Teams lookback changed from `yesterday` to `3 days ago` to catch older unactioned threads |
