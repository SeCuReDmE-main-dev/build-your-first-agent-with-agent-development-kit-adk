# Human learning path

Open `my_first_agent/agent.py` first. It contains the complete behavior of the first agent: its model, name, description, and instruction.

Then read `README.md` to understand how the environment, secret configuration, and local server fit around that small Python file.

The important lesson is the separation of responsibilities:

1. `agent.py` defines the agent.
2. `.env` grants local access to the model and stays private.
3. ADK loads the package and provides the local development interface.
4. A test conversation supplies evidence that the full path works.

When returning after an interruption, check the repository status before editing, reopen `agent.py`, and change only one concept at a time. Record what was observed separately from what is still expected.

Current next action: run one controlled conversation and record the prompt, observable response, model, and limitation without recording credentials.

## Identity milestone

The internal ADK name is now `learning_continuity_agent`, while the Python entry-point variable remains `root_agent`. Its description tells another agent when delegation would be useful. Its instruction tells this agent how to behave: explain plainly, connect the lesson to the learner's project, distinguish evidence from ideas, and finish with one next learning action.
