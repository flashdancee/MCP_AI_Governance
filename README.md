# MCP AI Governance Lab

Security-first reference architecture for using a local large language model to assist infrastructure, cybersecurity, and governance reviews through Model Context Protocol (MCP) tools.

> **Project status:** Phase 1 implementation. The deterministic governance foundation, review state machine, audit-event contract, and Scenario 1 fixtures are now implemented on the MVP branch.

## Why this project exists

AI agents can retrieve evidence and call tools, but a plausible answer is not the same as a defensible security decision. This project explores how to build an AI-assisted review system that is:

- local-first and privacy-conscious;
- evidence-backed rather than purely generative;
- read-only by default;
- explicit about authorization and tool boundaries;
- resilient to prompt injection and unsafe tool chaining;
- auditable from request through human decision; and
- useful for real infrastructure and governance workflows.

The demonstration environment is fictional. It contains no employer information, production configuration, credentials, or real personal or health information.

## Initial use case

A fictional facilities vendor requests remote access to a building-automation subnet. The system gathers synthetic firewall rules, asset context, vulnerabilities, and policy requirements, then produces a structured risk review.

```text
User request
    │
    ▼
Review orchestrator ─────► Local LLM
    │                         │
    ├── Network MCP ──────────┤
    ├── Security MCP ─────────┤
    └── Governance MCP ───────┘
    │
    ▼
Deterministic validation
    │
    ▼
Evidence-backed draft recommendation
    │
    ▼
Human approval or rejection
    │
    ▼
Immutable audit record
```

The first release will not change a firewall. It will review a proposed change and clearly separate machine-generated analysis from the accountable human decision.

## Planned MCP services

| Service | Purpose | Initial authority |
|---|---|---|
| Network MCP | Retrieve synthetic zones, objects, routes, firewall policy, and diagrams | Read-only |
| Security MCP | Retrieve fictional assets, vulnerabilities, alerts, and exposure context | Read-only |
| Governance MCP | Retrieve policies, controls, risk criteria, exceptions, and review templates | Read-only |
| Audit MCP | Append normalized tool calls, evidence references, decisions, and approvals | Append-only |

Write-capable infrastructure tools are deliberately out of scope for the first release.

## Design principles

1. **Deterministic controls outrank model opinion.** The LLM explains and synthesizes; code performs schema validation, authorization, risk calculations, and policy checks.
2. **Evidence is mandatory.** Findings identify the tool result and evidence object on which they rely.
3. **Least privilege is the default.** Tools receive narrowly scoped identities and expose the minimum data required for a review.
4. **Retrieved content is untrusted.** Documents, logs, and tool output may contain malicious instructions and are treated as data, never as authority.
5. **Humans remain accountable.** The system drafts recommendations; an authorized reviewer accepts, rejects, or modifies them.
6. **No silent actions.** Every tool call is attributable and represented in the audit record.
7. **Privacy is architectural.** Data minimization, synthetic demonstrations, local inference, redaction, and retention controls are built in.

## Example output

See [`examples/sample-review.md`](examples/sample-review.md) for the expected shape of a review. It intentionally includes:

- request scope;
- evidence inventory;
- deterministic control failures;
- model-assisted analysis;
- uncertainties and missing evidence;
- proposed safeguards;
- residual risk; and
- human decision.

## Security model

The working threat model covers:

- prompt injection in retrieved documents;
- tool poisoning and misleading tool descriptions;
- excessive tool permissions;
- confused-deputy and cross-user access;
- insecure tool chaining;
- sensitive-data disclosure;
- evidence tampering;
- model hallucination;
- denial of service; and
- supply-chain compromise.

Read [`docs/threat-model.md`](docs/threat-model.md) and [`SECURITY.md`](SECURITY.md) before implementing a connector.

## Repository map

```text
.
├── README.md
├── ROADMAP.md
├── SECURITY.md
├── CONTRIBUTING.md
├── docs/
│   ├── architecture.md
│   ├── governance-model.md
│   ├── threat-model.md
│   ├── demo-scenarios.md
│   └── adr/
├── schemas/
│   ├── review-request.schema.json
│   └── review-result.schema.json
└── examples/
    ├── review-request.json
    └── sample-review.md
```

Implementation directories will be added during Phase 1:

```text
orchestrator/
mcp-servers/network/
mcp-servers/security/
mcp-servers/governance/
synthetic-data/
tests/
evaluations/
```

## Current implementation\n\nThe first executable slice intentionally works without an LLM. `orchestrator.policy` evaluates the initial vendor-access controls, `ReviewStateMachine` constrains lifecycle transitions, and the audit/review snapshot schemas define the integrity contracts that later MCP services and the dashboard will consume.\n\nScenario 1 currently demonstrates deterministic failure of unconstrained vendor source access, missing MFA, missing logging, and an untreated high-risk destination vulnerability while separately passing owner and expiry checks.\n\nRun the validation suite with:\n\n```bash\npip install -e ".[dev]"\npytest -q\n```\n\n## Planned technology choices

- **Inference:** Ollama-hosted local model behind a model-neutral adapter
- **Protocol:** current MCP specification and official SDK
- **Implementation:** Python, using typed models and JSON Schema
- **Runtime isolation:** rootless containers with read-only filesystems where practical
- **Policy:** explicit allowlists plus deterministic authorization middleware
- **Observability:** structured JSON audit events with correlation IDs
- **Testing:** unit, integration, authorization, prompt-injection, and evaluation suites
- **Delivery:** Docker Compose for the demonstration environment and GitHub Actions for validation

Technology choices remain provisional until the Phase 0 architecture decisions are validated.

## Success criteria

The initial demonstration is successful when it can:

1. complete the same synthetic review repeatedly without unauthorized calls;
2. cite every material factual assertion to retrieved evidence;
3. detect seeded policy violations using deterministic checks;
4. identify missing evidence instead of inventing it;
5. refuse an injected instruction embedded in a retrieved document;
6. require a recorded human decision;
7. produce a complete, redacted audit trail; and
8. run locally from documented setup steps.

No accuracy or performance claims will be published until the evaluation suite produces reproducible results.

## Roadmap

See [`ROADMAP.md`](ROADMAP.md). The work deliberately starts with one polished workflow rather than a broad collection of shallow integrations.

## License

MIT. See [`LICENSE`](LICENSE).

## Disclaimer

This is a home-lab reference project. It is not legal advice, a compliance certification product, or an autonomous change-management system. Human reviewers remain responsible for decisions and production actions.
