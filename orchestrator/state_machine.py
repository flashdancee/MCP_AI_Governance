from __future__ import annotations

from dataclasses import dataclass

from .models import ReviewState


_ALLOWED: dict[ReviewState, set[ReviewState]] = {
    ReviewState.RECEIVED: {ReviewState.VALIDATED, ReviewState.FAILED_SAFE},
    ReviewState.VALIDATED: {ReviewState.EVIDENCE_COLLECTION, ReviewState.FAILED_SAFE},
    ReviewState.EVIDENCE_COLLECTION: {ReviewState.DETERMINISTIC_CHECKS, ReviewState.FAILED_SAFE},
    ReviewState.DETERMINISTIC_CHECKS: {ReviewState.ASSISTED_ANALYSIS, ReviewState.AWAITING_HUMAN_DECISION, ReviewState.FAILED_SAFE},
    ReviewState.ASSISTED_ANALYSIS: {ReviewState.OUTPUT_VALIDATION, ReviewState.FAILED_SAFE},
    ReviewState.OUTPUT_VALIDATION: {ReviewState.AWAITING_HUMAN_DECISION, ReviewState.FAILED_SAFE},
    ReviewState.AWAITING_HUMAN_DECISION: {ReviewState.APPROVED, ReviewState.REJECTED, ReviewState.REVISION_REQUIRED, ReviewState.FAILED_SAFE},
    ReviewState.APPROVED: set(),
    ReviewState.REJECTED: set(),
    ReviewState.REVISION_REQUIRED: set(),
    ReviewState.FAILED_SAFE: set(),
}


@dataclass
class ReviewStateMachine:
    state: ReviewState = ReviewState.RECEIVED

    def transition(self, target: ReviewState) -> ReviewState:
        if target not in _ALLOWED[self.state]:
            raise ValueError(f"invalid review transition: {self.state.value} -> {target.value}")
        self.state = target
        return self.state

    def fail_safe(self) -> ReviewState:
        if self.state in {ReviewState.APPROVED, ReviewState.REJECTED, ReviewState.REVISION_REQUIRED, ReviewState.FAILED_SAFE}:
            raise ValueError(f"cannot fail-safe terminal review state: {self.state.value}")
        self.state = ReviewState.FAILED_SAFE
        return self.state
