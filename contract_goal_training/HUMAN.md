# Human entry point — Contract goal exercise

This exercise turns the course lessons into a controlled opportunity assessor. It does not search, contact a buyer, submit a proposal, or sign anything.

Read in this order:

1. `contracts.py` for the lifecycle states and deterministic contradiction checks.
2. `agent.py` for the instruction, planner budget, model profile, safety settings, structured output, and blocked actions.
3. `tests/test_contract_goal_agent.py` for the behaviors protected without a model call.

The monthly outcome is one signed contract with a stated value of at least USD 5,000 by 2026-09-30. The agent can only move an item from vague lead toward proposal preparation. The human verifies identity and evidence, approves every external communication, accepts terms, and records a signature or payment only from direct proof.

The configured Gemini model is a course-time candidate. Codex Spark 5.3 High is reserved for the future Codex operator and is not represented as an ADK runtime capability. No Spark run or live model comparison was performed here.

Next action: evaluate one current, publicly verifiable opportunity through the schema, then inspect every contradiction before drafting anything.
