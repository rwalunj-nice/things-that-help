# RCA Forum Orchestrator

Automates three workflows for the weekly Monday RCA forum:

- **remind.py** — Posts a Teams reminder card on Monday morning listing tonight's RCA bugs  
- **scan.py** — Daily: screens new bugs for RCA eligibility and labels qualifying ones  
- **review.py** — Daily: reviews RCA content on flagged bugs and posts gap analysis comments  

## Setup

### 1. Install dependencies

```bash
cd rca-bot
pip install -r requirements.txt
```

### 2. Configure environment

Copy `.env.example` to `.env` and fill in all values:

```
JIRA_BASE_URL=https://nice-ce-cxone-prod.atlassian.net
JIRA_USER_EMAIL=your.email@nice.com
JIRA_API_TOKEN=<from https://id.atlassian.com/manage-profile/security/api-tokens>
JIRA_FILTER_RCA_FLAGGED=97314
JIRA_FILTER_SCREENING=101489
JIRA_LABEL_RCA_CANDIDATE=INT_RCA_CANDIDATE
JIRA_RCA_FIELD=customfield_10117
JIRA_FIX_FIELD=customfield_12794
TEAMS_WEBHOOK_URL=<from Teams channel > Connectors > Incoming Webhook>
ANTHROPIC_API_KEY=<from https://console.anthropic.com>
BOT_JIRA_ACCOUNT_ID=<your Jira account ID — visible in your Jira profile URL>
```

### 3. Register scheduled tasks (Windows)

Run `setup.bat` as Administrator to register all three tasks in Windows Task Scheduler:

```
setup.bat
```

Tasks created:
| Task | Trigger | Script |
|------|---------|--------|
| RCA-Reminder | Monday 08:00 | remind.py |
| RCA-Scan | Daily 09:00 | scan.py |
| RCA-Review | Daily 10:00 | review.py |

## Running manually

```bash
# Post today's Teams reminder (any day)
python remind.py

# Screen new bugs (preview only, no label writes)
python scan.py --dry-run

# Review RCA content and post comments
python review.py
```

## Tests

```bash
cd rca-bot
pytest -v
```

## Files

| File | Purpose |
|------|---------|
| `config.py` | Loads credentials from `.env` |
| `models.py` | Bug and Comment dataclasses |
| `state.py` | Tracks last scan timestamp in `state.json` |
| `jira_client.py` | Jira REST API v3 calls |
| `teams_client.py` | Teams incoming webhook |
| `claude_client.py` | Claude API — eligibility judgment + RCA gap analysis |
| `remind.py` | Script 1: Monday reminder |
| `scan.py` | Script 2: Daily eligibility scan |
| `review.py` | Script 3: Daily RCA review |
