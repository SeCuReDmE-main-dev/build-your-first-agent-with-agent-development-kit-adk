# Human learning path

Open `my_first_agent/agent.py` first. It contains the complete behavior of the first agent: its model, name, description, and instruction.

Then read `README.md` to understand how the environment, secret configuration, and local server fit around that small Python file.

The important lesson is the separation of responsibilities:

1. `agent.py` defines the agent.
2. `.env` grants local access to the model and stays private.
3. ADK loads the package and provides the local development interface.
4. A test conversation supplies evidence that the full path works.

When returning after an interruption, check the repository status before editing, reopen `agent.py`, and change only one concept at a time. Record what was observed separately from what is still expected.

Current next action: continue the course. This milestone has enough evidence: two teaching prompts worked, and later failures were upstream `503` model saturation.

## Model configuration milestone

For the next lesson, open `docs/13-task-specific-model-configuration.md`, then
compare `model_configuration_demo/profiles.py` with
`model_configuration_demo/agent.py`. The first file answers “which controls fit
this task?” and the second answers “which agent receives that profile?”

The factual and creative profiles are deliberately different. Their offline
tests do not spend tokens or require an API key. The configured model names are
candidates to verify before a live run, and safety filtering must not be confused
with factual accuracy.

## Planning and contract-goal milestone

Read `docs/14-planning-contract-goal-agent.md`, then compare
`contract_goal_training/contracts.py` and `agent.py`. The first file protects
evidence and lifecycle state; the second applies the Google ADK planning lesson.
This is the Google implementation exercise. The future Codex Spark operator is
configured separately in the case-study repository and has not been launched.

## Session-state milestone

Read `docs/15-session-state-programmatic-control.md` after the planning note.
The practical anchor is `output_key="contract_opportunity_assessment"` in
`contract_goal_training/agent.py`: ADK can save the agent's final response into
`session.state`, while `contracts.py` keeps lifecycle validation separate from
conversation history. This is documentation of the session-state pattern, not a
new production memory system.

## Identity milestone

The internal ADK name is now `math_tutor_agent`, while the Python entry-point variable remains `root_agent`. Its description tells another agent when delegation would be useful. Its instruction makes it a generic mathematics tutor for learners at any level, with particular strength in fractal geometry, neutrosophic mathematics, and applied plithogeny. It teaches step by step, defines symbols, uses worked examples, asks for missing information, and ends with one short comprehension check.

No personal book, research file, project data, or private Drive content is used by this agent. The current agent has no Drive or retrieval tool; its answers come from the configured model and the current conversation.

## Model stability note

The first local algebra and fractal-dimension tests worked, but later tests received temporary upstream `503 UNAVAILABLE` high-demand errors. A direct availability check confirmed that `gemini-3.1-flash-lite` responds now, so the agent uses that lighter model while learning the ADK mechanics.
