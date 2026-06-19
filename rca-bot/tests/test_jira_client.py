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
