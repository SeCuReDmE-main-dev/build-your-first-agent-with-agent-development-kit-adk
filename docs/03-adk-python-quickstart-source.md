# Source: ADK Python Quickstart

Source: https://adk.dev/get-started/python/  
Publisher: Agent Development Kit documentation  
Observed: 2026-09-12  
Classification: primary technical documentation / Python quickstart

## What this source establishes

The quickstart defines the minimum Python path for an ADK agent: Python 3.10 or later, `pip`, a recommended virtual environment, `google-adk`, an agent package containing `agent.py` and `__init__.py`, a `root_agent`, local credentials in `.env`, and local execution through `adk run` or `adk web`. It states that ADK Web is a development and debugging interface rather than a production deployment surface.

Our repository follows this structure. It uses Python 3.11, an isolated environment, a `root_agent`, a secret-safe `.env`, and a local web server bound to `127.0.0.1`.

## Version-sensitive observation

The quickstart page observed on 2026-09-12 shows `from google.adk.agents.llm_agent import Agent`. The Google Skills exercise for the current course warns against relying on that private module path and recommends the public import `from google.adk.agents import Agent`. This repository follows the course's public import. Recheck both primary sources when upgrading ADK.

## What this source does not establish

Completing the quickstart does not demonstrate production readiness, deployment, persistent memory, RAG, context caching, tools, multi-agent orchestration, or response quality.
