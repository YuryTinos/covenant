from covenant.models import BiasContract


def hiring_contract() -> BiasContract:
    return BiasContract.model_validate(
        {
            "header": {
                "contract_id": "hiring-eu-v1",
                "version": "1.0.0",
                "status": "active",
                "domain": "hiring",
                "jurisdiction": ["EU"],
                "owner": "talent-platform-risk",
                "created_at": "2026-02-01T00:00:00Z",
                "supersedes": None,
            },
            "invariants": {
                "explainability_required": True,
                "refusal_allowed": True,
                "no_silent_modification": True,
            },
            "hard_constraints": {
                "forbidden_signals": ["race", "religion"],
                "forbidden_intents": ["discrimination"],
                "forbidden_operations": ["ranking_by_cultural_fit"],
            },
            "soft_signals": {
                "allowlist": ["skills", "experience"],
                "denylist": ["age", "gender"],
            },
            "bias_primitives": {
                "risk_aversion": "high",
                "safety_over_efficiency": True,
                "uncertainty_penalty": "medium",
            },
            "refusal_rules": [],
        }
    )
