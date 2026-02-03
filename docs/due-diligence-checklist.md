# Due-Diligence Checklist

## Automated Decision Governance (Bias Contracts / Covenant)

### Section 1 — Governance Foundations

- [ ] Are the rules governing automated decisions **explicitly documented**?
- [ ] Are decision rules defined **before** the system operates (ex-ante)?
- [ ] Is there a formal mechanism to **prevent decisions from occurring**, not just to review them later?
- [ ] Are governance rules enforceable by the system itself, not dependent on user behavior?

**Evidence to request:**
Policy documents, contract definitions, enforcement logic description.

---

### Section 2 — Bias Declaration and Control

- [ ] Does the system require explicit declaration of which decision factors are allowed?
- [ ] Does it explicitly declare which factors are forbidden?
- [ ] Are forbidden decision types blocked regardless of phrasing?
- [ ] Are there **no implicit defaults** when rules are missing?

**Evidence to request:**
Bias Contract examples, configuration schemas, refusal conditions.

---

### Section 3 — Refusal Capability

- [ ] Can the system intentionally refuse to produce a decision?
- [ ] Is refusal a documented and supported outcome?
- [ ] Does refusal occur **before** an AI model runs when required?
- [ ] Are refusal reasons recorded and reviewable?

**Red flag:**
Systems that must always return an output.

---

### Section 4 — Determinism and Predictability

- [ ] Does the same input under the same rules always produce the same governance outcome?
- [ ] Are governance decisions independent of model randomness?
- [ ] Can governance behavior be reproduced for audit or investigation?

**Evidence to request:**
Test cases, deterministic enforcement description.

---

### Section 5 — Post-Decision Controls

- [ ] Are outputs checked after generation for forbidden information?
- [ ] Is prohibited information **explicitly removed**, not silently ignored?
- [ ] Are corrective actions visible to reviewers?

**Evidence to request:**
Redaction examples, post-decision enforcement logic.

---

### Section 6 — Auditability and Traceability

- [ ] Does each decision generate a structured audit artifact?
- [ ] Does the audit record identify the governing rules and version used?
- [ ] Can past decisions be reviewed without reconstructing intent?
- [ ] Are audit records immutable once created?

**Evidence to request:**
Sample audit records, retention policy.

---

### Section 7 — Versioning and Change Management

- [ ] Are governance rules versioned?
- [ ] Does changing rules require issuing a new version?
- [ ] Are past decisions tied to the rules in effect at the time?
- [ ] Are silent or retroactive rule changes prevented?

**Evidence to request:**
Version history, change-management process.

---

### Section 8 — Jurisdiction and Scope

- [ ] Can different rules be applied to different jurisdictions or domains?
- [ ] Is jurisdiction explicitly declared as part of governance?
- [ ] Are cross-jurisdiction conflicts handled through explicit rules?

**Evidence to request:**
Jurisdiction-scoped configurations, examples.

---

### Section 9 — Failure and Edge Cases

- [ ] What happens if governance rules are incomplete or contradictory?
- [ ] Does the system fail safely (refusal) in such cases?
- [ ] Is failure behavior documented and testable?

**Red flag:**
Systems that “best-effort” their way through governance gaps.

---

### Section 10 — Accountability and Oversight

- [ ] Can the organization identify **who approved** the governance rules?
- [ ] Can responsibility be assigned for allowing a decision to occur?
- [ ] Can regulators or auditors review decisions without technical reconstruction?

**Evidence to request:**
Approval workflows, ownership assignment.

---

## Final Due-Diligence Assessment

- [ ] Governance prevents prohibited decisions **before execution**
- [ ] Enforcement is deterministic and auditable
- [ ] Refusal is supported and intentional
- [ ] Responsibility is explicit and traceable

**Overall risk posture:**

- [ ] Low 
- [ ] Medium 
- [ ] High

---

## One-sentence executive summary

> **This system enforces explicit, pre-approved rules on automated decisions and provides full traceability for oversight and audit.**
