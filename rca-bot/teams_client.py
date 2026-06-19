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
