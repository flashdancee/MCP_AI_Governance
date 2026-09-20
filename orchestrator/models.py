from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any


class ReviewState(str, Enum):
    RECEIVED = "RECEIVED"
    VALIDATED = "VALIDATED"
    EVIDENCE_COLLECTION = "EVIDENCE_COLLECTION"
    DETERMINISTIC_CHECKS = "DETERMINISTIC_CHECKS"
    ASSISTED_ANALYSIS = "ASSISTED_ANALYSIS"
    OUTPUT_VALIDATION = "OUTPUT_VALIDATION"
    AWAITING_HUMAN_DECISION = "AWAITING_HUMAN_DECISION"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    REVISION_REQUIRED = "REVISION_REQUIRED"
    FAILED_SAFE = "FAILED_SAFE"


class ControlResult(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    NOT_EVALUATED = "NOT_EVALUATED"


@dataclass(frozen=True)
class ControlFinding:
    control_id: str
    result: ControlResult
    severity: str
    statement: str
    evidence_ids: tuple[str, ...]
    details: dict[str, Any] | None = None
