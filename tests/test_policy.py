import json
from pathlib import Path

from orchestrator.models import ControlResult
from orchestrator.policy import blocking_failures, evaluate_vendor_access


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def test_scenario_one_detects_seeded_failures():
    request = load_json("examples/review-request.json")
    context = load_json("synthetic-data/scenario-1/control-context.json")

    findings = evaluate_vendor_access(request, context)
    by_id = {finding.control_id: finding for finding in findings}

    assert by_id["NET-VENDOR-SOURCE-001"].result == ControlResult.FAIL
    assert by_id["IAM-VENDOR-MFA-001"].result == ControlResult.FAIL
    assert by_id["LOG-VENDOR-001"].result == ControlResult.FAIL
    assert by_id["GOV-OWNER-001"].result == ControlResult.PASS
    assert by_id["GOV-EXPIRY-001"].result == ControlResult.PASS
    assert by_id["VULN-VENDOR-001"].result == ControlResult.FAIL
    assert len(blocking_failures(findings)) == 3


def test_unknown_context_is_not_invented():
    request = load_json("examples/review-request.json")
    findings = evaluate_vendor_access(request, {})
    by_id = {finding.control_id: finding for finding in findings}

    assert by_id["IAM-VENDOR-MFA-001"].result == ControlResult.NOT_EVALUATED
    assert by_id["LOG-VENDOR-001"].result == ControlResult.NOT_EVALUATED
    assert by_id["VULN-VENDOR-001"].result == ControlResult.NOT_EVALUATED
