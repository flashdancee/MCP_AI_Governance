# Roadmap

## Phase 0 — Architecture and safety baseline

- [x] Define the purpose and initial review workflow.
- [x] Document trust boundaries and primary threats.
- [x] Define governance roles and human decision points.
- [x] Create request and result schemas.
- [ ] Select the official MCP SDK version and pin dependencies.
- [ ] Record model-selection criteria and hardware constraints.
- [x] Define an audit-event schema and integrity strategy.
- [ ] Create repository secret scanning and dependency-update policy.

**Exit condition:** architecture decisions, schemas, threat model, and security acceptance criteria are reviewed before tool code is written.

## Phase 1 — Read-only network review MVP

**In progress:** the deterministic policy engine, review state machine, audit-event schema, review-snapshot schema, Scenario 1 control context, and unit tests are implemented. The next vertical-slice step is the read-only Network MCP service and evidence normalization.

- [ ] Build a synthetic network containing user, server, management, vendor, and BAS zones.
- [ ] Implement a read-only Network MCP server.
- [ ] Implement a read-only Governance MCP server.
- [x] Create deterministic firewall-policy checks.
- [ ] Add a model-neutral local inference adapter.
- [ ] Produce a structured review from the supplied JSON request.
- [ ] Add evidence identifiers and citations.
- [ ] Add a human approval/rejection step.
- [ ] Emit normalized audit events for every tool call and decision.

**Exit condition:** a reviewer can reproduce the vendor-access demonstration locally, and the system refuses all write operations.

## Phase 2 — Security context and evaluations

- [ ] Implement a read-only Security MCP server for synthetic vulnerabilities and alerts.
- [ ] Add asset criticality and exposure context.
- [ ] Build a labelled evaluation set containing safe, unsafe, ambiguous, and incomplete requests.
- [ ] Measure evidence coverage, deterministic-control recall, unsupported assertions, refusal correctness, and run-to-run consistency.
- [ ] Publish results and known limitations.

**Exit condition:** published metrics are reproducible from repository fixtures and test commands.

## Phase 3 — Adversarial security testing

- [ ] Seed prompt injection in policies, asset descriptions, and tool results.
- [ ] Test tool-description spoofing and lookalike tools.
- [ ] Test cross-tenant and cross-review access attempts.
- [ ] Test excessive-result and denial-of-service conditions.
- [ ] Test secret and PII leakage paths.
- [ ] Add integrity verification for evidence and audit events.

**Exit condition:** the documented abuse cases fail safely and produce actionable audit events.

## Phase 4 — Privacy and SaaS assurance workflow

- [ ] Add a fictional healthcare SaaS review package.
- [ ] Model PHI/PII data flows and retention.
- [ ] Include synthetic security questionnaires, DPA clauses, and assurance summaries.
- [ ] Map findings to fictionalized privacy and security requirements inspired by common public-sector obligations.
- [ ] Keep legal conclusions out of model scope; require privacy/legal review.

**Exit condition:** the system identifies seeded privacy risks, cites evidence, and clearly labels matters requiring privacy or legal interpretation.

## Phase 5 — Portfolio-quality demonstration

- [ ] Add architecture and data-flow diagrams.
- [ ] Record a two-to-three-minute demonstration.
- [ ] Add screenshots and an animated overview to the README.
- [ ] Publish a concise engineering retrospective.
- [ ] Tag a stable release with setup and evaluation instructions.

## Explicit non-goals

- Autonomous production changes
- Direct connection to employer systems
- Replacement of accountable security, privacy, or legal reviewers
- Claims of compliance certification
- Unrestricted shell or infrastructure access
- Collection of real PHI, PII, secrets, or proprietary configurations
