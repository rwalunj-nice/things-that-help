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
