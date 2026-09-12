# Session state and programmatic control

Date: 2026-09-12  
Source lesson: Google Skills ADK, Manage Agent Memory and State, Module 01  
Repository role: local course exercise documentation

## Why this matters

Conversation history helps the model answer coherently, but application code
cannot safely route a workflow by rereading prose. Session state gives the code
a dictionary of exact values:

```python
value = session.state.get("key", default)
```

The ADK shortcut is `output_key`. When an `LlmAgent` sets
`output_key="topic"`, ADK stores the agent's final response under
`session.state["topic"]`. That value can then drive a later step without asking
another model to reinterpret the transcript.

## Where this repository shows the pattern

`contract_goal_training/agent.py` uses:

```python
output_key="contract_opportunity_assessment"
```

After a runner call, the course pattern is to inspect:

```python
assessment = session.state.get("contract_opportunity_assessment")
```

The important boundary is that session state stores a workflow value; it does
not prove the value is true. This exercise therefore pairs the ADK handoff
primitive with:

- `ContractOpportunityAssessment`, a structured Pydantic output contract;
- `OpportunityStage`, an explicit domain lifecycle;
- `validate_assessment(...)`, deterministic contradiction checks;
- blocked actions that keep outreach, submission, signature, and payment under
  human control.

## State surfaces

| Surface | Purpose in this exercise |
|---|---|
| Conversation history | Gives the model the current task wording and supplied evidence. |
| Session state | Lets code retrieve the final assessment by key after the run. |
| Domain lifecycle state | Classifies the opportunity as lead, verified, proposal-ready, submitted, signed, paid, or rejected. |
| Evidence artifacts | Public URLs or local identifiers listed inside the assessment. |
| Long-term memory | Out of scope for this repository; future use would need consent, retention, and provenance rules. |

## CCP transfer

For a Context Continuity Package, this distinction is the useful lesson:

- keep invariant instructions and schemas stable;
- pass the current workflow state as small typed values;
- reference evidence by locator instead of copying every source into the prompt;
- leave raw conversation history for human continuity or compact summaries;
- require explicit proof before lifecycle promotion.

This is especially important for a contract workflow. A transcript may suggest
that a proposal was prepared, but the state transition should still require a
typed value, evidence, and validation.

## Learner privacy note

The same design protects future education companions. A session can store the
current activity, quiz result, or next learning action without turning every
student phrase into durable memory. Long-term memory should be rarer, consented,
correctable, and supported by evidence.

## Validation

This documentation change does not require a live model call. The relevant
offline guard remains:

```powershell
.\.venv311\Scripts\python.exe -m unittest discover -s tests -v
```

That command checks the local structured contracts and profile boundaries
without spending tokens or reading secrets.
