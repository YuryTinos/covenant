import re
from datetime import datetime
from typing import List

from covenant.models import (
    BiasContract,
    PostcheckRequest,
    PostcheckResponse,
    ActionTaken,
    AuditRecord,
)
from covenant.contracts import validate_contract, ContractValidationError


# --- Simple signal patterns for v0 ---

SIGNAL_PATTERNS = {
    "age": [
        r"\byounger\b",
        r"\bolder\b",
        r"\bage\b",
    ],
    "gender": [
        r"\bmale\b",
        r"\bfemale\b",
        r"\bman\b",
        r"\bwoman\b",
    ],
}


def postcheck_decision(req: PostcheckRequest) -> PostcheckResponse:
    """
    Perform post-generation enforcement.

    This function:
    - validates the Bias Contract
    - detects denylisted signals in model output
    - applies explicit redaction
    - produces an audit artifact
    """

    try:
        validate_contract(req.contract)
    except ContractValidationError as e:
        return _refuse(
            req,
            reason=str(e),
            signals_ignored=[],
            actions=[],
        )

    output = req.llm_output
    actions: List[ActionTaken] = []
    ignored_signals: List[str] = []

    # 1. Enforce soft signal denylist
    for signal in req.contract.soft_signals.denylist:
        patterns = SIGNAL_PATTERNS.get(signal, [])
        if _contains_signal(output, patterns):
            output = _redact_signal(output, patterns)
            ignored_signals.append(signal)
            actions.append(
                ActionTaken(
                    type="redaction",
                    signal=signal,
                    reason="Signal is denylisted by contract",
                )
            )

    # 2. Build audit record
    audit = AuditRecord(
        decision_id=req.decision_id,
        contract_id=req.contract.header.contract_id,
        version=req.contract.header.version,
        precheck_decision="allow",
        postcheck_decision="redact" if actions else "allow",
        signals_ignored=ignored_signals,
        actions=actions,
        timestamp=_now(),
    )

    return PostcheckResponse(
        decision="allow",
        output=output,
        actions=actions,
        audit=audit,
    )


def _contains_signal(text: str, patterns: List[str]) -> bool:
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def _redact_signal(text: str, patterns: List[str]) -> str:
    for pattern in patterns:
        text = re.sub(pattern, "[REDACTED]", text, flags=re.IGNORECASE)
    return text


def _refuse(
    req: PostcheckRequest,
    reason: str,
    signals_ignored: List[str],
    actions: List[ActionTaken],
) -> PostcheckResponse:
    audit = AuditRecord(
        decision_id=req.decision_id,
        contract_id=req.contract.header.contract_id,
        version=req.contract.header.version,
        precheck_decision="allow",
        postcheck_decision="refuse",
        signals_ignored=signals_ignored,
        actions=actions,
        timestamp=_now(),
    )

    return PostcheckResponse(
        decision="refuse",
        output=None,
        actions=actions,
        audit=audit,
    )


def _now() -> str:
    return datetime.utcnow().isoformat()
