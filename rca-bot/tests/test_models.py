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
