# ADR 0003 — Audit is part of the enforcement plane

## Status

Accepted.

## Context

A model-facing or MCP-exposed audit tool could make logging appear optional: a workflow might complete a sensitive operation without first choosing to call the audit tool.

## Decision

Mandatory audit emission is implemented by the orchestrator/tool gateway, outside model discretion. Authorization decisions, denied calls, successful calls, tool results, deterministic policy results, integrity failures, model-analysis boundaries, and human decisions all generate audit events.

The audit store remains append-only. A future MCP interface may expose read-only audit queries, but model/tool execution cannot suppress required audit events.

If a mandatory audit event cannot be recorded, the review transitions to `FAILED_SAFE`.

## Consequences

- Audit coverage is an enforcement property rather than a prompt convention.
- Denied and failed actions remain observable.
- The audit pipeline becomes a critical dependency and must be tested for outage and integrity failure.
- A read-only dashboard can consume the same normalized event stream.
