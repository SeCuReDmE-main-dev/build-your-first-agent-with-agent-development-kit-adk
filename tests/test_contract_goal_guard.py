"""Offline safeguards for the contract-goal training agent."""

from __future__ import annotations

import unittest

from contract_goal_training.contracts import (
    ContractOpportunityAssessment,
    EvidenceRef,
    OpportunityStage,
    TARGET_DATE,
    validate_assessment,
)


def assessment(**overrides: object) -> ContractOpportunityAssessment:
    values: dict[str, object] = {
        "opportunity_id": "training-example-001",
        "stage": OpportunityStage.LEAD,
        "client_identity_status": "unverified",
        "budget_status": "unverified",
        "stated_value_usd": None,
        "meets_target_value": False,
        "scope_is_bounded": False,
        "fit_score": 40,
        "evidence": [
            EvidenceRef(
                locator="https://example.invalid/opportunity",
                observed_fact="A fictional training listing exists.",
                status="unverified",
            )
        ],
        "missing_evidence": ["buyer identity", "budget", "scope"],
        "risk_flags": ["identity_unverified"],
        "blocked_actions": ["submission", "private repository access"],
        "recommendation": "hold",
        "next_human_action": "Verify the buyer identity from a public source.",
    }
    values.update(overrides)
    return ContractOpportunityAssessment(**values)


class ContractGoalGuardTests(unittest.TestCase):
    def test_target_date_is_end_of_september(self) -> None:
        self.assertEqual(str(TARGET_DATE), "2026-09-30")

    def test_unverified_lead_remains_valid_as_a_lead(self) -> None:
        self.assertEqual(validate_assessment(assessment()), [])

    def test_value_claim_requires_numeric_threshold(self) -> None:
        item = assessment(meets_target_value=True, stated_value_usd=4_999)
        self.assertIn("Target value is below USD 5,000.", validate_assessment(item))

    def test_verified_stage_requires_identity_budget_and_scope(self) -> None:
        item = assessment(stage=OpportunityStage.VERIFIED_OPPORTUNITY)
        errors = validate_assessment(item)
        self.assertIn("A verified stage requires verified client identity.", errors)
        self.assertIn("A verified stage requires verified budget evidence.", errors)
        self.assertIn("A verified stage requires a bounded scope.", errors)

    def test_external_outcomes_cannot_be_inferred(self) -> None:
        item = assessment(
            stage=OpportunityStage.CONTRACT_SIGNED,
            client_identity_status="verified",
            budget_status="verified",
            stated_value_usd=5_000,
            meets_target_value=True,
            scope_is_bounded=True,
        )
        self.assertTrue(
            any("external proof" in error for error in validate_assessment(item))
        )

    def test_verified_opportunity_can_pass_with_complete_evidence(self) -> None:
        item = assessment(
            stage=OpportunityStage.VERIFIED_OPPORTUNITY,
            client_identity_status="verified",
            budget_status="verified",
            stated_value_usd=7_500,
            meets_target_value=True,
            scope_is_bounded=True,
            recommendation="qualify",
        )
        self.assertEqual(validate_assessment(item), [])


if __name__ == "__main__":
    unittest.main()
