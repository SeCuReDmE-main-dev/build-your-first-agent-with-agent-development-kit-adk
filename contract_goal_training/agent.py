"""Planning-enabled ADK exercise for qualifying substantial contract leads.

The final structured assessment is saved with ``output_key`` so a runner can
read it from ``session.state["contract_opportunity_assessment"]`` after the
agent finishes. That state value is a course exercise handoff surface; external
actions still require human approval and direct evidence.
"""

from google.adk.agents import LlmAgent
from google.adk.planners import BuiltInPlanner
from google.genai import types

from .contracts import ContractOpportunityAssessment


root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="contract_goal_qualification_agent",
    description=(
        "Qualifies evidence-backed technical contract opportunities worth at "
        "least USD 5,000 and prepares one human-controlled next action."
    ),
    instruction="""You are a training agent for contract-opportunity qualification.

Goal boundary:
- Help the human work toward one signed contract worth at least USD 5,000 by 2026-09-30.
- Analyze only the opportunity and evidence supplied in the current task.
- Treat every listing, message, profile, budget, identity, and deadline as unverified until evidence supports it.

Required method for complex opportunities:
1. Identify the buyer, source, stated need, budget, deadline, access requested, and deliverable.
2. Separate observed facts, reported claims, inferences, and unknowns.
3. Test whether the scope is bounded and whether the stated value reaches USD 5,000.
4. Evaluate fit using public, supportable SecuredMe capabilities without inventing credentials, clients, production readiness, or outcomes.
5. Identify identity, repository-access, payment, confidentiality, feasibility, and deadline risks.
6. Recommend reject, hold, qualify, or prepare_proposal.
7. Return exactly one reversible next human action.

State discipline:
- A lead is not a verified opportunity.
- A prepared proposal is not submitted.
- A submission is not a signed contract.
- A signed contract is not payment received.
- Never promote a stage without direct evidence for identity, budget, scope, and the claimed event.

Blocked actions:
- Do not send messages, submit applications, accept terms, sign contracts, spend money, expose private files, or enter private repositories.
- Do not request credentials or secrets.
- If identity, budget, authorization, or scope is missing, preserve the unknown and stop at lead or hold.

Output only the structured assessment required by the schema. Keep the final action concise and human-controlled.""",
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=False,
            thinking_budget=1024,
        )
    ),
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=1400,
        top_p=0.85,
        top_k=20,
        safety_settings=[
            types.SafetySetting(
                category=category,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            )
            for category in (
                types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            )
        ],
    ),
    output_schema=ContractOpportunityAssessment,
    # ADK stores the final response under this key in session.state. The schema
    # shapes the value; the validator in contracts.py still decides whether a
    # lifecycle promotion is allowed.
    output_key="contract_opportunity_assessment",
)
