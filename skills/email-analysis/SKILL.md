---
name: email-analysis
description: Use when the user invokes /email-analysis with a keyword to search Outlook mailbox threads, analyze per-thread content, and synthesize cross-thread insights including timeline, stakeholders, patterns, and unresolved items.
---

# Email Analysis

Search your entire Outlook mailbox for emails matching a keyword, group them into conversation threads, analyze each thread, then synthesize cross-thread intelligence: timeline of topic evolution, recurring stakeholders, patterns, and unresolved items.

---

## Arguments

Parse the invocation string for these arguments before doing anything else:

| Argument | Type | Default | Values |
|----------|------|---------|--------|
| `keyword` | required | — | Any word or phrase |
| `days=N` | optional | `50` | Any integer |
| `scope=...` | optional | `subject` | `subject` / `body` / `both` |
| `visual` | optional flag | off | Presence = true |

**If `keyword` is missing:** ask for it before proceeding. Do not guess.

**Examples:**
```
/email-analysis CX-5
/email-analysis CX-5 days=10
/email-analysis deployment scope=both
/email-analysis budget days=30 visual
```

---

## Step 1 — Print Summary Header

Always print this as the very first line of output (before any data fetch):

```
**Keyword:** "<keyword>" | **Scope:** <scope> | **Period:** last <days> days (<start_date> → <today>)
```

Calculate `start_date` = today − days (display as YYYY-MM-DD).

---

## Step 2 — Fetch Emails

Calculate `afterDateTime` = today − days in ISO 8601 format (e.g. `2026-03-23T00:00:00`).

Call `outlook_email_search` with:
- `afterDateTime`: calculated value
- `limit`: 100
- Do **not** pass `folderName` — this searches all folders

If the tool returns an error, report it briefly and stop.

---

## Step 3 — Filter by Keyword

Apply case-insensitive keyword matching based on `scope`:

| scope | Match against |
|-------|--------------|
| `subject` | `subject` field only |
| `body` | body / summary field only |
| `both` | either field |

If zero emails match: report `No emails found matching "<keyword>" in the last <days> days.` and stop.

---

## Step 4 — Group Into Threads

Group matching emails by `conversationId`. If `conversationId` is unavailable, group by normalized subject (strip Re:/Fwd: prefixes, lowercase, trim).

Sort threads by most recent message descending.

---

## Step 5 — Analyze Each Thread

For every thread, extract:

- **Subject** — the thread subject
- **Participants** — all senders/recipients (deduplicated)
- **Date range** — first message date → last message date
- **Message count** — total emails in thread
- **Key ask or decision** — the main question, request, or decision point in the thread
- **Status** — classify as one of: `open` / `resolved` / `pending` / `FYI`
- **Tone shift** — note if the thread escalated, stalled, or resolved over time (only if detectable)

---

## Step 6 — Cross-Thread Intelligence Synthesis

After analyzing all threads, synthesize across them:

- **Key Insight** — 2-3 sentence executive summary: what is really happening around this keyword across the date range?
- **Topic Timeline** — chronological narrative of how the topic evolved, referencing specific threads and dates
- **Recurring Stakeholders** — people appearing in 2+ threads; infer their role from context
- **Patterns Detected** — e.g. same issue resurfacing, multiple teams involved, escalation arc, repeated asks with no response
- **Unresolved Items** — open asks or decisions with no resolution, each with: item description + thread subject + date

---

## Step 7 — Output

### Markdown output (default)

```markdown
## Email Analysis

**Keyword:** "CX-5" | **Scope:** subject | **Period:** last 10 days (2026-05-02 → 2026-05-12)
**Threads found:** N

---

### Intelligence Summary
[2-3 sentence key insight]

### Topic Timeline
[Chronological narrative — reference thread subjects and dates inline]

### Recurring Stakeholders
- [Name] — appears in N threads — [inferred role]

### Patterns Detected
- [Pattern]

### Unresolved Items
- [Item description] — "[Thread subject]" — [Date]

---

### Thread Details

#### Thread 1: [Subject] | [Start date → End date] | [Status] | [N messages]
**Participants:** [names]
**Key ask / decision:** [one sentence]
**Tone:** [escalating / stable / resolved / stalled — only if notable]

[repeat for each thread, most recent first]
```

### Visual output (when `visual` flag is present)

Render a single self-contained HTML widget via `show_widget`. Structure:

1. **Header card** — keyword, scope, period, thread count (blue accent)
2. **Intelligence summary card** — key insight text in highlighted block (amber border)
3. **Timeline strip** — horizontal bar showing thread activity across the date range; one row per thread, bar width proportional to thread duration, labeled with thread subject; x-axis spans start_date → today
4. **Thread cards** — one card per thread with:
   - Status badge (green = resolved, amber = pending, red = open, gray = FYI)
   - Participant chips
   - Date range
   - Key ask/decision text
5. **Unresolved items section** — amber card, bulleted list; omit section if none
6. **Footer** — "N threads found | Searched: all folders | Period: start_date → today"

Use the same color system as `daily-email-brief`: confirmed blue `#B5D4F4`, amber `#F5C4B3`, resolved green `#C0DD97`, neutral gray `#D3D1C7`.
