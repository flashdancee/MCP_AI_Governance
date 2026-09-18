# Contributing

This project values small, reviewable changes with explicit security reasoning.

## Before proposing a change

1. Read `SECURITY.md` and `docs/threat-model.md`.
2. Confirm the change uses synthetic data only.
3. Open an issue describing the problem, expected behaviour, trust-boundary impact, and test approach.

## Pull requests

A pull request should include:

- a concise problem statement;
- implementation or documentation changes;
- tests or a reason tests are not applicable;
- security and privacy impact;
- screenshots with synthetic data when UI behaviour changes; and
- updates to architecture decisions or the threat model when required.

## Commit hygiene

- Do not include generated secrets or environment files.
- Keep commits focused.
- Use clear messages describing why a change exists.
- Run formatting, schema validation, tests, and secret scanning before submitting.

## Scope

The first milestone is intentionally narrow. New integrations should not displace completion, testing, and documentation of the read-only vendor-access review.
