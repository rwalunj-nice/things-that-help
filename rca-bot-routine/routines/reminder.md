# Routine 1 — RCA Forum Reminder

**Trigger:** Weekly, Monday 08:00 local time  
**Type:** Remote  
**Model:** Claude Haiku 4.5 (`claude-haiku-4-5`) — mechanical task, no judgment required  
**Connectors:** Atlassian + Microsoft 365  
**Environment:** none — all auth handled by connectors (Atlassian OAuth + Microsoft 365 OAuth)

---

## How Teams Posting Works

The Microsoft 365 connector provides Claude with authenticated access to Microsoft Graph API during each run. No Power Automate, no webhook URL, no stored tokens required. Claude posts directly to the recurring meeting chat using the chat thread ID below.

**Teams meeting chat thread ID:**
```
19:meeting_OWJjZWExZmQtNDdiNy00ZjQ3LWIyZDItMDk3YTE3OTdhNTgx@thread.v2
```
Update this ID if the recurring meeting series is ever recreated.

---

## Prompt

Copy the text below verbatim into the Routine's prompt field at `claude.ai/code/routines`.

```
You are the RCA Forum Reminder for the INT team's weekly Monday evening RCA forum.

STEP 1 — Fetch tonight's bugs:
Search Jira with JQL: filter=97314
Extract from each issue: key, summary, assignee display name.

STEP 2 — Build the message text:
If bugs exist:
  "📋 RCA Forum tonight — bugs to present:\n• [KEY] Summary — Assignee Name\n(one bullet per bug)"
If no bugs:
  "📋 RCA Forum tonight — no bugs currently flagged for review."

STEP 3 — Post to Teams meeting chat:
Use the Microsoft 365 connector to send a message to Teams chat:
  Chat ID: 19:meeting_OWJjZWExZmQtNDdiNy00ZjQ3LWIyZDItMDk3YTE3OTdhNTgx@thread.v2
  Message: the text built in STEP 2

STEP 4 — Log: "Reminder posted for N bugs" or any errors.
```
