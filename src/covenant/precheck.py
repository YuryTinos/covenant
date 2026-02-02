import uuid
from covenant.models import (
    BiasContract,
    PrecheckRequest,
    PrecheckResponse,
)
from covenant.contracts import validate_contract, ContractValidationError


# --- Simple keyword maps for v0 intent / operation detection ---

FORBIDDEN_OPERATION_KEYWORDS = {
    "ranking_by_cultural_fit": ["cultural fit", "culture fit"],
}

FORBIDDEN_INTENT_KEYWORDS = {
    "discrimination": ["prefer", "exclude", "reject based on"],
    "medical_diagnosis": ["diagnose", "diagnosis", "medical condition"],
    "legal_advice": ["legal advice", "sue", "lawsuit"],
}


def precheck_decision(req: PrecheckRequest) -> PrecheckResponse:
    """
    Perform pre-generation enforcement.

    This function:
    - validates the Bias Contract
    - detects forbidden intents or operations
    - refuses execution if any hard constraint is violated
    """

    try:
        validate_contract(req.contract)
    except ContractValidationError as e:
        return PrecheckResponse(
            decision="refuse",
            reason=str(e),
            decision_id=_new_decision_id(),
        )

    prompt = req.prompt.lower()

    # 1. Check forbidden operations
    for operation in req.contract.hard_constraints.forbidden_operations:
        keywords = FORBIDDEN_OPERATION_KEYWORDS.get(operation, [])
        if _contains_any(prompt, keywords):
            return PrecheckResponse(
                decision="refuse",
                reason=f"Forbidden operation detected: {operation}",
                decision_id=_new_decision_id(),
            )

    # 2. Check forbidden intents
    for intent in req.contract.hard_constraints.forbidden_intents:
        keywords = FORBIDDEN_INTENT_KEYWORDS.get(intent, [])
        if _contains_any(prompt, keywords):
            return PrecheckResponse(
                decision="refuse",
                reason=f"Forbidden intent detected: {intent}",
                decision_id=_new_decision_id(),
            )

    # 3. Allowed to proceed
    return PrecheckResponse(
        decision="allow",
        reason="Prompt complies with hard constraints",
        decision_id=_new_decision_id(),
    )


def _contains_any(text: str, keywords: list[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def _new_decision_id() -> str:
    return str(uuid.uuid4())
