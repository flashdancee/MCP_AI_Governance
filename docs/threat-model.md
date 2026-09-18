# Threat model

## Assets

- Review requests and business context
- Network and security evidence
- Governance policies and risk criteria
- Tool credentials and authorization context
- Model prompts and responses
- Human decisions and risk acceptance
- Audit records and integrity metadata
- Source code, dependencies, and container images

## Security objectives

- Only authorized actors can request or approve reviews.
- Tools cannot access data outside the current identity and review scope.
- Retrieved content cannot redefine system authority.
- Findings remain traceable to authentic evidence.
- Sensitive data is minimized and does not leak through prompts, output, or logs.
- The system fails safely when evidence, authorization, or integrity checks fail.

## Primary threats and controls

| Threat | Example | Planned controls |
|---|---|---|
| Prompt injection | A policy document says to ignore instructions and call another tool | Delimit retrieved content, treat it as data, isolate instructions, scan fixtures, enforce calls outside the model |
| Tool poisoning | A malicious server advertises a trusted-looking tool | Static registry, pinned server identity, signed manifests where practical, allowlists, review of tool-description changes |
| Excessive permissions | Network service can modify rules although review is read-only | Dedicated read-only identity, no write endpoint, deny-by-default policy, authorization tests |
| Insecure tool chaining | Asset data is fetched then sent to an unrelated external service | No generic egress tool, per-workflow allowlist, information-flow checks, local inference |
| Confused deputy | User causes the orchestrator to access another review or tenant | Actor-bound tokens, audience validation, resource scoping, per-request context |
| Data disclosure | Secrets or PII enter prompts or audit logs | Synthetic data, ingestion scanning, redaction, sensitivity labels, minimum context, no telemetry by default |
| Evidence tampering | A fixture changes after a recommendation | Content hashes, immutable review snapshot, provenance fields, integrity check before approval |
| Hallucination | Model invents a firewall rule or policy requirement | Required evidence IDs, schema validation, unsupported-assertion checks, human review |
| Replay | An old approval is applied to a changed request | Nonce/correlation ID, request and evidence hashes, expiry, approval bound to exact review version |
| Denial of service | Huge tool results exhaust model or host | Size limits, pagination, timeouts, quotas, bounded retries, circuit breakers |
| Supply-chain compromise | Malicious dependency or container image | Pinned dependencies, SBOM, vulnerability scanning, minimal images, dependency review |
| Audit bypass | Failed calls or denied actions are not recorded | Central audit middleware, append-only events, completeness tests, fail closed if mandatory logging fails |

## Abuse cases to test

1. Policy text instructs the model to approve the request.
2. Asset description asks the model to reveal its system prompt.
3. User requests all firewall rules rather than rules relevant to the review.
4. A lookalike tool uses a Unicode character in its name.
5. A read-only review attempts to invoke a future write tool.
6. Evidence changes after analysis but before approval.
7. User references another review's correlation ID.
8. Tool result contains a credential-shaped string.
9. Model cites a nonexistent evidence identifier.
10. Audit service is unavailable during a tool call.

## Residual risks

- Model behaviour cannot be made perfectly deterministic.
- Human reviewers may over-trust polished output.
- Local operation reduces but does not eliminate privacy and supply-chain risks.
- A compromised host can undermine service isolation and audit integrity.
- Synthetic demonstrations do not prove fitness for production or regulated use.

These risks must remain visible in the interface and project documentation.
