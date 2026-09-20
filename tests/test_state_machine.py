import pytest

from orchestrator.models import ReviewState
from orchestrator.state_machine import ReviewStateMachine


def test_happy_path_without_llm_is_supported():
    review = ReviewStateMachine()
    review.transition(ReviewState.VALIDATED)
    review.transition(ReviewState.EVIDENCE_COLLECTION)
    review.transition(ReviewState.DETERMINISTIC_CHECKS)
    review.transition(ReviewState.AWAITING_HUMAN_DECISION)
    assert review.state == ReviewState.AWAITING_HUMAN_DECISION


def test_invalid_transition_is_rejected():
    review = ReviewStateMachine()
    with pytest.raises(ValueError):
        review.transition(ReviewState.APPROVED)


def test_fail_safe_is_available_before_terminal_state():
    review = ReviewStateMachine()
    review.transition(ReviewState.VALIDATED)
    assert review.fail_safe() == ReviewState.FAILED_SAFE
