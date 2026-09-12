# Programmatic execution with Python - Colab trace

Date: 2026-09-12
Course: Google Skills, Build Your First Agent with Agent Development Kit (ADK)
Section: Other ways to run your agent - Three deployment methods
Method: 3, Programmatic execution with Python

## What was created

A Colab-ready notebook was created at:

`notebooks/2026-09-12-adk-programmatic-execution-colab.ipynb`

Drive copy:

- File ID: `1NigNH188jrV60hrULQGHSuk6XeZFfl3x`
- Folder ID: `1QS3RGByIz1Pz_EukSN6iu2kmSONx8imI`
- URL: `https://drive.google.com/file/d/1NigNH188jrV60hrULQGHSuk6XeZFfl3x/view?usp=drivesdk`

The notebook demonstrates how to run an ADK agent directly from Python code using:

- `Agent`
- `Runner`
- `InMemorySessionService`
- `Content`
- `Part`
- `await run_agent(...)`

## Why this matters

This method is the cleanest bridge between the course and SecuredMe Education experiments. `adk web` is useful for visual debugging, and `adk api_server` is useful for HTTP/API integration. Programmatic execution is useful when the educational flow itself is written in Python, such as a Colab, a research notebook, a data-processing pipeline, or a controlled proof of concept before implementing a side panel.

For the companion side-panel idea, the pattern is:

1. create or resume a session;
2. send a bounded learner message;
3. collect the final agent response;
4. decide what the learner sees next;
5. record only safe metadata and learning observations.

## Security boundary

The notebook does not contain an API key. It expects `GOOGLE_API_KEY` to be stored in Colab Secrets or in the runtime environment. It does not include private project data, learner data, personal research files, Drive documents, or `.env` content.

This notebook is not production infrastructure. It does not implement authentication, authorization, persistent session storage, logging policy, rate limiting, context caching, CCP, RAG, tools, or multi-agent orchestration.

## SecuredMe Education angle

The lesson is directly applicable to a future AlgoQuest or SecuredMe companion because it gives the application code control over session creation and agent invocation. This is a better mental model than treating the agent as only a chat window. A learning application can decide when the agent speaks, what context is allowed, and what next action is shown to the learner.

## Next step

Open the notebook in Colab, set `GOOGLE_API_KEY` as a Colab Secret, and run the cells once. Record only whether the install worked, whether the session was created, whether the agent returned a final response, and whether the response included a useful next learning step.
