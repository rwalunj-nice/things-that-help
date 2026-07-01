# RCA Bot — Claude Routines

Three Remote Routines that automate the weekly INT team RCA (Root Cause Analysis) forum.
Runs on Anthropic's cloud infrastructure — no Python install, no API key, no machine left on.

---

## What Each Routine Does

| Routine | Schedule | Model | What it does |
|---|---|---|---|
| RCA Forum Reminder | Every Monday 08:00 | Claude Haiku 4.5 | Reads Jira filter 97314, outputs a formatted bug list to the run log for manual paste into Teams |
| RCA Bug Scanner | Daily 09:00 | Claude Sonnet 4.6 | Reads Jira filter 101489 (last 3 days), skips ineligible bugs, judges eligibility, labels eligible bugs `INT_RCA_CANDIDATE` |
| RCA Gap Reviewer | Daily 10:00 | Claude Sonnet 4.6 | Reads Jira filter 97314, posts rubric check + 5 Whys gap analysis as a Jira comment on each unreviewed bug |

---

## How It Works

Each Routine runs as a Claude session on Anthropic's cloud, triggered on schedule. It uses:

- **Atlassian connector** — reads and writes Jira (search bugs, add labels, post comments)
- **Run log** (Routine 1) — the reminder outputs the formatted message to the run log; you copy and paste it into the Teams meeting chat each Monday (~20 seconds)

> **Why manual paste for the reminder?** The Microsoft 365 connector in Claude Routines is read-only for Teams (cannot send messages), and NICE tenant policy enforces OAuth on all Power Automate HTTP triggers, blocking anonymous calls from the Routine. Manual paste is zero-infrastructure and takes 20 seconds.

---

## Prerequisites

Before creating the Routines, confirm the following are in place:

- **Claude Code Enterprise** account with Routines enabled
  - Verify by navigating to [claude.ai/code/routines](https://claude.ai/code/routines) — if you can see this page, you're good
- **Atlassian connector** connected in Claude Code
  - Go to [claude.ai/settings → Connectors](https://claude.ai/settings) → confirm Atlassian is listed and authorised
- **Microsoft 365 account** with access to the RCA Forum recurring meeting chat (needed to build the Power Automate flow)

---

## One-Time Setup

### Create the 3 Routines

Go to [claude.ai/code/routines](https://claude.ai/code/routines) and click **+ New Routine** for each.

---

#### Routine 1 — RCA Forum Reminder

| Field | Value |
|---|---|
| Name | `RCA Bot - RCA Forum Reminder` |
| Type | Remote |
| Model | Claude Haiku 4.5 |
| Trigger | Weekly → Monday → 08:00 AM (your local timezone) |
| Repository | `things-that-help` |
| Connectors | Atlassian |
| Environment | None |

**Instructions:** copy the full prompt from [`routines/reminder.md`](routines/reminder.md) and paste into the Instructions field.

---

#### Routine 2 — RCA Bug Scanner

| Field | Value |
|---|---|
| Name | `RCA Bot - RCA Bug Scanner` |
| Type | Remote |
| Model | Claude Sonnet 4.6 |
| Trigger | Daily → 09:00 AM (your local timezone) |
| Repository | `things-that-help` |
| Connectors | Atlassian |
| Environment | None |

**Instructions:** copy the full prompt from [`routines/scanner.md`](routines/scanner.md) and paste into the Instructions field.

> The scanner looks back 3 days and skips bugs that already have labels `CLONE`, `CICD_FAIL_BUG`, or `INT_RCA_CANDIDATE`, or have resolution `Duplicate`.

---

#### Routine 3 — RCA Gap Reviewer

| Field | Value |
|---|---|
| Name | `RCA Bot - RCA Gap Reviewer` |
| Type | Remote |
| Model | Claude Sonnet 4.6 |
| Trigger | Daily → 10:00 AM (your local timezone) |
| Repository | `things-that-help` |
| Connectors | Atlassian |
| Environment | None |

**Instructions:** copy the full prompt from [`routines/reviewer.md`](routines/reviewer.md) and paste into the Instructions field.

> The reviewer is idempotent — it skips any bug that already has a comment starting with `🤖 RCA Bot Review`, so running it multiple times is safe.

---

## Verify Before Relying on the Schedule

After creating each Routine, click **Run now** and confirm:

1. **Reminder** → the run log shows the formatted bug list between `---COPY THIS MESSAGE INTO TEAMS CHAT---` markers. Open the run at [claude.ai/code/routines](https://claude.ai/code/routines), copy that block, and paste it into the Teams meeting chat.
2. **Scanner** → the run log shows skip decisions (with reasons) and eligibility judgments for bugs from filter 101489
3. **Reviewer** → a `🤖 RCA Bot Review` comment appears on a known bug in filter 97314 (e.g. INT-56504) with rubric gaps and 5 Whys analysis
4. **Idempotency check** → click "Run now" on the Reviewer a second time — it should report 0 bugs processed (all already reviewed)

Check run history and logs at [claude.ai/code/routines](https://claude.ai/code/routines) after each run.

---

## File Structure

```
rca-bot-routine/
├── CLAUDE.md             ← Context Claude reads at run time: filter IDs, field names, skip labels
├── routines/
│   ├── reminder.md       ← Routine 1 — prompt + config (model, connectors, trigger)
│   ├── scanner.md        ← Routine 2 — prompt + config
│   └── reviewer.md       ← Routine 3 — prompt + config
├── .env.example          ← Documents the TEAMS_FLOW_URL variable
└── README.md             ← This file
```

---

## When the Meeting Series Changes

If the recurring RCA meeting is recreated, you only need to update **the Power Automate flow** — re-open it in [make.powerautomate.com](https://make.powerautomate.com), edit the "Post message" step, and select the new meeting chat from the dropdown. The `TEAMS_FLOW_URL` and the Routine itself do not change.

---

## Manual Fallback

The original Python scripts in [`../rca-bot/`](../rca-bot/) remain available for ad-hoc runs and debugging individual bugs. They require a Jira API token and `ANTHROPIC_API_KEY` — see that folder's README for setup. They are not used by these Routines.
