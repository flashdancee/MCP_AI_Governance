from __future__ import annotations

from typing import Any

from .models import ControlFinding, ControlResult


def _finding(control_id: str, result: ControlResult, severity: str, statement: str, evidence_ids: tuple[str, ...], **details: Any) -> ControlFinding:
    return ControlFinding(
        control_id=control_id,
        result=result,
        severity=severity,
        statement=statement,
        evidence_ids=evidence_ids,
        details=details or None,
    )


def evaluate_vendor_access(request: dict[str, Any], context: dict[str, Any]) -> list[ControlFinding]:
    """Evaluate deterministic controls for the initial vendor-access workflow.

    This function deliberately contains no model calls. It converts explicit
    request/context facts into stable PASS/FAIL/NOT_EVALUATED control results.
    """
    findings: list[ControlFinding] = []
    access = request.get("requested_access", {})
    source = str(access.get("source", "")).strip().lower()

    findings.append(
        _finding(
            "NET-VENDOR-SOURCE-001",
            ControlResult.FAIL if source in {"", "any", "0.0.0.0/0", "::/0"} else ControlResult.PASS,
            "HIGH",
            "Vendor access source must be explicitly constrained.",
            ("NET-001", "GOV-001"),
            observed_source=source or None,
        )
    )

    mfa = context.get("mfa_confirmed")
    if mfa is None:
        mfa_result = ControlResult.NOT_EVALUATED
    else:
        mfa_result = ControlResult.PASS if bool(mfa) else ControlResult.FAIL
    findings.append(
        _finding(
            "IAM-VENDOR-MFA-001",
            mfa_result,
            "HIGH",
            "Privileged vendor access requires confirmed MFA.",
            ("SEC-001", "GOV-001"),
            mfa_confirmed=mfa,
        )
    )

    logging = context.get("logging_enabled")
    if logging is None:
        logging_result = ControlResult.NOT_EVALUATED
    else:
        logging_result = ControlResult.PASS if bool(logging) else ControlResult.FAIL
    findings.append(
        _finding(
            "LOG-VENDOR-001",
            logging_result,
            "MEDIUM",
            "Vendor sessions and firewall activity must be logged.",
            ("NET-001", "GOV-001"),
            logging_enabled=logging,
        )
    )

    owner_present = bool(request.get("owner", {}).get("id"))
    findings.append(
        _finding(
            "GOV-OWNER-001",
            ControlResult.PASS if owner_present else ControlResult.FAIL,
            "HIGH",
            "The request must identify an accountable service owner.",
            ("NET-001",),
        )
    )

    expiry_present = bool(request.get("expires_at"))
    findings.append(
        _finding(
            "GOV-EXPIRY-001",
            ControlResult.PASS if expiry_present else ControlResult.FAIL,
            "HIGH",
            "Vendor access must be time-bound.",
            ("NET-001", "GOV-001"),
        )
    )

    vulnerable_assets = context.get("unmitigated_high_risk_assets")
    if vulnerable_assets is None:
        vuln_result = ControlResult.NOT_EVALUATED
        assets: list[str] = []
    else:
        assets = list(vulnerable_assets)
        vuln_result = ControlResult.FAIL if assets else ControlResult.PASS
    findings.append(
        _finding(
            "VULN-VENDOR-001",
            vuln_result,
            "HIGH",
            "High-risk destination vulnerabilities require remediation or a documented safeguard.",
            ("SEC-002", "GOV-001"),
            affected_assets=assets,
        )
    )
    return findings


def blocking_failures(findings: list[ControlFinding]) -> list[ControlFinding]:
    return [finding for finding in findings if finding.result == ControlResult.FAIL and finding.severity in {"HIGH", "CRITICAL"}]
