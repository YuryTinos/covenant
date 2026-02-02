from covenant.models import PostcheckRequest
from covenant.postcheck import postcheck_decision
from tests.fixtures import hiring_contract


def test_postcheck_redacts_denylisted_signal():
    req = PostcheckRequest(
        decision_id="test-id",
        contract=hiring_contract(),
        llm_output="Candidate A is younger and energetic.",
    )

    res = postcheck_decision(req)

    assert res.decision == "allow"
    assert "[REDACTED]" in res.output
    assert res.audit.postcheck_decision == "redact"
    assert "age" in res.audit.signals_ignored


def test_postcheck_allows_clean_output():
    req = PostcheckRequest(
        decision_id="test-id",
        contract=hiring_contract(),
        llm_output="Candidate A has strong Python skills.",
    )

    res = postcheck_decision(req)

    assert res.decision == "allow"
    assert res.actions == []
    assert res.audit.postcheck_decision == "allow"
