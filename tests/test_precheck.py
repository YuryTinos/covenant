from covenant.models import PrecheckRequest, DecisionContext
from covenant.precheck import precheck_decision
from tests.fixtures import hiring_contract


def test_precheck_refuses_forbidden_operation():
    req = PrecheckRequest(
        contract=hiring_contract(),
        prompt="Rank candidates by cultural fit.",
        context=DecisionContext(domain="hiring", jurisdiction="EU"),
    )

    res = precheck_decision(req)

    assert res.decision == "refuse"
    assert "ranking_by_cultural_fit" in res.reason


def test_precheck_allows_valid_prompt():
    req = PrecheckRequest(
        contract=hiring_contract(),
        prompt="Summarize candidates' skills and experience.",
        context=DecisionContext(domain="hiring", jurisdiction="EU"),
    )

    res = precheck_decision(req)

    assert res.decision == "allow"
