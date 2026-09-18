# Governance model

## Purpose

Governance is implemented as control points in the workflow, not as a policy document placed beside the code.

## Roles

| Role | Responsibility |
|---|---|
| Requester | Supplies the business purpose, scope, owner, duration, and requested outcome |
| Security reviewer | Validates evidence and security analysis |
| Privacy reviewer | Reviews privacy implications when sensitive information is in scope |
| System owner | Confirms operational requirements and accepts implementation obligations |
| Risk owner | Accepts or rejects residual business risk |
| Platform administrator | Maintains the orchestrator and MCP services but cannot approve their own changes |

The home-lab demonstration may use one person in several roles, but the audit record keeps the roles logically distinct.

## Decision authority

The model has no approval authority. It may:

- summarize evidence;
- identify apparent conflicts;
- explain deterministic findings;
- propose safeguards;
- draft questions; and
- identify missing information.

Only an authorized human can approve, reject, or accept residual risk.

## Tool governance

Every tool must have:

- a named owner;
- a documented purpose;
- input and output schemas;
- read/write/destructive annotations;
- an authorization policy;
- sensitivity classification;
- rate and result-size limits;
- test coverage;
- an audit strategy; and
- a retirement process.

New tools are denied by default until reviewed and allowlisted.

## Model governance

Model onboarding requires:

- source and license review;
- hash/version pinning;
- supported-context and hardware documentation;
- task-specific evaluation;
- prompt-injection testing;
- unsupported-assertion measurement;
- privacy review; and
- an approved rollback path.

Changing the model version triggers regression evaluation before promotion.

## Risk-rating approach

The deterministic engine calculates a transparent preliminary rating from:

- asset criticality;
- information sensitivity;
- exposure;
- likelihood;
- technical impact;
- business impact;
- control strength; and
- time-bound exceptions.

The model can explain the rating but cannot silently alter its inputs or formula. Human reviewers can adjust the final rating only with a recorded rationale.

## Evidence requirements

A material finding must include:

1. evidence identifier;
2. source tool and collection time;
3. relevant extracted fact;
4. applicable policy or control;
5. confidence and uncertainty; and
6. recommended action.

Unsupported findings are labelled as hypotheses or questions, not facts.

## Change management

Changes to prompts, tools, schemas, policies, models, or authorization rules require:

- version control;
- peer review where available;
- automated tests;
- threat-model review when trust boundaries change;
- evaluation comparison;
- documented approval; and
- rollback instructions.

## Metrics

Planned metrics include:

- percentage of material statements with valid evidence;
- deterministic violation recall against labelled fixtures;
- unsupported assertion rate;
- correct refusal rate;
- prompt-injection resistance;
- authorization-denial correctness;
- human override rate and rationale;
- time to complete a review; and
- audit-record completeness.

Metrics will not be claimed until reproducible evaluation data exists.
