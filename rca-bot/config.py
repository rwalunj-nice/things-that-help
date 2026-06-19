import os
from dataclasses import dataclass
from dotenv import load_dotenv


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
    load_dotenv()

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
