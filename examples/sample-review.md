# Sample review — REV-2026-0001

> Fictional demonstration output. Not an authorization or production recommendation.

## Status

`REVISION_REQUIRED`

## Scope

Review the requested HTTPS and RDP access to two synthetic BAS servers for a 90-day vendor maintenance engagement.

## Evidence inventory

| Evidence | Source | Purpose |
|---|---|---|
| NET-001 | `network.get_change_request` | Proposed source, destination, services, owner, and expiry |
| NET-002 | `network.list_relevant_rules` | Existing zone policy and approved jump-host path |
| SEC-001 | `security.get_asset_context` | Asset criticality and management controls |
| SEC-002 | `security.list_vulnerabilities` | Open vulnerability affecting BAS-APP-02 |
| GOV-001 | `governance.get_policy_requirements` | Vendor access, MFA, logging, and expiry requirements |

## Deterministic findings

1. **HIGH — Source is not constrained.** The request specifies `any`, which violates the vendor-access source restriction. Evidence: `NET-001`, `GOV-001`.
2. **HIGH — MFA is not demonstrated.** Privileged remote access requires MFA. Evidence: `SEC-001`, `GOV-001`.
3. **HIGH — Vulnerable destination.** BAS-APP-02 has a high-risk management-service vulnerability without a documented safeguard. Evidence: `SEC-002`, `GOV-001`.
4. **MEDIUM — Session logging is absent.** The proposed path does not enable required session and firewall logging. Evidence: `NET-001`, `GOV-001`.
5. **PASS — Ownership and expiry are present.** The request names a service owner and a time-limited expiry. Evidence: `NET-001`.

## Assisted analysis

The approved jump-host pattern in `NET-002` provides a narrower alternative to direct vendor access. Routing the vendor through that gateway could centralize MFA, session logging, source validation, and automatic expiry while avoiding a broadly scoped rule.

This statement is an architectural recommendation, not a deterministic pass condition. The implementation team must confirm that the gateway supports the required vendor workflow.

## Missing evidence

- Named vendor source addresses
- Confirmation of MFA integration
- Remediation date or documented compensating control for BAS-APP-02
- Logging destination and retention period
- Confirmation that RDP is necessary rather than a more restricted support method

## Recommendation

Return the request for revision. Require the managed support gateway, approved vendor source addresses, MFA, least-privilege services, centralized logging, automatic expiry, and remediation or documented risk treatment for the affected server.

## Human decision

- **Decision:** Revision required
- **Decision-maker:** Synthetic security reviewer
- **Rationale:** Mandatory evidence and access controls are incomplete.
