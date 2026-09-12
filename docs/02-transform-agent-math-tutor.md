# Milestone 2: transform the agent into a mathematics tutor

## Source

Google Skills, **Build Your First Agent with Agent Development Kit (ADK)**, exercise **Transform your agent**.

## Objective

Transform the generic starter agent into a reusable tutor for any learner. The tutor covers general mathematics and has particular strength in fractal geometry, neutrosophic mathematics, and applied plithogeny.

## Smallest code change

Only the public `Agent` import and the agent's `name`, `description`, and `instruction` changed at first. The required Python entry point remains `root_agent`. After one successful test and repeated temporary upstream `503 UNAVAILABLE` high-demand responses, the model was pinned from `gemini-flash-latest` to `gemini-2.0-flash` for a more stable learning session.

## Intended behavior

- adapt to the learner's level;
- explain one mathematical step at a time;
- define symbols before using them;
- use short worked examples when useful;
- request missing information instead of guessing;
- end with one comprehension question or practice step.

## Validation performed

- `python -m py_compile my_first_agent/agent.py` completed successfully.
- ADK loaded the package and identified the responding author as `math_tutor_agent`.
- The prompt `Solve 2x + 5 = 13 step by step.` returned the correct solution, including isolation of `2x`, division by `2`, and a check that `x = 4`.
- Two later fractal-dimension attempts reached the configured model, but both returned `503 UNAVAILABLE` because the model was experiencing high demand.

The identity and integration path are therefore observed. Response quality is partially verified for a simple algebra explanation and should be checked again after the pinned-model change.

## Limitation

This milestone configures identity and instructions only. It does not add document retrieval, Drive access, RAG, memory, tools, or source-grounded answers. Those capabilities require explicit later implementation and testing.

No personal book, research file, project data, or private Drive content is part of the agent, its repository, or its validation prompts.

## Next action

Refresh or restart ADK Web if needed, retry one controlled conversation, then record only the observable teaching behavior. Do not store credentials, private prompts, or raw model logs.
