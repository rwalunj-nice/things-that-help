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


def _wrap_text_as_adf(text: str) -> dict:
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
            json={"body": _wrap_text_as_adf(markdown_body)},
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
