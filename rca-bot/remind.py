import argparse
import logging
from config import load_config
from jira_client import JiraClient
from teams_client import TeamsClient

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)


def run_reminder(jira: JiraClient, teams: TeamsClient, filter_id: str) -> None:
    bugs = jira.get_filter_bugs(filter_id)
    log.info(f"Posting reminder for {len(bugs)} bugs")
    teams.post_reminder(bugs)
    log.info("Reminder posted")


if __name__ == "__main__":
    cfg = load_config()
    jira = JiraClient(cfg)
    teams = TeamsClient(cfg.teams_webhook_url)
    run_reminder(jira, teams, filter_id=cfg.jira_filter_rca_flagged)
