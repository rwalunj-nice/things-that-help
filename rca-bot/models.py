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
