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

The first milestone is deliberately narrow: create one root agent, authenticate locally, and launch ADK Web. The identity milestone then separates the ADK entry-point variable (`root_agent`) from the internal agent name (`learning_continuity_agent`), the routing description, and the behavioral instruction. Later experiments can add tools, sessions, memory, evaluation, and structured handoffs one concept at a time.

## Security boundary

This public repository contains no API key, private conversation, learner data, or local execution logs. The web interface binds to `127.0.0.1` for local study.

## Status

The agent scaffold and local ADK server have been verified. A controlled model-response test remains the next evidence checkpoint.
