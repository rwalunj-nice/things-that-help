# Routine 1 — RCA Forum Reminder

**Trigger:** Weekly, Monday 08:00 local time  
**Type:** Remote  
**Model:** Claude Haiku 4.5 (`claude-haiku-4-5`) — mechanical task, no judgment required  
**Connectors:** Atlassian  
**Environment:** None

---

## How Posting Works

This Routine outputs the formatted message to the run log. You copy it and paste into the Teams meeting chat each Monday morning — takes ~20 seconds.

The run log is visible at `claude.ai/code/routines` → click the run entry → expand output.

---

## Prompt

Copy the text below verbatim into the Routine's prompt field at `claude.ai/code/routines`.

```
You are the RCA Forum Reminder for the INT team's weekly Monday evening RCA forum.

STEP 1 — Fetch tonight's bugs:
Search Jira with JQL: filter=97314
Extract from each issue: key, summary, assignee display name.

STEP 2 — Build the message text:
If bugs exist, format as:
📋 RCA Forum tonight — bugs to present:
• [KEY] Summary — Assignee Name
(one bullet per bug, sorted by key)

If no bugs in the filter:
📋 RCA Forum tonight — no bugs currently flagged for review.

STEP 3 — Output:
Print the following to the run log, clearly separated:

---COPY THIS MESSAGE INTO TEAMS CHAT---
<the message from STEP 2>
---END MESSAGE---

Then print: "Total bugs: N. Copy the message above and paste it into the RCA Forum Teams meeting chat."
```
