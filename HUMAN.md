# Human learning path

Open `my_first_agent/agent.py` first. It contains the complete behavior of the first agent: its model, name, description, and instruction.

Then read `README.md` to understand how the environment, secret configuration, and local server fit around that small Python file.

The important lesson is the separation of responsibilities:

1. `agent.py` defines the agent.
2. `.env` grants local access to the model and stays private.
3. ADK loads the package and provides the local development interface.
4. A test conversation supplies evidence that the full path works.

When returning after an interruption, check the repository status before editing, reopen `agent.py`, and change only one concept at a time. Record what was observed separately from what is still expected.

Current next action: refresh or restart ADK Web if needed, then run one controlled mathematics conversation and record the prompt, observable response, model, and limitation without recording credentials.

## Identity milestone

The internal ADK name is now `math_tutor_agent`, while the Python entry-point variable remains `root_agent`. Its description tells another agent when delegation would be useful. Its instruction makes it a generic mathematics tutor for learners at any level, with particular strength in fractal geometry, neutrosophic mathematics, and applied plithogeny. It teaches step by step, defines symbols, uses worked examples, asks for missing information, and ends with one short comprehension check.

No personal book, research file, project data, or private Drive content is used by this agent. The current agent has no Drive or retrieval tool; its answers come from the configured model and the current conversation.

## Model stability note

The first local algebra and fractal-dimension tests worked, but later tests received temporary upstream `503 UNAVAILABLE` high-demand errors. A direct availability check confirmed that `gemini-3.1-flash-lite` responds now, so the agent uses that lighter model while learning the ADK mechanics.
