# Regulatory FAQ — Bias Contracts & Covenant

## What happens when a user asks the system to do something prohibited?

The request is **refused before any AI model runs**.

No output is generated, no partial result exists, and no post-processing occurs.
The refusal is deterministic and attributable to a specific, pre-approved rule.

---

## What happens when a prohibited type of decision is requested indirectly?

Indirect phrasing does not bypass controls.

The system evaluates **intent and decision type**, not just wording.
If the underlying intent or operation is prohibited, the request is refused.

---

## What happens when a decision would rely on forbidden information?

If forbidden information appears **after** generation, it is:

- explicitly identified
- visibly removed (redacted)
- recorded in an audit artifact

No silent filtering occurs.

---

## What happens when a contract is invalid or contradictory?

The system refuses to operate.

If the governing rules are incomplete, inactive, or internally inconsistent, **no automated decision is allowed to proceed**. This prevents false compliance.

---

## What happens when rules change over time?

Rules are versioned.

Each decision is tied to:

- a specific contract
- a specific version
- a specific point in time

Changes require issuing a new version; past decisions remain traceable to the rules that governed them.

---

## What happens when an outcome appears unfair despite compliance?

Compliance does not guarantee fairness.

When outcomes raise concerns:

- the governing contract can be reviewed
- constraints can be tightened explicitly
- a new version can be issued

The system ensures responsibility for outcomes is **visible and contestable**, not hidden.

---

## What happens if the system cannot decide safely?

The system refuses.

Refusal is a supported, intentional outcome designed to prevent unsafe or non-compliant decisions from existing at all.

---

## What happens if a model behaves unpredictably?

Model behavior does not override governance.

Pre-decision checks occur **before** the model runs, and post-decision checks enforce constraints **after** output. Model variability does not weaken controls.

---

## What happens if regulators audit a past decision?

Each decision produces an audit artifact that documents:

- the governing rules
- the version applied
- the enforcement actions taken
- the time of execution

Audits do not rely on reconstruction or inference.

---

## What happens if a prohibited decision would have been profitable or efficient?

Governance overrides optimization.

The system enforces declared constraints regardless of performance, efficiency, or business incentives.

---

## What happens if no bias rules are declared?

No decision is allowed.

The system does not assume defaults.
Explicit declaration is required for operation.

---

## What happens if someone tries to bypass governance?

Bypass attempts fail at enforcement boundaries.

Rules are enforced at execution time, not at the user interface or policy-document level.

---

## What happens when regulations differ by jurisdiction?

Contracts are scoped by jurisdiction.

Different rules can be declared and enforced for different regulatory environments, without changing the underlying system.

---

## What happens if a regulator’s interpretation changes?

Governance adapts through **new contract versions**, not silent changes.

This preserves historical accountability while allowing future compliance.

---

## What happens when the system makes no decision?

That outcome is intentional and recorded.

A refusal indicates that governance prevented an illegitimate decision, not that the system malfunctioned.

---

# Regulatory summary

> **This system does not attempt to predict or justify outcomes after the fact.
> It ensures that automated decisions only occur under explicitly approved, enforceable rules, with full traceability.**
