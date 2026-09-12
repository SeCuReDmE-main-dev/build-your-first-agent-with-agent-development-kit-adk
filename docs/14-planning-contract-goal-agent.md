# Planning exercise — Contract goal agent

This Google ADK exercise combines structured instructions, structured output,
task-specific model configuration, and planning for a complex decision. It
qualifies opportunities toward a USD 5,000 target without taking external
action.

Read `contract_goal_training/contracts.py` before `agent.py`. The deterministic
validator protects lifecycle states independently of the model. The ADK layer
adds `BuiltInPlanner`, a bounded thinking budget, a low-variance generation
profile, a Pydantic output schema, and an `output_key`.

Run the offline checks:

```powershell
.\.venv311\Scripts\python.exe -m unittest discover -s tests -v
```

After separately verifying model availability, the course exercise can be
opened locally with:

```powershell
.\.venv311\Scripts\adk.exe web --host 127.0.0.1 --port 8000 contract_goal_training
```

That second command can call a cloud model and was not used for this milestone.
The Google model identifier is a course-time candidate. It is separate from the
future Codex Spark 5.3 High operator configured in the case-study repository.
