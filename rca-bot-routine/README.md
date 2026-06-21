# RCA Bot — Claude Routines

Three Remote Routines that automate the weekly INT team RCA (Root Cause Analysis) forum. Runs on Anthropic's cloud — no Python install, no API key, no machine staying on.

## What Each Routine Does

| Routine | Schedule | What it does |
|---|---|---|
| RCA Forum Reminder | Monday 08:00 | Reads Jira filter 97314, posts Teams card listing tonight's bugs and owners |
| RCA Bug Scanner | Daily 09:00 | Reads Jira filter 101489 (last 3 days), skips CLONE/CICD/Duplicate/already-labeled bugs, judges eligibility, adds `INT_RCA_CANDIDATE` label |
| RCA Gap Reviewer | Daily 10:00 | Reads Jira filter 97314, posts rubric check + 5 Whys analysis as a Jira comment on each unreviewed bug |

No `ANTHROPIC_API_KEY` needed — Claude handles AI reasoning natively via your Enterprise credentials.

## Prerequisites

- Claude Code Enterprise account with Routines enabled
- Atlassian MCP connector connected in Claude Code (for Jira access)
- Teams incoming webhook URL for your channel

## One-Time Setup

### Step 1 — Create a custom Routine environment

Go to [claude.ai/settings → Environments](https://claude.ai/settings) → **New environment**:
- Name: `RCA Bot`
- Add secret: `TEAMS_WEBHOOK_URL` = your Teams incoming webhook URL

This is only needed for Routine 1. Routines 2 and 3 use no secrets.

### Step 2 — Create the three Routines

Go to [claude.ai/code/routines](https://claude.ai/code/routines) → **+ New Routine** for each:

**Routine 1 — RCA Forum Reminder**
- Type: Remote
- Trigger: Scheduled → Weekly → Monday → 08:00
- Repository: `things-that-help`
- Connector: Atlassian
- Environment: `RCA Bot`
- Prompt: copy from [`routines/reminder.md`](routines/reminder.md)

**Routine 2 — RCA Bug Scanner**
- Type: Remote
- Trigger: Scheduled → Daily → 09:00
- Repository: `things-that-help`
- Connector: Atlassian
- Prompt: copy from [`routines/scanner.md`](routines/scanner.md)

**Routine 3 — RCA Gap Reviewer**
- Type: Remote
- Trigger: Scheduled → Daily → 10:00
- Repository: `things-that-help`
- Connector: Atlassian
- Prompt: copy from [`routines/reviewer.md`](routines/reviewer.md)

## Verification

After creating each Routine, click **Run now** before relying on the schedule:

1. **Reminder**: Teams card should appear in the channel with bugs from filter 97314
2. **Scanner**: Run log should show skip decisions (CLONE/CICD/Duplicate/already-labeled) and eligibility judgments
3. **Reviewer**: A `🤖 RCA Bot Review` comment should appear on a known bug (e.g. INT-56504)
4. **Idempotency**: Run Reviewer again — it should process 0 bugs (all already reviewed)

## File Structure

```
rca-bot-routine/
├── CLAUDE.md             ← Context Claude reads at run time (filter IDs, field names, skip labels)
├── routines/
│   ├── reminder.md       ← Routine 1 prompt
│   ├── scanner.md        ← Routine 2 prompt
│   └── reviewer.md       ← Routine 3 prompt
├── .env.example          ← Required environment variables
└── README.md             ← This file
```

## Manual / Fallback

The original Python scripts in [`../rca-bot/`](../rca-bot/) still work for ad-hoc runs and debugging. They require a Jira API token and ANTHROPIC_API_KEY (see that folder's README).
