# ADR 0002: Deterministic policy checks precede LLM analysis

- **Status:** Accepted
- **Date:** 2026-09-18

## Context

Policy requirements such as mandatory MFA, expiry, logging, encrypted management protocols, and prohibited zone paths should not depend on probabilistic interpretation when the inputs are structured.

## Decision

Structured evidence is evaluated by deterministic rules before it is provided to the model. The model may explain results, identify relationships, and propose safeguards, but it cannot suppress or rewrite deterministic findings.

## Consequences

- Control behaviour is testable and repeatable.
- Model prompts remain simpler.
- Conflicts between model commentary and policy results are detectable.
- Policy-as-code maintenance becomes a distinct governed activity.
