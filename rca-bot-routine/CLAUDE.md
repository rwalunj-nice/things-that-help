# RCA Bot — Routine Context

This folder contains the prompts for the three Claude Routines that automate the weekly RCA (Root Cause Analysis) forum for the INT team.

## Jira Configuration

| Setting | Value |
|---|---|
| Jira instance | `nice-ce-cxone-prod.atlassian.net` |
| Filter — RCA flagged bugs (Reminder + Reviewer) | `97314` |
| Filter — Screening pending bugs (Scanner) | `101489` |
| RCA content field | `customfield_10117` |
| Fix description field | `customfield_12794` |
| Label to apply when eligible | `INT_RCA_CANDIDATE` |

## Skip Labels (Scanner)

| Label | Reason |
|---|---|
| `CLONE` | Cloned bugs don't need independent RCA |
| `CICD_FAIL_BUG` | Nightly/CI failures are not RCA-worthy |
| `INT_RCA_CANDIDATE` | Already processed — don't relabel |

## Idempotency Marker (Reviewer)

The Reviewer checks whether a bug already has a comment starting with `🤖 RCA Bot Review` before posting. This prevents duplicate reviews across daily runs.
