# Vendor Questionnaire

## Automated Decision Governance & Bias Control

**Instructions to Vendor:**
Please answer all questions clearly. Responses such as _“it depends”_, _“best effort”_, or _“handled by the model”_ are insufficient. Where applicable, provide documentation or examples.

---

## Section 1 — System Scope

1. Describe the types of automated decisions your system produces (e.g., recommendations, rankings, approvals, denials).

2. In which domains is your system currently deployed (e.g., hiring, credit, healthcare, content moderation)?

3. Does your system produce outputs that could materially affect individuals, access, or outcomes?
   - [ ] Yes
   - [ ] No

---

## Section 2 — Governance Model

4. Does your system require **explicit, documented rules** defining what decisions are allowed before execution?
   - [ ] Yes
   - [ ] No

5. Are these rules enforced **by the system itself**, rather than by user guidelines or training?
   - [ ] Yes
   - [ ] No

6. Can your system operate without any governance rules being declared?
   - [ ] Yes
   - [ ] No
         _(If “Yes”, please explain how risks are mitigated.)_

---

## Section 3 — Bias Declaration

7. Does your system require explicit declaration of which decision factors are allowed?
   - [ ] Yes
   - [ ] No

8. Does your system explicitly prohibit certain decision factors (e.g., age, gender, health)?
   - [ ] Yes
   - [ ] No

9. Are prohibited decision factors enforced even if they appear indirectly or implicitly?
   - [ ] Yes
   - [ ] No

10. Are there any implicit defaults when rules are not specified?
    - [ ] Yes
    - [ ] No
          _(If “Yes”, please list them.)_

---

## Section 4 — Refusal Capability

11. Can your system intentionally refuse to produce a decision?
    - [ ] Yes
    - [ ] No

12. Is refusal a **documented and supported outcome**, rather than an error state?
    - [ ] Yes
    - [ ] No

13. Can refusal occur **before** any AI model or inference is executed?
    - [ ] Yes
    - [ ] No

14. Are refusal reasons recorded and reviewable?
    - [ ] Yes
    - [ ] No

---

## Section 5 — Determinism and Predictability

15. Given the same input and rules, does governance behavior remain consistent across executions?
    - [ ] Yes
    - [ ] No

16. Are governance decisions independent of model randomness (e.g., temperature, sampling)?
    - [ ] Yes
    - [ ] No

17. Can governance outcomes be reproduced for audit or investigation purposes?
    - [ ] Yes
    - [ ] No

---

## Section 6 — Post-Decision Controls

18. Does your system evaluate outputs after generation for prohibited information?
    - [ ] Yes
    - [ ] No

19. When prohibited information is detected, is it **explicitly removed** rather than silently ignored?
    - [ ] Yes
    - [ ] No

20. Are enforcement actions (e.g., redactions) visible and reviewable?
    - [ ] Yes
    - [ ] No

---

## Section 7 — Auditability

21. Does each automated decision generate a structured audit record?
    - [ ] Yes
    - [ ] No

22. Does the audit record identify:

- the governing rules applied?
  - [ ] Yes
  - [ ] No
- the version of those rules?
  - [ ] Yes
  - [ ] No
- the enforcement actions taken?
  - [ ] Yes
  - [ ] No

23. Are audit records immutable once created?
    - [ ] Yes
    - [ ] No

24. Can audit records be reviewed without reconstructing intent after the fact?
    - [ ] Yes
    - [ ] No

---

## Section 8 — Rule Changes and Versioning

25. Are governance rules versioned?
    - [ ] Yes
    - [ ] No

26. Does changing governance rules require issuing a new version?
    - [ ] Yes
    - [ ] No

27. Are past decisions permanently tied to the rules in effect at the time?
    - [ ] Yes
    - [ ] No

28. Are silent or retroactive rule changes prevented?
    - [ ] Yes
    - [ ] No

---

## Section 9 — Jurisdiction and Compliance

29. Can governance rules be scoped by jurisdiction (e.g., EU vs. non-EU)?
    - [ ] Yes
    - [ ] No

30. Can different regulatory requirements be enforced without changing the core system?
    - [ ] Yes
    - [ ] No

31. How does your system adapt when regulatory interpretations change?

---

## Section 10 — Failure Modes and Safeguards

32. What happens if governance rules are incomplete or contradictory?

33. In such cases, does the system fail safely by refusing to operate?
    - [ ] Yes
    - [ ] No

34. Are failure behaviors documented and testable?
    - [ ] Yes
    - [ ] No

---

## Section 11 — Accountability

35. Can your organization identify who approved the governance rules currently in effect?
    - [ ] Yes
    - [ ] No

36. Can responsibility be assigned for allowing a specific automated decision to occur?
    - [ ] Yes
    - [ ] No

37. Can regulators or auditors review decisions without requiring deep technical expertise?
    - [ ] Yes
    - [ ] No

---

## Final Declaration (Vendor)

38. Do you attest that the answers above accurately represent your system’s current capabilities?
    - [ ] Yes
    - [ ] No

**Name:**
**Title:**
**Date:**

---

## Internal Evaluation Notes (for your organization)

- Clear refusal support:
  - [ ] Yes
  - [ ] No
- Deterministic governance:
  - [ ] Yes
  - [ ] No
- Explicit bias control:
  - [ ] Yes
  - [ ] No
- Strong auditability:
  - [ ] Yes
  - [ ] No

**Overall governance risk:**

- [ ] Low
- [ ] Medium
- [ ] High

---

### One-line procurement guidance

> **Vendors unable to refuse decisions or make governance explicit should be considered high risk.**
