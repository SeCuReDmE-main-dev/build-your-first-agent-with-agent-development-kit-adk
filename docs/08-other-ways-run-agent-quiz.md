# Other ways to run your agent - quiz trace

Date: 2026-09-12
Course: Google Skills, Build Your First Agent with Agent Development Kit (ADK)
Section: Other ways to run your agent - Three deployment methods
Quiz: Google Skills 649843
Observed score: 100%

## Questions and answers

Question 1: Which command should you use to quickly test your agent from the terminal without opening a browser?

Correct answer: `adk run`

Lesson: `adk run` is the lightest terminal path for quick tests and command-line workflows. It is useful when the developer wants to interact with the same agent without opening the browser UI.

Question 2: When would you use `adk api_server` instead of `adk web`?

Correct answer: When you need to integrate your agent into a web or mobile application.

Lesson: `adk api_server` exposes the agent through HTTP so another application can send requests. It is the local API integration path, while `adk web` is mainly for visual development, debugging, and demos.

## SecuredMe Education angle

This quiz confirms the three-mode mental model now used for the education suite:

- `adk web`: inspect and debug the agent visually;
- `adk run`: quick terminal checks;
- `adk api_server`: connect an interface, side panel, web app, or mobile backend to the agent.

For AlgoQuest or a SecuredMe companion, `adk api_server` is the method that maps most directly to a future side-panel integration. The app can own the learner interface while the agent runs behind an HTTP boundary. The method does not by itself solve production authentication, session persistence, rate limits, private data handling, or deployment.

## CCP and context-efficiency angle

The quiz also clarifies where a CCP would sit. `adk api_server` gives the transport path; the client still decides what context to send. A compact handoff can travel in the HTTP body or be attached to the session state, but this quiz does not prove context caching, memory, or token savings. Those need a separate experiment.

## Summary

The quiz was passed at 100%.
Use `adk run` for quick terminal tests.
Use `adk api_server` for web or mobile integration.
Use `adk web` for visual debugging and demos.
The next useful proof is a small side-panel-style HTTP call with a safe, minimal handoff.
