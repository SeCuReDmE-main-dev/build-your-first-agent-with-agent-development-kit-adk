# Two ways to define agents - YAML activity trace

Date: 2026-09-12
Course: Google Skills, Build Your First Agent with Agent Development Kit (ADK)
Section: Agent configuration with YAML - Two ways to define agents

## What was learned

ADK supports two first-class ways to define an agent:

- Python code with `agent.py`;
- YAML Agent Config with `root_agent.yaml`.

Both methods define the same core agent fields: `name`, `model`, `description`, and `instruction`. The difference is the authoring surface. Python is better when the agent needs custom tools, callbacks, programmatic control, and advanced multi-agent behavior. YAML is better when the agent is simple, collaborative, easy to review, and meant for quick configuration experiments.

## Exercise completed

A YAML-based exercise agent was created locally at:

`my_config_agent/root_agent.yaml`

The file now defines a Synthia handoff orientation agent, using readable YAML and a multiline `instruction: |` block. It is no longer a generic math tutor. Its purpose is to model how a future handoff to Codex/OpenAI or Antigravity/Gemini should preserve Synthia's public identity, source traceability, uncertainty boundaries, plithogenic/neutrosophic system context, and human-review authority boundary. A non-secret `.env.example` was also added for orientation. No real `.env` file or API key was copied.

## Synthia angle

This lesson is important for Synthia because of the architectural principle, not because Synthia must use Google ADK. The reusable idea is to separate a human-readable configuration layer from executable logic and runtime state while respecting Synthia's real public structure. Synthia is already an educational research system for context-preserving lexicon intelligence, biology classification, source traceability, taxonomy memory, and uncertainty-aware classification. A YAML or YAML-like surface is useful only if it preserves that identity instead of flattening Synthia into a generic assistant.

For Synthia, future surgery should consider:

- which stable role contracts, companion handoff rules, and source-boundary reminders belong in declarative configuration;
- which parts require executable code because they implement Synthia's real pipelines, tools, callbacks, WebMCP surfaces, document lane, or governance logic;
- how Codex/OpenAI and Antigravity/Gemini should receive Synthia handoffs without losing provenance or authority boundaries;
- how to keep `I -> I_system^S -> H_lex -> G_lex -> I_lexicon`, bounded T/I/F, plithogenic contradiction, rough regions, and review state visible;
- how to version behavior changes without mixing them with application logic or runtime session state.

## Limits

Agent Config is still described by ADK as experimental and has known limitations. The course states that Python remains necessary for complex multi-agent systems, custom tools, callbacks, and runtime behavior. This activity does not migrate Synthia, does not implement tools, and does not prove production readiness.

## Next action

When Synthia is analyzed, begin by mapping current behavior into three layers:

1. stable Synthia identity, public invariant, role contracts, handoff rules, source-boundary reminders, and companion persona constraints that could live in readable configuration;
2. real Synthia code that must remain executable logic: tools, callbacks, pipelines, CLI commands, WebMCP adapters, validation, plithogenic/neutrosophic kernels, and governance checks;
3. runtime state, sessions, memory, CCP handoff data, source packets, and temporary review outputs that should not be hardcoded in either.

Do not assume Google ADK is the target framework. Evaluate the pattern first, then decide whether Synthia should use its own configuration system, ADK Agent Config, or another mechanism.
