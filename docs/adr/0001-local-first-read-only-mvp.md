# ADR 0001: Local-first, read-only MVP

- **Status:** Accepted
- **Date:** 2026-09-18

## Context

The project is intended to demonstrate secure AI orchestration for infrastructure and governance reviews. Beginning with write-capable infrastructure tools would add operational risk without improving the core evidence, authorization, and audit demonstration.

## Decision

The MVP will:

- use a locally hosted model;
- use synthetic data;
- expose narrowly scoped read-only MCP tools;
- perform deterministic checks outside the model;
- require a human decision; and
- write only to an append-only audit interface.

## Consequences

The MVP cannot demonstrate automated remediation, but it can demonstrate the more important security properties: bounded authority, evidence provenance, refusal behaviour, auditability, and accountable decision-making.
