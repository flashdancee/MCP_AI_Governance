# Architecture

## Context

The system assists a human reviewer by collecting narrowly scoped evidence from MCP services and producing a structured draft assessment. It does not authorize or execute infrastructure changes.

## Components

### Review interface

Accepts a typed review request and presents evidence, findings, uncertainty, proposed safeguards, and the human decision. The interface never communicates directly with infrastructure connectors.

### Orchestrator

Controls the workflow and owns the review state machine. Responsibilities include:

- request validation;
- identity and authorization context propagation;
- tool allowlisting;
- evidence normalization;
- deterministic policy evaluation;
- model-context construction;
- output validation;
- approval workflow; and
- audit emission.

The model may propose a tool call, but the orchestrator independently decides whether it is permitted.

### Local model adapter

Provides a model-neutral interface to an Ollama-hosted model. It receives only the minimum evidence required for the current step. Model output is treated as untrusted until it passes schema and policy validation.

### MCP servers

Each server has a distinct identity, data boundary, and tool catalogue. The MVP exposes read-only tools such as:

```text
network.get_change_request
network.list_relevant_rules
network.get_zone
security.get_asset_context
security.list_vulnerabilities
governance.get_policy_requirements
governance.get_risk_criteria
audit.append_event
```

No generic file, URL, database, or shell tool will be exposed.

### Deterministic policy engine

Evaluates controls that should not depend on probabilistic output. Initial rules include:

- source and destination scope must be explicit;
- administrative access cannot originate from `any`;
- privileged vendor access requires MFA;
- access must have an owner and expiry;
- logging must be enabled;
- management protocols must be encrypted;
- direct user-to-BAS access is prohibited;
- vulnerable assets require documented safeguards; and
- unresolved critical evidence blocks approval.

### Evidence store

Stores immutable synthetic inputs and normalized evidence objects. Each object has a stable identifier, content hash, source, collection time, and sensitivity label.

### Audit store

Records review events in append-only form. Events include correlation ID, actor, tool, arguments after redaction, result hash, authorization decision, policy outcome, model identifier, approval state, and timestamp.

## Trust boundaries

1. User to review interface
2. Interface to orchestrator
3. Orchestrator to local model
4. Orchestrator to each MCP server
5. MCP server to its synthetic data source
6. Orchestrator to audit store
7. Human approver to decision record

Crossing a boundary requires authenticated identity, explicit authorization, validation, and an audit event.

## Review state machine

```text
RECEIVED
  -> VALIDATED
  -> EVIDENCE_COLLECTION
  -> DETERMINISTIC_CHECKS
  -> ASSISTED_ANALYSIS
  -> OUTPUT_VALIDATION
  -> AWAITING_HUMAN_DECISION
  -> APPROVED | REJECTED | REVISION_REQUIRED
```

An authorization failure, invalid schema, missing mandatory evidence, or integrity failure moves the review to `FAILED_SAFE`.

## Data handling

- Demonstrations use synthetic data only.
- Evidence receives a sensitivity label before model use.
- Secrets are prohibited and scanned at ingestion and commit time.
- Logs contain hashes or redacted values where raw arguments are unnecessary.
- Model context is ephemeral by default.
- Retention periods are configurable and documented.

## Deployment model

The demonstration runs on a single home-lab host using rootless containers and an isolated container network. Services run as non-root users, mount read-only fixtures, expose only required ports, and use pinned images and dependencies.

Production deployment is outside the initial scope.
