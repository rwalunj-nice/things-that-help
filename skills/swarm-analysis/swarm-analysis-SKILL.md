---
name: swarm-analysis
description: "Analyze CXone WorkBot support swarm threads from Microsoft Teams. Use this skill whenever the user shares a Teams swarm thread URL (from the TS/R&D Support Swarm team or any swarm channel), mentions 'swarm', 'swarm analysis', 'check this swarm', 'swarm conclusion', 'swarm summary', or references a Swarming Session (SS#). The skill parses the Teams URL, fetches the swarm card and all thread replies, discovers related cross-channel swarms for the same case, synthesizes findings into a structured root-cause analysis, and generates a recommended reply draft. Also trigger when user mentions swarm session numbers (e.g., SS048570), case numbers in the context of swarms, or asks about the status/conclusion of a support swarm."
---

# Swarm Analysis

Analyze CXone WorkBot support swarm threads from Microsoft Teams. Given a Teams swarm thread URL, this skill extracts the swarm metadata, fetches all replies and related cross-channel swarms, and synthesizes a structured conclusion with root-cause analysis, per-team findings, status assessment, and a recommended reply draft.

---

## Prerequisites

Before executing any step, load the Microsoft 365 tools:

```
tool_search(query="Teams chat message search")
```

This loads `Microsoft 365:chat_message_search` and `Microsoft 365:read_resource`.

Also read `/mnt/skills/user/microsoft365-connector/SKILL.md` for the M365 connector rules (KQL-first for Teams, pagination, timezone handling). Those rules apply to every Teams search in this skill.

---

## Step 1 — Parse the Teams URL

Extract identifiers from the user-provided Teams message URL. Teams swarm thread URLs follow this pattern:

```
https://teams.microsoft.com/l/message/
  19:<channelHash>@thread.skype/
  <messageId>?
  tenantId=<tenantId>&
  groupId=<teamId>&
  parentMessageId=<parentMessageId>&
  teamName=<teamName>&
  channelName=<channelName>&
  createdTime=<timestamp>
```

Extract these fields:

| Field | Source | Example |
|-------|--------|---------|
| `channelId` | URL path segment after `/message/` (URL-decoded) | `19:bb00bb0a5ac14a0e84e5db561287fd64@thread.skype` |
| `messageId` | Numeric ID after the channelId in the URL path | `1781021729383` |
| `teamId` | `groupId` query parameter | `930c10af-48f9-41b6-ba52-0345000ba7b3` |
| `channelName` | `channelName` query parameter (URL-decoded) | `IEX-Engage Integration` |
| `teamName` | `teamName` query parameter (URL-decoded) | `TS/R&D Support Swarm` |

If any required field cannot be extracted, report the parsing failure and ask the user for the missing information.

---

## Step 2 — Fetch the Initial Swarm Card

Call `Microsoft 365:read_resource` to retrieve the root message:

```
read_resource(uri="teams:///teams/{teamId}/channels/{channelId}/messages/{messageId}")
```

The CXone WorkBot posts swarm cards as **Adaptive Card attachments**. The message body will typically be null — all structured data is inside `attachments[0].content` (a JSON string).

### Parse the Adaptive Card JSON

Parse the Adaptive Card and extract these fields by walking the card body:

| Field | Location in Card | How to Find |
|-------|-----------------|-------------|
| **Swarm Session #** | First TextBlock with "Swarming Session#" prefix | Extract `SS######` from the text |
| **Swarm Status** | TextBlock starting with "Swarming Status :" | Extract the status value (Open, Closed, etc.) |
| **Case #** | FactSet with title "Case#" | Extract value |
| **Priority** | FactSet with title "Priority" | Extract value |
| **Created By** | FactSet with title "Created By" | Extract value |
| **Account** | FactSet with title "Account" | Extract value |
| **Cadebill #** | FactSet with title "Cadebill#" | Extract value |
| **Cluster** | FactSet with title "Cluster" | Extract value |
| **Subject** | FactSet with title "Subject" | Extract value |
| **Description** | TextBlock after "Description" header | Extract full text, preserve newlines |
| **Replication Steps** | TextBlock after "Replication Steps" header | Extract full text |
| **Troubleshooting Steps** | TextBlock after "Troubleshooting Steps" header | Extract full text |
| **Question for Swarm** | TextBlock after "Question for Swarm" header | Extract full text |
| **First Responder** | FactSet with title "Swarm Initially Acknowledged By" | Extract value |

If parsing fails (e.g., the card structure is unexpected), report what was successfully extracted and what failed, then continue with available data.

### Print Swarm Header

After parsing, immediately print a summary header:

```
**Swarm:** SS###### | **Case:** ####### | **Account:** ACCOUNT NAME | **Priority:** P# | **Channel:** Channel Name
**Created By:** Name | **First Responder:** Name | **Status:** Open/Closed
**Subject:** subject text
```

---

## Step 3 — Search for Replies in the Thread

Swarm discussions happen as replies in the same channel thread. The Microsoft 365 connector cannot directly fetch thread replies by `replyToId`, so use `chat_message_search` with KQL to find messages in the same channel about the same case.

### Search Strategy

Run multiple targeted searches to maximize reply coverage. Use the case number, account name, and swarm-specific keywords from the card:

**Search 1 — Case number + account name:**
```
chat_message_search(query="{caseNumber} {accountName}", limit=25)
```

**Search 2 — Swarm session number:**
```
chat_message_search(query="{swarmSessionNumber}", limit=25)
```

**Search 3 — Subject keywords + date range:**
Pick 2-3 distinctive keywords from the swarm subject. Use KQL `sent:` to bound the search from the swarm creation date to today:
```
chat_message_search(query="{keyword1} {keyword2} sent:{swarmCreatedDate}..{today}", limit=25)
```

**Search 4 — First responder + date range (catches terse replies):**
Many swarm replies are short ("checking", "agreed", "logs attached") and won't match keyword searches. Search by the first responder's email to catch their contributions even if they don't repeat the case number or subject terms:
```
chat_message_search(query="from:{firstResponderEmail} sent:{swarmCreatedDate}..{today}", limit=25)
```
Then client-side filter results to only keep messages whose `channelId` matches the swarm's channel. If other investigators are identified from earlier search results, run this search for them too (up to 3 additional `from:` queries to stay within practical limits).

### Filter and Deduplicate

From all search results:
1. **Deduplicate** by message `id` — the same message may appear in multiple searches
2. **Identify the original channel** — messages with `channelUri` matching the original swarm channel's `channelId`
3. **Identify cross-channel messages** — messages with a *different* `channelId` but the same case number (these are related swarms — see Step 4)
4. **Exclude the root swarm card** itself (matching the original `messageId`)

### Read Full Content of Each Reply

For each unique reply message found, attempt to read the full body using a **three-tier fallback strategy**. The Teams Graph API is inconsistent about which URI format works for channel thread replies — neither format is guaranteed, and some replies are only accessible via one or the other.

**Tier 1 — Chat URI (most reliable for replies):**
```
read_resource(uri="teams:///chats/{chatId}/messages/{replyMessageId}")
```

**Tier 2 — Channel URI (works for root messages, sometimes for replies):**
```
read_resource(uri="teams:///teams/{teamId}/channels/{channelId}/messages/{replyMessageId}")
```

**Tier 3 — Search snippet fallback:**
If both Tier 1 and Tier 2 return NOT_FOUND, use the `summary` field from the original `chat_message_search` result. This is a truncated preview (~200 chars) but still captures the key content of most swarm replies. When using this fallback, flag the message in the output:
```
[Content from search snippet — full message could not be retrieved]
```

**Known limitation:** The Teams API does not expose a reliable "get all replies to a thread" endpoint via the M365 connector. Reply discovery depends entirely on keyword-based search. This means very short replies ("agreed", "thanks", "+1") or replies using terminology not in the search queries may be missed entirely. The skill compensates by running multiple overlapping searches (Step 3) and by including a participant-based search (Search 4 below).

For each reply successfully read, extract:
- **Author** (displayName, email)
- **Timestamp** (createdDateTime — convert to IST for display)
- **Body text** (strip HTML tags for analysis, preserve structure)
- **Mentions** (who was @mentioned)
- **Attachments** (note if any Adaptive Cards are present — these may be bot updates)
- **Jira ticket references** (scan body for patterns like `[A-Z]+-\d+` — e.g., EM-162327, WFM-174707 — collect these for Step 4B)

---

## Step 4 — Discover Related Cross-Channel Swarms

A single customer case often spawns multiple swarms across different channels (e.g., IEX-Engage → WCX → ACD). These cross-channel swarms are critical for understanding the full investigation path.

### Detection

From Step 3's search results, any message whose `channelId` differs from the original swarm's channel AND references the same case number is a candidate for a related swarm.

### Fetch Related Swarm Cards

For each related swarm root message (identifiable by `from.displayName === "Cxone WorkBot"` or `"CXone WorkBot"` and containing an Adaptive Card attachment):

1. Call `read_resource` to get the full message
2. Parse the Adaptive Card using the same logic as Step 2
3. Extract the new swarm session number, channel name, first responder, and any updated description/troubleshooting steps

### Fetch Related Swarm Replies

For each related swarm, repeat Step 3's search strategy scoped by the related swarm's keywords:

```
chat_message_search(query="{relatedSwarmSessionNumber} {accountName}", limit=25)
```

Read full content of each related reply using `read_resource`.

### Build the Investigation Chain

Map the cross-channel flow:

```
Swarm 1 (SS048570, IEX-Engage Integration) 
  → finding: "data received, issue is upstream"
  → Swarm 2 (SS049075, ACD/WCX channel)
    → finding: "DX suppresses events by design"
```

---

## Step 4B — Fetch Referenced Jira Tickets

Swarm thread replies frequently reference Jira tickets inline (e.g., "tracked under EM-162327", "see WFM-174707", "bug logged as WFMDEV-4567"). These tickets often contain the authoritative root cause analysis, fix versions, and resolution status that the swarm thread only summarizes.

### Collect Ticket References

From all reply content gathered in Steps 3 and 4, scan for Jira ticket ID patterns: `[A-Z]{2,10}-\d+` (e.g., EM-162327, WFM-174707, INT-54696, DE-12345). Deduplicate the list.

### Fetch Each Referenced Ticket

For each unique ticket ID, load the Atlassian tools and fetch the ticket:

```
tool_search(query="Jira issue details")
Atlassian:getJiraIssue(cloudId="nice-ce-cxone-prod.atlassian.net", issueIdOrKey="{ticketId}", responseContentFormat="markdown", fields=["summary", "status", "assignee", "description", "comment", "issuelinks", "fixVersions", "resolution"])
```

From each ticket, extract:
- **Summary** — what the ticket tracks
- **Status** — Open / In Progress / Resolved / Closed
- **Fix Version(s)** — if available, this is the authoritative release target
- **Resolution** — if resolved, how (Fixed, WAD, Won't Fix, Duplicate)
- **Key comments** — scan for root cause findings, decisions, and references to other tickets
- **Linked issues** — "is fixed by", "is caused by", "relates to" — follow one level of links for fix version data

### Integration with Analysis

Include Jira findings in the output under "Related Jira Tickets" with substantive detail, not just ticket IDs. If a Jira ticket provides more authoritative root cause data than the swarm thread discussion, prefer the Jira data in the Root Cause section and cite the ticket.

**Skip this step if:** No Jira ticket IDs are found in any reply content, or if the Atlassian connector is not available (note the limitation in the disclosure block).

---

## Step 5 — Synthesize the Analysis

With all data collected (original swarm card, replies, related swarms, all reply content, and any Jira ticket data), produce a structured analysis.

### Analysis Framework

For each reply and related swarm finding, classify into:

| Category | What to Look For |
|----------|-----------------|
| **Root Cause** | Technical explanation of why the issue occurs. Look for: code behavior, event suppression, design decisions, configuration gaps |
| **Team Findings** | Per-team conclusions — what each team investigated and determined. Map: team/channel → their specific finding |
| **Data Flow** | How events/data move through the system. Identify where in the pipeline the issue occurs |
| **Resolution Options** | Any proposed fixes, workarounds, or enhancement paths mentioned |
| **Open Questions** | Unresolved items, pending verifications, or diagnostic steps not yet completed |
| **Working as Designed (WAD)** | Whether the behavior is intentional and under what conditions |

### Key Signals to Watch For

- **"Working as designed" / "expected behavior" / "intentional"** — indicates WAD conclusion
- **"Enhancement" / "epic" / "PM prioritization"** — indicates future roadmap item
- **"Defect" / "bug" / "fix"** — indicates a code issue with a potential fix path
- **"Workaround"** — indicates interim solution available
- **"Not supported"** — indicates a gap in product capability
- **Team handoffs** — "raised to ACD", "escalated to DFO team", "need to check with EM team" — trace the investigation chain
- **Jira ticket references** — any ticket IDs mentioned (e.g., EM-162327) should be noted as related work items

---

## Step 6 — Generate Output

### Structured Conclusion Report

Use this exact template for the output:

```markdown
## Swarm Analysis: SS###### — [Account Name]

**Case:** ####### | **Priority:** P# | **Channel:** Channel Name
**Created By:** Name | **First Responder:** Name
**Subject:** Subject text
**Swarm Created:** Date | **Last Activity:** Date
**Status:** Open / Closed / Resolved

---

### The Problem

[2-4 sentence summary of the customer's issue in clear, non-jargon language. Include what the customer expects vs. what is happening.]

---

### Investigation Chain

[Show the cross-team/cross-channel investigation flow]

```
Team/Channel A (SS######)
  → Finding: "[their conclusion]"
  → Escalated to Team/Channel B (SS######)
    → Finding: "[their conclusion]"
    → [Optional: further escalation]
```

---

### Root Cause

[Technical explanation of the root cause. Include the data flow / event pipeline showing where the issue occurs. Be specific about components, event names, and suppression points.]

---

### Per-Team Findings

| Team / Channel | Investigator | Finding |
|----------------|-------------|---------|
| [Team A] | [Name] | [Their specific conclusion] |
| [Team B] | [Name] | [Their specific conclusion] |

---

### Resolution Status

**Classification:** [WAD / Defect / Enhancement Needed / Configuration Issue / Unsupported Scenario]

**Available Options:**
1. [Option 1 — e.g., Close as WAD with documentation]
2. [Option 2 — e.g., Create enhancement epic for PM prioritization]

**Workaround:** [If any exists, describe it. If none, state "No workaround available."]

---

### Open Items

- [ ] [Pending verification or action item 1]
- [ ] [Pending verification or action item 2]

### Related Jira Tickets

- [TICKET-ID] — [Brief description of what it tracks]

---

### Recommended Reply

[Draft a reply that can be posted in the swarm thread to close or advance it. The reply should:
- Summarize the finding concisely
- State the classification (WAD / defect / etc.)
- Recommend specific next steps
- Tag relevant people if known
- Be professional and actionable]
```

---

## Step 7 — Handle Edge Cases

### Swarm Card Not Parseable
If `read_resource` returns null body and no attachments, or the Adaptive Card JSON is malformed:
1. Report what was retrieved
2. Fall back to searching by any available context (case number from URL params, channel name)
3. Ask user for additional context if needed

### No Replies Found
If searches return zero replies beyond the root card:
1. State the swarm appears to have no discussion yet
2. Report the swarm card details
3. Suggest the swarm may need attention / first response

### Related Swarms in Channels Without Access
If `read_resource` returns permission errors for cross-channel messages:
1. Note which channel/message could not be accessed
2. Report findings from what was accessible
3. Suggest the user check the inaccessible channel directly

### Bot Messages vs. Human Messages
CXone WorkBot messages contain Adaptive Cards with swarm lifecycle events (start, status change, close). Human messages contain the actual analysis. Distinguish between:
- **Bot messages:** `from.displayName` contains "WorkBot" — these are swarm lifecycle events
- **Human messages:** All others — these contain the actual investigation discussion
- **NiCE DX-Claude / AI messages:** These may contain detailed technical analysis posted by AI assistants — treat as investigation findings

---

## Disclosure Block

End every analysis with:

```
**Search Details & Limitations**
- Searches executed: [N queries]
- Messages retrieved: [N total, M unique after dedup]
- Channels covered: [list channel names]
- Related swarms found: [N — list SS numbers]
- [Any limitations: pagination caps hit, channels inaccessible, partial results]
```

---

## Quick Reference — Tool Call Patterns

**Fetch swarm root card:**
```
read_resource(uri="teams:///teams/{teamId}/channels/{channelId}/messages/{messageId}")
```

**Search for thread replies (KQL — always prefer this for Teams):**
```
chat_message_search(query="{caseNumber} {accountName} sent:{startDate}..{endDate}", limit=25)
```

**Read a specific reply message:**
```
read_resource(uri="teams:///chats/{chatId}/messages/{messageId}")
```

**Fallback for channel message read:**
```
read_resource(uri="teams:///teams/{teamId}/channels/{channelId}/messages/{messageId}")
```
