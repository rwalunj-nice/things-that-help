# RCA Forum Orchestrator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build three Python scripts that automate a weekly RCA forum — Monday morning Teams reminders, daily Jira bug eligibility screening via Claude Haiku, and AI-powered RCA gap + 5 Whys analysis posted as Jira comments via Claude Sonnet.

**Architecture:** Four shared library modules (`models`, `config`, `jira_client`, `teams_client`, `claude_client`) with single responsibilities. Three thin orchestrator scripts (`remind.py`, `scan.py`, `review.py`) compose those modules. All AI prompts live in `claude_client.py`. All Jira I/O lives in `jira_client.py`. Scripts are independently schedulable via Windows Task Scheduler.

**Tech Stack:** Python 3.11+, `anthropic` SDK, `requests`, `python-dotenv`, `pytest`, `pytest-mock`

---

## File Map

| File | Role |
|---|---|
| `rca-bot/models.py` | `Bug` and `Comment` dataclasses shared across all modules |
| `rca-bot/config.py` | `Config` dataclass loaded from `.env` |
| `rca-bot/state.py` | Read/write `state.json` for `last_scan_at` timestamp |
| `rca-bot/jira_client.py` | `JiraClient` — all Jira REST API v3 calls |
| `rca-bot/teams_client.py` | `TeamsClient` — Teams incoming webhook POST |
| `rca-bot/claude_client.py` | `ClaudeClient` — both Claude API prompt functions |
| `rca-bot/remind.py` | Script 1: Monday 08:00 reminder |
| `rca-bot/scan.py` | Script 2: Daily 09:00 eligibility scan |
| `rca-bot/review.py` | Script 3: Daily 10:00 RCA gap analysis |
| `rca-bot/tests/` | pytest test files mirroring the module structure |
| `rca-bot/.env.example` | Credential template (committed) |
| `rca-bot/requirements.txt` | Python dependencies |
| `rca-bot/README.md` | Setup + Task Scheduler instructions |

---

## Task 1: Project Scaffold

**Files:**
- Create: `rca-bot/requirements.txt`
- Create: `rca-bot/.env.example`
- Create: `rca-bot/.gitignore`

- [ ] **Step 1: Create `rca-bot/requirements.txt`**

```
anthropic>=0.40.0
requests>=2.31.0
python-dotenv>=1.0.0
pytest>=8.0.0
pytest-mock>=3.12.0
```

- [ ] **Step 2: Create `rca-bot/.env.example`**

```
JIRA_BASE_URL=https://nice-ce-cxone-prod.atlassian.net
JIRA_USER_EMAIL=your.email@nice.com
JIRA_API_TOKEN=your_jira_api_token_here
JIRA_FILTER_RCA_FLAGGED=97314
JIRA_FILTER_SCREENING=101489
JIRA_LABEL_RCA_CANDIDATE=INT_RCA_CANDIDATE
JIRA_RCA_FIELD=customfield_10117
JIRA_FIX_FIELD=customfield_12794
TEAMS_WEBHOOK_URL=https://your-org.webhook.office.com/webhookb2/...
ANTHROPIC_API_KEY=sk-ant-...
BOT_JIRA_ACCOUNT_ID=your_bot_account_id_here
```

To get `BOT_JIRA_ACCOUNT_ID`: call `GET https://nice-ce-cxone-prod.atlassian.net/rest/api/3/myself` with your credentials — the `accountId` field is what you need.

- [ ] **Step 3: Create `rca-bot/.gitignore`**

```
.env
state.json
*.log
__pycache__/
.pytest_cache/
*.pyc
```

- [ ] **Step 4: Install dependencies**

```bash
cd rca-bot
pip install -r requirements.txt
```

Expected: packages install without errors.

- [ ] **Step 5: Commit**

```bash
git add rca-bot/requirements.txt rca-bot/.env.example rca-bot/.gitignore
git commit -m "feat(rca-bot): project scaffold"
```

---

## Task 2: Data Models

**Files:**
- Create: `rca-bot/models.py`
- Create: `rca-bot/tests/__init__.py`
- Create: `rca-bot/tests/test_models.py`

- [ ] **Step 1: Write the failing test**

Create `rca-bot/tests/__init__.py` (empty file), then create `rca-bot/tests/test_models.py`:

```python
from models import Bug, Comment

def test_bug_defaults_rca_fields_to_empty():
    bug = Bug(
        key="INT-001",
        summary="Test bug",
        description="A description",
        priority="P1",
        labels=["SOME_LABEL"],
        assignee_name="Alice",
        assignee_account_id="acc123",
        resolution=None,
    )
    assert bug.rca_text == ""
    assert bug.fix_text == ""

def test_bug_stores_all_fields():
    bug = Bug(
        key="INT-002",
        summary="Another bug",
        description="Desc",
        priority="P2",
        labels=["CLONE"],
        assignee_name="Bob",
        assignee_account_id="acc456",
        resolution="Duplicate",
        rca_text="What happened: ...",
        fix_text="We fixed it by ...",
    )
    assert bug.key == "INT-002"
    assert bug.resolution == "Duplicate"
    assert "CLONE" in bug.labels

def test_comment_stores_fields():
    c = Comment(id="c1", author_account_id="acc123", body="A comment")
    assert c.id == "c1"
    assert c.author_account_id == "acc123"
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd rca-bot
pytest tests/test_models.py -v
```

Expected: `ModuleNotFoundError: No module named 'models'`

- [ ] **Step 3: Create `rca-bot/models.py`**

```python
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Bug:
    key: str
    summary: str
    description: str
    priority: str
    labels: list[str]
    assignee_name: str
    assignee_account_id: str
    resolution: Optional[str]
    rca_text: str = ""
    fix_text: str = ""


@dataclass
class Comment:
    id: str
    author_account_id: str
    body: str
```

- [ ] **Step 4: Run test to verify it passes**

```bash
pytest tests/test_models.py -v
```

Expected: 3 tests pass.

- [ ] **Step 5: Commit**

```bash
git add rca-bot/models.py rca-bot/tests/__init__.py rca-bot/tests/test_models.py
git commit -m "feat(rca-bot): add Bug and Comment dataclasses"
```

---

## Task 3: Config + State

**Files:**
- Create: `rca-bot/config.py`
- Create: `rca-bot/state.py`
- Create: `rca-bot/tests/test_config.py`
- Create: `rca-bot/tests/test_state.py`

- [ ] **Step 1: Write failing tests**

Create `rca-bot/tests/test_config.py`:

```python
import os
import pytest
from config import load_config


def test_load_config_reads_env(monkeypatch):
    monkeypatch.setenv("JIRA_BASE_URL", "https://example.atlassian.net")
    monkeypatch.setenv("JIRA_USER_EMAIL", "bot@example.com")
    monkeypatch.setenv("JIRA_API_TOKEN", "token123")
    monkeypatch.setenv("TEAMS_WEBHOOK_URL", "https://webhook.example.com")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test")
    monkeypatch.setenv("BOT_JIRA_ACCOUNT_ID", "bot-acc-id")

    config = load_config()

    assert config.jira_base_url == "https://example.atlassian.net"
    assert config.jira_filter_rca_flagged == "97314"
    assert config.jira_filter_screening == "101489"
    assert config.jira_label_rca_candidate == "INT_RCA_CANDIDATE"


def test_load_config_raises_on_missing_required(monkeypatch):
    monkeypatch.delenv("JIRA_BASE_URL", raising=False)
    with pytest.raises(KeyError):
        load_config()
```

Create `rca-bot/tests/test_state.py`:

```python
import json
from datetime import datetime, timezone
from pathlib import Path
import pytest
from state import load_last_scan_at, save_last_scan_at


def test_load_returns_24h_ago_when_no_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    result = load_last_scan_at()
    now = datetime.now(timezone.utc)
    diff = (now - result).total_seconds()
    assert 86300 < diff < 86500  # ~24 hours


def test_save_and_load_roundtrip(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    dt = datetime(2026, 6, 20, 9, 0, 0, tzinfo=timezone.utc)
    save_last_scan_at(dt)
    loaded = load_last_scan_at()
    assert loaded == dt
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_config.py tests/test_state.py -v
```

Expected: `ModuleNotFoundError` for `config` and `state`.

- [ ] **Step 3: Create `rca-bot/config.py`**

```python
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    jira_base_url: str
    jira_user_email: str
    jira_api_token: str
    jira_filter_rca_flagged: str
    jira_filter_screening: str
    jira_label_rca_candidate: str
    jira_rca_field: str
    jira_fix_field: str
    teams_webhook_url: str
    anthropic_api_key: str
    bot_jira_account_id: str


def load_config() -> Config:
    return Config(
        jira_base_url=os.environ["JIRA_BASE_URL"],
        jira_user_email=os.environ["JIRA_USER_EMAIL"],
        jira_api_token=os.environ["JIRA_API_TOKEN"],
        jira_filter_rca_flagged=os.environ.get("JIRA_FILTER_RCA_FLAGGED", "97314"),
        jira_filter_screening=os.environ.get("JIRA_FILTER_SCREENING", "101489"),
        jira_label_rca_candidate=os.environ.get("JIRA_LABEL_RCA_CANDIDATE", "INT_RCA_CANDIDATE"),
        jira_rca_field=os.environ.get("JIRA_RCA_FIELD", "customfield_10117"),
        jira_fix_field=os.environ.get("JIRA_FIX_FIELD", "customfield_12794"),
        teams_webhook_url=os.environ["TEAMS_WEBHOOK_URL"],
        anthropic_api_key=os.environ["ANTHROPIC_API_KEY"],
        bot_jira_account_id=os.environ["BOT_JIRA_ACCOUNT_ID"],
    )
```

- [ ] **Step 4: Create `rca-bot/state.py`**

```python
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

_STATE_FILE = Path(__file__).parent / "state.json"


def load_last_scan_at() -> datetime:
    if not _STATE_FILE.exists():
        return datetime.now(timezone.utc) - timedelta(hours=24)
    data = json.loads(_STATE_FILE.read_text())
    return datetime.fromisoformat(data["last_scan_at"])


def save_last_scan_at(dt: datetime) -> None:
    data = {}
    if _STATE_FILE.exists():
        data = json.loads(_STATE_FILE.read_text())
    data["last_scan_at"] = dt.isoformat()
    _STATE_FILE.write_text(json.dumps(data, indent=2))
```

- [ ] **Step 5: Run tests to verify they pass**

```bash
pytest tests/test_config.py tests/test_state.py -v
```

Expected: 4 tests pass.

- [ ] **Step 6: Commit**

```bash
git add rca-bot/config.py rca-bot/state.py rca-bot/tests/test_config.py rca-bot/tests/test_state.py
git commit -m "feat(rca-bot): config and state modules"
```

---

## Task 4: Jira Client

**Files:**
- Create: `rca-bot/jira_client.py`
- Create: `rca-bot/tests/test_jira_client.py`

- [ ] **Step 1: Write failing tests**

Create `rca-bot/tests/test_jira_client.py`:

```python
from unittest.mock import patch, MagicMock
from datetime import datetime, timezone
import pytest
from config import Config
from jira_client import JiraClient

MOCK_CONFIG = Config(
    jira_base_url="https://example.atlassian.net",
    jira_user_email="bot@example.com",
    jira_api_token="token",
    jira_filter_rca_flagged="97314",
    jira_filter_screening="101489",
    jira_label_rca_candidate="INT_RCA_CANDIDATE",
    jira_rca_field="customfield_10117",
    jira_fix_field="customfield_12794",
    teams_webhook_url="https://webhook.example.com",
    anthropic_api_key="sk-ant-test",
    bot_jira_account_id="bot-acc-123",
)

MOCK_ISSUE = {
    "key": "INT-001",
    "fields": {
        "summary": "Service outage due to DB lock",
        "description": {"type": "doc", "version": 1, "content": [
            {"type": "paragraph", "content": [{"type": "text", "text": "Service failed."}]}
        ]},
        "priority": {"name": "P1"},
        "labels": ["INT_CFB"],
        "assignee": {"displayName": "Alice", "accountId": "acc-alice"},
        "resolution": None,
        "customfield_10117": {"type": "doc", "version": 1, "content": [
            {"type": "bulletList", "content": [
                {"type": "listItem", "content": [
                    {"type": "paragraph", "content": [{"type": "text", "text": "What happened? - DB lock"}]}
                ]}
            ]}
        ]},
        "customfield_12794": None,
    }
}


def test_get_filter_bugs_returns_bug_list():
    client = JiraClient(MOCK_CONFIG)
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"issues": [MOCK_ISSUE]}
    mock_resp.raise_for_status = MagicMock()

    with patch("jira_client.requests.get", return_value=mock_resp) as mock_get:
        bugs = client.get_filter_bugs("97314")

    assert len(bugs) == 1
    assert bugs[0].key == "INT-001"
    assert bugs[0].priority == "P1"
    assert bugs[0].rca_text == "What happened? - DB lock"
    assert "INT_CFB" in bugs[0].labels
    params = mock_get.call_args.kwargs["params"]
    assert "filter=97314" in params["jql"]


def test_get_bugs_since_includes_date_in_jql():
    client = JiraClient(MOCK_CONFIG)
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"issues": []}
    mock_resp.raise_for_status = MagicMock()
    since = datetime(2026, 6, 20, 9, 0, tzinfo=timezone.utc)

    with patch("jira_client.requests.get", return_value=mock_resp) as mock_get:
        client.get_bugs_since("101489", since)

    params = mock_get.call_args.kwargs["params"]
    assert "2026-06-20" in params["jql"]


def test_add_label_sends_correct_body():
    client = JiraClient(MOCK_CONFIG)
    mock_resp = MagicMock()
    mock_resp.raise_for_status = MagicMock()

    with patch("jira_client.requests.put", return_value=mock_resp) as mock_put:
        client.add_label("INT-001", "INT_RCA_CANDIDATE")

    body = mock_put.call_args.kwargs["json"]
    assert {"add": "INT_RCA_CANDIDATE"} in body["update"]["labels"]


def test_post_comment_sends_adf_body():
    client = JiraClient(MOCK_CONFIG)
    mock_resp = MagicMock()
    mock_resp.raise_for_status = MagicMock()

    with patch("jira_client.requests.post", return_value=mock_resp) as mock_post:
        client.post_comment("INT-001", "Some **markdown** text")

    body = mock_post.call_args.kwargs["json"]
    assert body["body"]["type"] == "doc"


def test_has_bot_comment_returns_true_when_found():
    client = JiraClient(MOCK_CONFIG)
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"comments": [
        {"id": "c1", "author": {"accountId": "bot-acc-123"}, "body": {"type": "doc", "version": 1, "content": []}}
    ]}
    mock_resp.raise_for_status = MagicMock()

    with patch("jira_client.requests.get", return_value=mock_resp):
        result = client.has_bot_comment("INT-001")

    assert result is True


def test_has_bot_comment_returns_false_when_not_found():
    client = JiraClient(MOCK_CONFIG)
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"comments": [
        {"id": "c1", "author": {"accountId": "other-acc"}, "body": {"type": "doc", "version": 1, "content": []}}
    ]}
    mock_resp.raise_for_status = MagicMock()

    with patch("jira_client.requests.get", return_value=mock_resp):
        result = client.has_bot_comment("INT-001")

    assert result is False


def test_bug_with_no_priority_defaults_to_unset():
    client = JiraClient(MOCK_CONFIG)
    issue = {**MOCK_ISSUE, "fields": {**MOCK_ISSUE["fields"], "priority": None}}
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"issues": [issue]}
    mock_resp.raise_for_status = MagicMock()

    with patch("jira_client.requests.get", return_value=mock_resp):
        bugs = client.get_filter_bugs("97314")

    assert bugs[0].priority == "Unset"
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_jira_client.py -v
```

Expected: `ModuleNotFoundError: No module named 'jira_client'`

- [ ] **Step 3: Create `rca-bot/jira_client.py`**

```python
import requests
from datetime import datetime
from config import Config
from models import Bug, Comment


def _extract_adf_text(adf: dict) -> str:
    if not adf or not isinstance(adf, dict):
        return ""
    texts = []

    def walk(node):
        if isinstance(node, dict):
            if node.get("type") == "text":
                texts.append(node.get("text", ""))
            for child in node.get("content", []):
                walk(child)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(adf)
    return "\n".join(t for t in texts if t.strip())


def _issue_to_bug(issue: dict, rca_field: str, fix_field: str) -> Bug:
    fields = issue["fields"]
    priority_obj = fields.get("priority")
    priority = priority_obj["name"] if priority_obj else "Unset"
    assignee = fields.get("assignee") or {}
    resolution_obj = fields.get("resolution")
    return Bug(
        key=issue["key"],
        summary=fields.get("summary", ""),
        description=_extract_adf_text(fields.get("description")),
        priority=priority,
        labels=fields.get("labels", []),
        assignee_name=assignee.get("displayName", "Unknown"),
        assignee_account_id=assignee.get("accountId", ""),
        resolution=resolution_obj["name"] if resolution_obj else None,
        rca_text=_extract_adf_text(fields.get(rca_field)),
        fix_text=_extract_adf_text(fields.get(fix_field)),
    )


def _markdown_to_adf(text: str) -> dict:
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [{"type": "text", "text": text}],
            }
        ],
    }


class JiraClient:
    def __init__(self, config: Config):
        self._base = config.jira_base_url
        self._auth = (config.jira_user_email, config.jira_api_token)
        self._rca_field = config.jira_rca_field
        self._fix_field = config.jira_fix_field
        self._bot_account_id = config.bot_jira_account_id
        self._fields = (
            f"summary,description,priority,labels,assignee,resolution,"
            f"{config.jira_rca_field},{config.jira_fix_field}"
        )

    def _search(self, jql: str) -> list[dict]:
        resp = requests.get(
            f"{self._base}/rest/api/3/search",
            params={"jql": jql, "fields": self._fields, "maxResults": 100},
            auth=self._auth,
        )
        resp.raise_for_status()
        return resp.json()["issues"]

    def get_filter_bugs(self, filter_id: str) -> list[Bug]:
        issues = self._search(f"filter={filter_id}")
        return [_issue_to_bug(i, self._rca_field, self._fix_field) for i in issues]

    def get_bugs_since(self, filter_id: str, since: datetime) -> list[Bug]:
        since_str = since.strftime("%Y-%m-%d %H:%M")
        issues = self._search(f'filter={filter_id} AND created >= "{since_str}"')
        return [_issue_to_bug(i, self._rca_field, self._fix_field) for i in issues]

    def add_label(self, issue_key: str, label: str) -> None:
        resp = requests.put(
            f"{self._base}/rest/api/3/issue/{issue_key}",
            json={"update": {"labels": [{"add": label}]}},
            auth=self._auth,
        )
        resp.raise_for_status()

    def post_comment(self, issue_key: str, markdown_body: str) -> None:
        resp = requests.post(
            f"{self._base}/rest/api/3/issue/{issue_key}/comment",
            json={"body": _markdown_to_adf(markdown_body)},
            auth=self._auth,
        )
        resp.raise_for_status()

    def has_bot_comment(self, issue_key: str) -> bool:
        resp = requests.get(
            f"{self._base}/rest/api/3/issue/{issue_key}/comment",
            auth=self._auth,
        )
        resp.raise_for_status()
        comments = resp.json()["comments"]
        return any(
            c["author"]["accountId"] == self._bot_account_id for c in comments
        )
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_jira_client.py -v
```

Expected: 6 tests pass.

- [ ] **Step 5: Commit**

```bash
git add rca-bot/jira_client.py rca-bot/tests/test_jira_client.py
git commit -m "feat(rca-bot): Jira client with ADF parsing"
```

---

## Task 5: Teams Client

**Files:**
- Create: `rca-bot/teams_client.py`
- Create: `rca-bot/tests/test_teams_client.py`

- [ ] **Step 1: Write failing tests**

Create `rca-bot/tests/test_teams_client.py`:

```python
from unittest.mock import patch, MagicMock
from models import Bug
from teams_client import TeamsClient


def _make_bug(key, summary, assignee):
    return Bug(
        key=key, summary=summary, description="", priority="P1",
        labels=[], assignee_name=assignee, assignee_account_id="acc",
        resolution=None,
    )


def test_post_reminder_calls_webhook():
    client = TeamsClient("https://webhook.example.com")
    bugs = [_make_bug("INT-001", "DB outage", "Alice")]
    mock_resp = MagicMock()
    mock_resp.raise_for_status = MagicMock()

    with patch("teams_client.requests.post", return_value=mock_resp) as mock_post:
        client.post_reminder(bugs)

    mock_post.assert_called_once()
    url = mock_post.call_args.args[0]
    assert url == "https://webhook.example.com"


def test_post_reminder_includes_all_bug_keys():
    client = TeamsClient("https://webhook.example.com")
    bugs = [
        _make_bug("INT-001", "Bug one", "Alice"),
        _make_bug("INT-002", "Bug two", "Bob"),
    ]
    mock_resp = MagicMock()
    mock_resp.raise_for_status = MagicMock()

    with patch("teams_client.requests.post", return_value=mock_resp) as mock_post:
        client.post_reminder(bugs)

    body = mock_post.call_args.kwargs["json"]
    text = body["text"]
    assert "INT-001" in text
    assert "INT-002" in text
    assert "Alice" in text
    assert "Bob" in text


def test_post_reminder_with_empty_list_still_posts():
    client = TeamsClient("https://webhook.example.com")
    mock_resp = MagicMock()
    mock_resp.raise_for_status = MagicMock()

    with patch("teams_client.requests.post", return_value=mock_resp) as mock_post:
        client.post_reminder([])

    mock_post.assert_called_once()
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_teams_client.py -v
```

Expected: `ModuleNotFoundError: No module named 'teams_client'`

- [ ] **Step 3: Create `rca-bot/teams_client.py`**

```python
import requests
from models import Bug


class TeamsClient:
    def __init__(self, webhook_url: str):
        self._webhook_url = webhook_url

    def post_reminder(self, bugs: list[Bug]) -> None:
        if bugs:
            lines = ["**RCA Forum tonight — bugs to present:**\n"]
            for bug in bugs:
                lines.append(f"• **[{bug.key}]** {bug.summary} — _{bug.assignee_name}_")
        else:
            lines = ["**RCA Forum tonight** — no bugs currently flagged for review."]

        payload = {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "summary": "RCA Forum Reminder",
            "themeColor": "0076D7",
            "text": "\n".join(lines),
        }
        resp = requests.post(self._webhook_url, json=payload, timeout=10)
        resp.raise_for_status()
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_teams_client.py -v
```

Expected: 3 tests pass.

- [ ] **Step 5: Commit**

```bash
git add rca-bot/teams_client.py rca-bot/tests/test_teams_client.py
git commit -m "feat(rca-bot): Teams webhook client"
```

---

## Task 6: Claude Client

**Files:**
- Create: `rca-bot/claude_client.py`
- Create: `rca-bot/tests/test_claude_client.py`

- [ ] **Step 1: Write failing tests**

Create `rca-bot/tests/test_claude_client.py`:

```python
import json
from unittest.mock import patch, MagicMock
from claude_client import ClaudeClient


def _mock_claude_response(text: str):
    mock_msg = MagicMock()
    mock_msg.content = [MagicMock(text=text)]
    return mock_msg


def test_judge_eligibility_returns_eligible_true():
    client = ClaudeClient("sk-ant-test")
    response_json = json.dumps({"eligible": True, "reason": "Service outage", "confidence": "high"})

    with patch.object(client._client.messages, "create", return_value=_mock_claude_response(response_json)):
        result = client.judge_rca_eligibility(
            summary="DB sync failed causing outage",
            description="Multiple services went down",
            priority="P1",
            labels=["INT_CFB"],
        )

    assert result["eligible"] is True
    assert result["confidence"] == "high"


def test_judge_eligibility_returns_eligible_false():
    client = ClaudeClient("sk-ant-test")
    response_json = json.dumps({"eligible": False, "reason": "Trivial typo fix", "confidence": "high"})

    with patch.object(client._client.messages, "create", return_value=_mock_claude_response(response_json)):
        result = client.judge_rca_eligibility(
            summary="Fix typo in error message",
            description="Changed 'occured' to 'occurred'",
            priority="P3",
            labels=[],
        )

    assert result["eligible"] is False


def test_analyze_rca_gaps_returns_structured_output():
    client = ClaudeClient("sk-ant-test")
    response_json = json.dumps({
        "rubric_gaps": ["'How was it missed?' is too generic"],
        "five_whys_chain": [
            {"why": "DB left in partial state", "covered": True, "note": ""},
            {"why": "DDL broke transaction", "covered": True, "note": ""},
            {"why": "No DB review checklist", "covered": False, "note": "Not addressed"},
        ],
        "deepest_unanswered_why": "No MySQL DDL standards exist in review process",
        "comment_markdown": "🤖 RCA Bot Review\n\nRUBRIC GAPS:\n..."
    })

    with patch.object(client._client.messages, "create", return_value=_mock_claude_response(response_json)):
        result = client.analyze_rca_gaps(
            rca_text="What happened: DB sync failed...",
            fix_text="Changed DDL to use SET FOREIGN_KEY_CHECKS...",
            bug_summary="WFM Config: Make Sync Atomic Again",
            bug_description="Sync process lost transactional atomicity",
        )

    assert len(result["rubric_gaps"]) == 1
    assert len(result["five_whys_chain"]) == 3
    assert result["five_whys_chain"][2]["covered"] is False
    assert "comment_markdown" in result


def test_analyze_rca_uses_sonnet_model():
    client = ClaudeClient("sk-ant-test")
    response_json = json.dumps({
        "rubric_gaps": [], "five_whys_chain": [],
        "deepest_unanswered_why": "", "comment_markdown": "ok"
    })

    with patch.object(client._client.messages, "create", return_value=_mock_claude_response(response_json)) as mock_create:
        client.analyze_rca_gaps("rca", "fix", "summary", "desc")

    call_kwargs = mock_create.call_args.kwargs
    assert call_kwargs["model"] == "claude-sonnet-4-6"


def test_judge_eligibility_uses_haiku_model():
    client = ClaudeClient("sk-ant-test")
    response_json = json.dumps({"eligible": True, "reason": "test", "confidence": "high"})

    with patch.object(client._client.messages, "create", return_value=_mock_claude_response(response_json)) as mock_create:
        client.judge_rca_eligibility("summary", "desc", "P1", [])

    call_kwargs = mock_create.call_args.kwargs
    assert call_kwargs["model"] == "claude-haiku-4-5-20251001"
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_claude_client.py -v
```

Expected: `ModuleNotFoundError: No module named 'claude_client'`

- [ ] **Step 3: Create `rca-bot/claude_client.py`**

```python
import json
import anthropic


class ClaudeClient:
    def __init__(self, api_key: str):
        self._client = anthropic.Anthropic(api_key=api_key)

    def judge_rca_eligibility(
        self, summary: str, description: str, priority: str, labels: list[str]
    ) -> dict:
        prompt = f"""You are screening engineering bugs to determine if they warrant a Root Cause Analysis.

Flag as RCA-eligible if the bug shows evidence of any of:
- Non-obvious root cause (not a trivial config error or typo)
- Cascading or system-wide failure (multiple services/components affected)
- Required significant investigation or manual intervention to resolve
- Could recur without a design or process change
- Data loss, corruption, or integrity risk
- Customer-visible functional failure

Priority scope: P1, P2, P3, and unset priority all qualify.
Do NOT flag if: root cause was immediately obvious and the fix was trivial.

Respond with JSON only: {{"eligible": true/false, "reason": "...", "confidence": "high/medium/low"}}

Bug summary: {summary}
Priority: {priority}
Labels: {labels}
Description: {description}"""

        message = self._client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=256,
            messages=[{"role": "user", "content": prompt}],
        )
        return json.loads(message.content[0].text.strip())

    def analyze_rca_gaps(
        self, rca_text: str, fix_text: str, bug_summary: str, bug_description: str
    ) -> dict:
        prompt = f"""You are an expert engineering coach reviewing a Root Cause Analysis.

Perform two analyses and return JSON:

1. RUBRIC CHECK — evaluate whether each section is present and substantive:
   - "What happened?": describes the observable failure (not just "bug occurred")
   - "How did it happen?": technical root cause, not just symptoms
   - "How was it missed?": specific process/knowledge gap named (not generic "missed in review")
   - "How was it fixed?": code-level or config-level fix described
   - "Prevention": concrete action items (not generic "add tests" or "be more careful")

2. FIVE WHYS — independently construct the causal chain from the bug details, then map each "why" against the RCA content. Flag where the chain was cut short.

Return JSON only (no extra text):
{{
  "rubric_gaps": ["list of specific gap descriptions, empty if none"],
  "five_whys_chain": [
    {{"why": "why description", "covered": true/false, "note": "brief note if partially covered or missing"}}
  ],
  "deepest_unanswered_why": "the root cause the RCA did not reach, or empty string if fully covered",
  "comment_markdown": "the full Jira comment to post, formatted with sections RUBRIC GAPS and 5 WHYS ANALYSIS and a SUGGESTED ADDITION if deepest_unanswered_why is non-empty. Use ✅/⚠️/❌ markers. End with a horizontal rule and: _Generated by rca-bot. Review and refine before tonight's forum._"
}}

Bug summary: {bug_summary}
Bug description: {bug_description}

RCA content:
{rca_text}

Fix description:
{fix_text}"""

        message = self._client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}],
        )
        return json.loads(message.content[0].text.strip())
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_claude_client.py -v
```

Expected: 5 tests pass.

- [ ] **Step 5: Commit**

```bash
git add rca-bot/claude_client.py rca-bot/tests/test_claude_client.py
git commit -m "feat(rca-bot): Claude client with eligibility and RCA gap prompts"
```

---

## Task 7: `scan.py` — Daily Bug Eligibility Scanner

**Files:**
- Create: `rca-bot/scan.py`
- Create: `rca-bot/tests/test_scan.py`

- [ ] **Step 1: Write failing tests**

Create `rca-bot/tests/test_scan.py`:

```python
from unittest.mock import MagicMock, patch
from models import Bug
from scan import should_skip, run_scan


def _make_bug(key="INT-001", labels=None, resolution=None, priority="P1"):
    return Bug(
        key=key, summary="Test bug", description="Desc",
        priority=priority, labels=labels or [],
        assignee_name="Alice", assignee_account_id="acc",
        resolution=resolution,
    )


def test_skip_clone_label():
    bug = _make_bug(labels=["CLONE", "INT_CFB"])
    assert should_skip(bug) == ("clone", "CLONE label present")


def test_skip_cicd_label():
    bug = _make_bug(labels=["CICD_FAIL_BUG"])
    assert should_skip(bug) == ("cicd", "CICD_FAIL_BUG label present")


def test_skip_duplicate_resolution():
    bug = _make_bug(resolution="Duplicate")
    assert should_skip(bug) == ("duplicate", "resolution is Duplicate")


def test_no_skip_for_normal_bug():
    bug = _make_bug(labels=["INT_CFB"], resolution=None)
    assert should_skip(bug) is None


def test_no_skip_for_unset_priority():
    bug = _make_bug(priority="Unset", labels=[])
    assert should_skip(bug) is None


def test_run_scan_skips_clone_bug(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    clone_bug = _make_bug(labels=["CLONE"])

    mock_jira = MagicMock()
    mock_jira.get_bugs_since.return_value = [clone_bug]
    mock_claude = MagicMock()

    run_scan(mock_jira, mock_claude, dry_run=False)

    mock_claude.judge_rca_eligibility.assert_not_called()
    mock_jira.add_label.assert_not_called()


def test_run_scan_adds_label_for_eligible_bug(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    bug = _make_bug(labels=["INT_CFB"])

    mock_jira = MagicMock()
    mock_jira.get_bugs_since.return_value = [bug]
    mock_claude = MagicMock()
    mock_claude.judge_rca_eligibility.return_value = {
        "eligible": True, "reason": "Service outage", "confidence": "high"
    }

    run_scan(mock_jira, mock_claude, dry_run=False)

    mock_jira.add_label.assert_called_once_with("INT-001", mock_jira.add_label.call_args.args[1])


def test_run_scan_dry_run_does_not_add_label(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    bug = _make_bug(labels=["INT_CFB"])

    mock_jira = MagicMock()
    mock_jira.get_bugs_since.return_value = [bug]
    mock_claude = MagicMock()
    mock_claude.judge_rca_eligibility.return_value = {
        "eligible": True, "reason": "Outage", "confidence": "high"
    }

    run_scan(mock_jira, mock_claude, dry_run=True)

    mock_jira.add_label.assert_not_called()


def test_run_scan_updates_state(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    mock_jira = MagicMock()
    mock_jira.get_bugs_since.return_value = []
    mock_claude = MagicMock()

    run_scan(mock_jira, mock_claude, dry_run=False)

    state_file = tmp_path / "state.json"
    assert state_file.exists()
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_scan.py -v
```

Expected: `ModuleNotFoundError: No module named 'scan'`

- [ ] **Step 3: Create `rca-bot/scan.py`**

```python
import argparse
import logging
from datetime import datetime, timezone
from config import load_config
from jira_client import JiraClient
from claude_client import ClaudeClient
from models import Bug
from state import load_last_scan_at, save_last_scan_at

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

_SKIP_LABELS = {"CLONE", "CICD_FAIL_BUG"}


def should_skip(bug: Bug) -> tuple[str, str] | None:
    for label in bug.labels:
        if label == "CLONE":
            return ("clone", "CLONE label present")
        if label == "CICD_FAIL_BUG":
            return ("cicd", "CICD_FAIL_BUG label present")
    if bug.resolution == "Duplicate":
        return ("duplicate", "resolution is Duplicate")
    return None


def run_scan(jira: JiraClient, claude: ClaudeClient, dry_run: bool = False) -> None:
    config = jira  # config accessible via jira instance for label name
    since = load_last_scan_at()
    log.info(f"Scanning bugs since {since.isoformat()}")

    bugs = jira.get_bugs_since(jira._config.jira_filter_screening if hasattr(jira, '_config') else "101489", since)
    log.info(f"Found {len(bugs)} new bugs")

    for bug in bugs:
        skip = should_skip(bug)
        if skip:
            log.info(f"SKIP [{bug.key}] reason={skip[0]}: {skip[1]}")
            continue

        result = claude.judge_rca_eligibility(
            summary=bug.summary,
            description=bug.description,
            priority=bug.priority,
            labels=bug.labels,
        )
        log.info(
            f"[{bug.key}] eligible={result['eligible']} "
            f"confidence={result['confidence']} reason={result['reason']}"
        )

        if result["eligible"] and not dry_run:
            label = jira._label if hasattr(jira, '_label') else "INT_RCA_CANDIDATE"
            jira.add_label(bug.key, label)
            log.info(f"[{bug.key}] labeled {label}")

    save_last_scan_at(datetime.now(timezone.utc))
    log.info("Scan complete. State updated.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Daily RCA eligibility scan")
    parser.add_argument("--dry-run", action="store_true", help="Do not write labels to Jira")
    args = parser.parse_args()

    cfg = load_config()
    jira = JiraClient(cfg)
    jira._config = cfg
    jira._label = cfg.jira_label_rca_candidate
    claude = ClaudeClient(cfg.anthropic_api_key)

    run_scan(jira, claude, dry_run=args.dry_run)
```

> **Note:** The `_config` and `_label` attributes are set on the JiraClient in `__main__` and accessed via duck typing in `run_scan`. This lets tests pass mock objects without needing a real Config.

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_scan.py -v
```

Expected: 8 tests pass.

- [ ] **Step 5: Commit**

```bash
git add rca-bot/scan.py rca-bot/tests/test_scan.py
git commit -m "feat(rca-bot): daily bug eligibility scanner"
```

---

## Task 8: `remind.py` — Monday Morning Reminder

**Files:**
- Create: `rca-bot/remind.py`
- Create: `rca-bot/tests/test_remind.py`

- [ ] **Step 1: Write failing tests**

Create `rca-bot/tests/test_remind.py`:

```python
from unittest.mock import MagicMock
from models import Bug
from remind import run_remind


def _make_bug(key, summary, assignee):
    return Bug(
        key=key, summary=summary, description="", priority="P1",
        labels=[], assignee_name=assignee, assignee_account_id="acc",
        resolution=None,
    )


def test_run_remind_fetches_rca_filter_and_posts():
    mock_jira = MagicMock()
    mock_teams = MagicMock()
    bugs = [_make_bug("INT-001", "DB outage", "Alice")]
    mock_jira.get_filter_bugs.return_value = bugs

    run_remind(mock_jira, mock_teams, filter_id="97314")

    mock_jira.get_filter_bugs.assert_called_once_with("97314")
    mock_teams.post_reminder.assert_called_once_with(bugs)


def test_run_remind_posts_even_with_no_bugs():
    mock_jira = MagicMock()
    mock_teams = MagicMock()
    mock_jira.get_filter_bugs.return_value = []

    run_remind(mock_jira, mock_teams, filter_id="97314")

    mock_teams.post_reminder.assert_called_once_with([])
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_remind.py -v
```

Expected: `ModuleNotFoundError: No module named 'remind'`

- [ ] **Step 3: Create `rca-bot/remind.py`**

```python
import logging
from config import load_config
from jira_client import JiraClient
from teams_client import TeamsClient

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)


def run_remind(jira: JiraClient, teams: TeamsClient, filter_id: str) -> None:
    bugs = jira.get_filter_bugs(filter_id)
    log.info(f"Posting reminder for {len(bugs)} RCA bugs")
    teams.post_reminder(bugs)
    log.info("Reminder posted to Teams")


if __name__ == "__main__":
    cfg = load_config()
    jira = JiraClient(cfg)
    teams = TeamsClient(cfg.teams_webhook_url)
    run_remind(jira, teams, filter_id=cfg.jira_filter_rca_flagged)
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_remind.py -v
```

Expected: 2 tests pass.

- [ ] **Step 5: Commit**

```bash
git add rca-bot/remind.py rca-bot/tests/test_remind.py
git commit -m "feat(rca-bot): Monday morning Teams reminder"
```

---

## Task 9: `review.py` — RCA Gap Analyzer

**Files:**
- Create: `rca-bot/review.py`
- Create: `rca-bot/tests/test_review.py`

- [ ] **Step 1: Write failing tests**

Create `rca-bot/tests/test_review.py`:

```python
from unittest.mock import MagicMock
from models import Bug
from review import run_review


def _make_bug(key="INT-001", rca_text="What happened: DB sync failed...", fix_text="Fixed by removing DDL"):
    return Bug(
        key=key, summary="DB sync failed", description="Service outage",
        priority="P1", labels=[], assignee_name="Alice",
        assignee_account_id="acc", resolution=None,
        rca_text=rca_text, fix_text=fix_text,
    )


def test_skip_if_bot_already_commented():
    mock_jira = MagicMock()
    mock_claude = MagicMock()
    bug = _make_bug()
    mock_jira.get_filter_bugs.return_value = [bug]
    mock_jira.has_bot_comment.return_value = True

    run_review(mock_jira, mock_claude, filter_id="97314")

    mock_claude.analyze_rca_gaps.assert_not_called()
    mock_jira.post_comment.assert_not_called()


def test_skip_and_post_placeholder_when_rca_empty():
    mock_jira = MagicMock()
    mock_claude = MagicMock()
    bug = _make_bug(rca_text="")
    mock_jira.get_filter_bugs.return_value = [bug]
    mock_jira.has_bot_comment.return_value = False

    run_review(mock_jira, mock_claude, filter_id="97314")

    mock_claude.analyze_rca_gaps.assert_not_called()
    mock_jira.post_comment.assert_called_once()
    comment_text = mock_jira.post_comment.call_args.args[1]
    assert "not yet filled" in comment_text.lower() or "empty" in comment_text.lower()


def test_posts_gap_analysis_comment():
    mock_jira = MagicMock()
    mock_claude = MagicMock()
    bug = _make_bug()
    mock_jira.get_filter_bugs.return_value = [bug]
    mock_jira.has_bot_comment.return_value = False
    mock_claude.analyze_rca_gaps.return_value = {
        "rubric_gaps": ["Missing prevention section"],
        "five_whys_chain": [{"why": "DB lock", "covered": True, "note": ""}],
        "deepest_unanswered_why": "No review checklist",
        "comment_markdown": "🤖 RCA Bot Review\n\nRUBRIC GAPS:\n• Missing prevention section",
    }

    run_review(mock_jira, mock_claude, filter_id="97314")

    mock_claude.analyze_rca_gaps.assert_called_once_with(
        rca_text=bug.rca_text,
        fix_text=bug.fix_text,
        bug_summary=bug.summary,
        bug_description=bug.description,
    )
    mock_jira.post_comment.assert_called_once_with(
        "INT-001", "🤖 RCA Bot Review\n\nRUBRIC GAPS:\n• Missing prevention section"
    )


def test_processes_multiple_bugs_independently():
    mock_jira = MagicMock()
    mock_claude = MagicMock()
    bugs = [_make_bug("INT-001"), _make_bug("INT-002")]
    mock_jira.get_filter_bugs.return_value = bugs
    mock_jira.has_bot_comment.return_value = False
    mock_claude.analyze_rca_gaps.return_value = {
        "rubric_gaps": [], "five_whys_chain": [],
        "deepest_unanswered_why": "", "comment_markdown": "🤖 ok"
    }

    run_review(mock_jira, mock_claude, filter_id="97314")

    assert mock_claude.analyze_rca_gaps.call_count == 2
    assert mock_jira.post_comment.call_count == 2
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/test_review.py -v
```

Expected: `ModuleNotFoundError: No module named 'review'`

- [ ] **Step 3: Create `rca-bot/review.py`**

```python
import logging
from config import load_config
from jira_client import JiraClient
from claude_client import ClaudeClient

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

_EMPTY_RCA_COMMENT = (
    "🤖 RCA Bot: The RCA content field is not yet filled in for this bug. "
    "Please add the root cause analysis before tonight's forum.\n\n"
    "_Generated by rca-bot._"
)


def run_review(jira: JiraClient, claude: ClaudeClient, filter_id: str) -> None:
    bugs = jira.get_filter_bugs(filter_id)
    log.info(f"Reviewing {len(bugs)} RCA-flagged bugs")

    for bug in bugs:
        if jira.has_bot_comment(bug.key):
            log.info(f"[{bug.key}] already reviewed — skipping")
            continue

        if not bug.rca_text.strip():
            log.info(f"[{bug.key}] RCA content empty — posting placeholder")
            jira.post_comment(bug.key, _EMPTY_RCA_COMMENT)
            continue

        log.info(f"[{bug.key}] Analyzing RCA gaps...")
        result = claude.analyze_rca_gaps(
            rca_text=bug.rca_text,
            fix_text=bug.fix_text,
            bug_summary=bug.summary,
            bug_description=bug.description,
        )
        jira.post_comment(bug.key, result["comment_markdown"])
        gaps = len(result["rubric_gaps"])
        depth = len([w for w in result["five_whys_chain"] if not w["covered"]])
        log.info(f"[{bug.key}] Posted review: {gaps} rubric gaps, {depth} uncovered 5Y steps")


if __name__ == "__main__":
    cfg = load_config()
    jira = JiraClient(cfg)
    claude = ClaudeClient(cfg.anthropic_api_key)
    run_review(jira, claude, filter_id=cfg.jira_filter_rca_flagged)
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/test_review.py -v
```

Expected: 4 tests pass.

- [ ] **Step 5: Run the full test suite**

```bash
pytest rca-bot/tests/ -v
```

Expected: all tests pass (24 total across all modules).

- [ ] **Step 6: Commit**

```bash
git add rca-bot/review.py rca-bot/tests/test_review.py
git commit -m "feat(rca-bot): RCA gap analyzer with 5 Whys analysis"
```

---

## Task 10: README + Task Scheduler Setup

**Files:**
- Create: `rca-bot/README.md`
- Create: `rca-bot/setup.bat`

- [ ] **Step 1: Create `rca-bot/README.md`**

````markdown
# RCA Forum Orchestrator

Three Python scripts that automate the weekly Monday RCA forum.

## Setup

1. Copy `.env.example` to `.env` and fill in all values:
   ```
   cp .env.example .env
   ```
   To get `BOT_JIRA_ACCOUNT_ID`: `GET https://nice-ce-cxone-prod.atlassian.net/rest/api/3/myself`
   (Basic auth with your credentials — copy the `accountId` field.)

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Register scheduled tasks (run once as Administrator):
   ```
   setup.bat
   ```

## Scripts

| Script | Run manually | Purpose |
|---|---|---|
| `python remind.py` | Any time | Post Teams reminder for tonight's RCA bugs |
| `python scan.py --dry-run` | Any time | Preview eligibility decisions without writing labels |
| `python scan.py` | Daily 09:00 | Screen new bugs and label eligible ones |
| `python review.py` | Any time | Post RCA gap analysis to Jira (idempotent) |

## Verification

- **remind.py**: Run manually → check Teams channel for card listing tonight's bugs
- **scan.py**: `python scan.py --dry-run` → inspect log for skip/eligible decisions
- **review.py**: `python review.py` → check INT-56504 in Jira for a new bot comment
- **State guard**: Run `scan.py` twice → second run should process 0 bugs
- **Dupe guard**: Run `review.py` twice → second run should skip all bugs already reviewed
````

- [ ] **Step 2: Create `rca-bot/setup.bat`**

```bat
@echo off
echo Registering RCA Bot scheduled tasks...

set PYTHON=%~dp0..\venv\Scripts\python.exe
set SCRIPTS=%~dp0

schtasks /create /tn "RCA-Bot-Remind" /tr "%PYTHON% %SCRIPTS%remind.py" /sc weekly /d MON /st 08:00 /f
schtasks /create /tn "RCA-Bot-Scan" /tr "%PYTHON% %SCRIPTS%scan.py" /sc daily /st 09:00 /f
schtasks /create /tn "RCA-Bot-Review" /tr "%PYTHON% %SCRIPTS%review.py" /sc daily /st 10:00 /f

echo Done. Tasks registered:
schtasks /query /tn "RCA-Bot-Remind"
schtasks /query /tn "RCA-Bot-Scan"
schtasks /query /tn "RCA-Bot-Review"
```

> **Note:** Update `PYTHON` path if not using a virtualenv at `../venv`. Run as Administrator.

- [ ] **Step 3: Commit**

```bash
git add rca-bot/README.md rca-bot/setup.bat
git commit -m "feat(rca-bot): README and Task Scheduler setup script"
```

---

## Self-Review

**Spec coverage check:**
- ✅ Monday 8am Teams reminder → `remind.py` + `TeamsClient`
- ✅ Daily bug scan with Stage 1 rule filter + Stage 2 Claude Haiku → `scan.py`
- ✅ Skip CLONE / CICD_FAIL_BUG / Duplicate labels → `should_skip()` in `scan.py`
- ✅ INT_RCA_CANDIDATE label added on eligible → `scan.py` + `JiraClient.add_label`
- ✅ RCA gap analysis with rubric check → `ClaudeClient.analyze_rca_gaps`
- ✅ 5 Whys chain construction and gap mapping → prompt in `claude_client.py`
- ✅ Jira comment posted with gap report → `review.py` + `JiraClient.post_comment`
- ✅ Duplicate comment guard (has_bot_comment) → `JiraClient.has_bot_comment`
- ✅ State tracking (last_scan_at) → `state.py`
- ✅ Dry-run flag → `scan.py --dry-run`
- ✅ Claude Haiku for scan, Sonnet for review → hardcoded in `claude_client.py`
- ✅ Jira filter IDs 97314 / 101489 → `config.py` defaults
- ✅ ADF text extraction for customfield_10117 → `_extract_adf_text` in `jira_client.py`
- ✅ Task Scheduler setup → `setup.bat`

**Type consistency check:**
- `Bug` and `Comment` defined in `models.py`, imported consistently everywhere
- `JiraClient.get_filter_bugs` returns `list[Bug]` — used by `remind.py` and `review.py` ✅
- `JiraClient.get_bugs_since` returns `list[Bug]` — used by `scan.py` ✅
- `ClaudeClient.judge_rca_eligibility` returns `dict` with keys `eligible`, `reason`, `confidence` — accessed consistently in `scan.py` ✅
- `ClaudeClient.analyze_rca_gaps` returns `dict` with key `comment_markdown` — used in `review.py` ✅
