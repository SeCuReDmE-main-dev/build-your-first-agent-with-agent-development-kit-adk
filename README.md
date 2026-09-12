# Build Your First Agent with Agent Development Kit (ADK)

This repository records a clean, minimal implementation of the Google Skills course **Build Your First Agent with Agent Development Kit (ADK)**.

The goal is educational: keep the first agent small enough to inspect line by line while preserving a reproducible setup and a strict boundary around credentials.

## What is here

- `my_first_agent/agent.py`: the ADK root agent definition.
- `my_first_agent/__init__.py`: exposes the agent package to ADK.
- `.env.example`: documents the required environment variables without containing a real key.
- `requirements.txt`: pins the ADK version used during the course.
- `HUMAN.md`: a short reading path for a learner returning to the project.
- `AGENTS.md`: boundaries for coding agents working in this repository.
- `model_configuration_demo/`: two task-specific ADK profiles for factual
  extraction and creative ideation.
- `tests/test_model_configuration_profiles.py`: offline contract checks for the
  profile differences.
- `contract_goal_training/`: planning-enabled ADK exercise for evidence-based
  qualification of substantial contract opportunities.
- `docs/15-session-state-programmatic-control.md`: session-state lesson tying
  `output_key` to programmatic control, CCP packets, learner privacy, and the
  contract lifecycle.

## Local setup

Python 3.11 or newer is recommended.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example my_first_agent\.env
```

Replace the placeholder in `my_first_agent/.env` with a Google AI Studio API key. Never commit that file.

Start the local development interface:

```powershell
adk web --host 127.0.0.1 --port 8000 my_first_agent
```

Then open `http://127.0.0.1:8000`.

## Learning checkpoint

The first milestone is deliberately narrow: create one root agent, authenticate locally, and launch ADK Web. The transformation milestone turns it into a generic mathematics tutor with particular strength in fractal geometry, neutrosophic mathematics, and applied plithogeny. It separates the ADK entry-point variable (`root_agent`) from the internal agent name (`math_tutor_agent`), the routing description, and the behavioral instruction. Later experiments can add tools, source retrieval, sessions, memory, evaluation, and structured handoffs one concept at a time.

## Security boundary

This public repository contains no API key, private conversation, learner data, or local execution logs. The web interface binds to `127.0.0.1` for local study.

## Status

The agent scaffold, public import, and transformed mathematics-tutor identity have been verified locally. ADK loaded `math_tutor_agent`, and the first algebra and fractal-dimension tests answered correctly. After repeated upstream `503 UNAVAILABLE` high-demand responses on later tests, the model was moved to the lighter `gemini-3.1-flash-lite`, which responded successfully in a direct availability check. This is enough evidence for the course milestone; later reuse should retest once the model service is stable.

The model-configuration milestone adds a separate offline exercise showing how
temperature, output limits, sampling, safety thresholds, and model choice can be
bound to a task. It does not claim that either configured model is currently
available, cheaper, faster, or higher quality; those require a live controlled
comparison.

The planning milestone adds a bounded exercise tied to the September contract
goal. It separates lead, verification, proposal readiness, submission,
signature, and payment, while reserving every external action for the human.

The session-state milestone documents how ADK saves an agent's final response
under `session.state` with `output_key`. In this repository the concept is
shown through `contract_goal_training`: the structured assessment can be read
programmatically as a workflow value, while lifecycle promotion still depends
on evidence and deterministic validation.
