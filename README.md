# Covenant

**Explicit Bias Governance for LLM Decisions**

This document defines the non-negotiable principles of Covenant.  
Any implementation that violates them is not Covenant.

---

## What is Covenant?

**Covenant** is an ex-ante bias governance layer that enforces explicit decision contracts around LLM outputs.

Covenant sits between applications and language models to ensure that:
- bias is declared **before** generation,
- forbidden considerations are structurally excluded,
- refusals are valid outcomes,
- and every decision is auditable.

Covenant does **not** attempt to remove bias.  
It makes bias **intentional, bounded, and accountable**.

---

## What Covenant Is

- A **decision governor** for LLM-based systems  
- A **bias contract enforcement layer**  
- A **refusal-capable compliance primitive**  
- A bridge between **policy and execution**

---

## What Covenant Is Not

- An AI model  
- A fairness optimizer  
- A moderation API  
- A prompt-engineering framework  
- An analytics or monitoring dashboard  

Covenant does not generate text.  
It governs whether text is allowed to be generated — and whether it is allowed to stand.

---

## Core Thesis

> Bias is inevitable.  
> Hidden bias is dangerous.  
> Explicit bias is governable.

Modern AI systems rely on soft controls such as prompts, fine-tuning, and post-hoc moderation.  
These mechanisms are probabilistic, fragile, and difficult to audit.

Covenant replaces post-hoc justification with **pre-decision commitment**.

---

## Non-Negotiable Invariants

These principles define Covenant. They are not configurable.

1. **No neutral mode**  
   Every decision requires an explicit bias contract.

2. **Bias is declared before execution**  
   Ex-ante governance, not post-hoc explanation.

3. **Refusal is a valid and expected outcome**  
   Some decisions must not exist.

4. **No silent intervention**  
   Any modification, redaction, or refusal is explicit and logged.

5. **Deterministic behavior in the MVP**  
   No learning, no adaptation, no probabilistic policy shifts.

6. **Contracts are immutable once active**  
   Changes require explicit versioning.

7. **Covenant never generates content**  
   It governs decisions, not language.

---

## Responsibility Boundaries

Covenant exists to prevent responsibility diffusion.

| Layer        | Responsibility |
|-------------|----------------|
| Application | User experience, intent capture |
| **Covenant** | Decision validity, bias enforcement, refusal |
| LLM         | Text generation only |
| Organization | Defining what it is willing to commit to |

Covenant eliminates the excuse:  
> “The model decided.”

---

## Initial Supported Domain

**Covenant v0 is intentionally scoped to a single domain:**

> **Hiring / Candidate Evaluation**

This domain was chosen because:
- bias risk is well understood,
- legal constraints are explicit,
- and the cost of ambiguity is high.

Other domains are explicitly **out of scope** for the MVP.

---

## Why Covenant Exists Now

LLMs are being deployed faster than governance structures can adapt.

Current controls rely on:
- prompt instructions,
- probabilistic moderation,
- and post-hoc explanations.

Regulators, auditors, and internal risk teams are increasingly asking for:
> proof of intent **at the time of decision**, not after incidents occur.

Covenant exists to fill the gap between policy and execution by making bias explicit **before** generation.

---

## What Covenant Will Not Do

Covenant explicitly refuses to:

- Offer a “best effort” or “neutral” mode  
- Optimize throughput at the expense of legitimacy  
- Infer protected attributes  
- Automatically rewrite or “fix” prompts  
- Learn from user behavior to adjust bias  

Constraint is a feature, not a limitation.

---

## Design Direction

Covenant is designed to be:

- Model-agnostic  
- Deterministic  
- Auditable  
- Refusal-capable  

The MVP prioritizes clarity and legitimacy over scale or convenience.

---

## Status

This repository currently documents **Plan 0**: the frozen identity and invariants of Covenant.

Implementation begins only after these principles are locked.

---

## License

TBD
