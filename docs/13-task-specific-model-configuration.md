# Task-specific model configuration exercise

## Source and objective

This exercise applies the Google Skills lesson on strategic model selection and
`google.genai.types.GenerateContentConfig`. It demonstrates that extraction and
creative ideation should not silently share one model profile.

## Read the example

1. Open `model_configuration_demo/profiles.py`. The task classes, model choices,
   sampling controls, output bounds, and safety thresholds are visible together.
2. Open `model_configuration_demo/agent.py`. Each ADK agent receives the profile
   for its task.
3. Open `tests/test_model_configuration_profiles.py`. The offline checks prove
   that the two profiles remain materially different without calling Google.

Run the checks from the repository root:

```powershell
.\.venv311\Scripts\python.exe -m unittest discover -s tests -v
```

To inspect the factual agent in ADK Web after verifying that the configured model
is available to the account:

```powershell
.\.venv311\Scripts\adk.exe web --host 127.0.0.1 --port 8000 model_configuration_demo
```

This second command can make live model calls and is intentionally not part of
the offline validation.

## What the profiles mean

The factual profile uses low temperature, focused sampling, a shorter output
limit, and strict content thresholds. Those settings reduce variation; they do
not prove factual accuracy. The instruction and source evidence still define
what may be extracted.

The creative profile uses a more capable model as a quality-baseline candidate,
higher temperature, wider sampling, and a larger response budget. Its model ID
is a course-time configuration, not a promise of permanent availability or a
verified cost ratio.

The safe optimization sequence is: establish a quality baseline, define a small
evaluation set, try a faster or cheaper profile, and measure the quality gap.
Only then should the lower-cost profile replace the baseline.

## CCP connection

A future CCP can carry a compact `task_kind` and evaluation requirements. A
selector can resolve that stable contract to the full runtime profile. This
keeps repeated generation settings out of every handoff while preserving an
explicit, reviewable decision. CCP should not guess a task class from vague text
or silently fall back to another model.

## Limitation and next action

No cloud call, billing action, latency benchmark, or model-quality comparison was
performed. Next, build a fixed extraction-and-ideation evaluation set and record
quality, latency, and usage for each verified model candidate.
