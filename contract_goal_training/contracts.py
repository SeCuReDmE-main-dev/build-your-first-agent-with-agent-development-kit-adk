"""Structured contracts for the USD 5,000 opportunity-qualification exercise.

These models classify evidence and recommendations. They do not submit a
proposal, accept a contract, access a private repository, or confirm payment.
The ``stage`` field is domain lifecycle state. ADK session state stores an
agent run's result separately when ``agent.py`` uses ``output_key``.
"""

from __future__ import annotations

from datetime import date
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


TARGET_VALUE_USD = 5_000
TARGET_DATE = date(2026, 9, 30)


class OpportunityStage(StrEnum):
    LEAD = "lead"
    VERIFIED_OPPORTUNITY = "verified_opportunity"
    PROPOSAL_READY = "proposal_ready"
    SUBMITTED = "submitted"
    CONTRACT_SIGNED = "contract_signed"
    PAYMENT_RECEIVED = "payment_received"
    REJECTED = "rejected"


class EvidenceRef(BaseModel):
    model_config = ConfigDict(extra="forbid")

    locator: str = Field(min_length=1, description="Public URL or local evidence identifier.")
    observed_fact: str = Field(min_length=1)
    status: Literal["observed", "reported", "unverified"]


class ContractOpportunityAssessment(BaseModel):
    """Machine-readable result for one bounded opportunity."""

    model_config = ConfigDict(extra="forbid")

    opportunity_id: str = Field(min_length=1)
    stage: OpportunityStage
    client_identity_status: Literal["verified", "partially_verified", "unverified"]
    budget_status: Literal["verified", "reported", "unverified"]
    stated_value_usd: float | None = Field(default=None, ge=0)
    meets_target_value: bool
    scope_is_bounded: bool
    fit_score: int = Field(ge=0, le=100)
    evidence: list[EvidenceRef] = Field(default_factory=list)
    missing_evidence: list[str] = Field(default_factory=list)
    risk_flags: list[str] = Field(default_factory=list)
    blocked_actions: list[str] = Field(default_factory=list)
    recommendation: Literal["reject", "hold", "qualify", "prepare_proposal"]
    next_human_action: str = Field(min_length=1)
    target_date: date = TARGET_DATE


def validate_assessment(assessment: ContractOpportunityAssessment) -> list[str]:
    """Return contradictions that must block promotion to a later stage."""

    errors: list[str] = []

    if assessment.meets_target_value:
        if assessment.stated_value_usd is None:
            errors.append("Target value cannot be met without a stated USD value.")
        elif assessment.stated_value_usd < TARGET_VALUE_USD:
            errors.append("Target value is below USD 5,000.")

    verified_stages = {
        OpportunityStage.VERIFIED_OPPORTUNITY,
        OpportunityStage.PROPOSAL_READY,
        OpportunityStage.SUBMITTED,
        OpportunityStage.CONTRACT_SIGNED,
        OpportunityStage.PAYMENT_RECEIVED,
    }
    if assessment.stage in verified_stages:
        if assessment.client_identity_status != "verified":
            errors.append("A verified stage requires verified client identity.")
        if assessment.budget_status != "verified":
            errors.append("A verified stage requires verified budget evidence.")
        if not assessment.scope_is_bounded:
            errors.append("A verified stage requires a bounded scope.")

    if assessment.stage in {
        OpportunityStage.SUBMITTED,
        OpportunityStage.CONTRACT_SIGNED,
        OpportunityStage.PAYMENT_RECEIVED,
    }:
        errors.append(
            "Submission, signature, and payment states require external proof and cannot be inferred by this agent."
        )

    if not assessment.evidence:
        errors.append("At least one evidence reference is required.")

    return errors
