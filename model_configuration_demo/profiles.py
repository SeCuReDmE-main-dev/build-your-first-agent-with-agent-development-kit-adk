"""Inspectable model profiles used by the configuration exercise.

Constructing these objects does not call a model or require credentials. Model
availability must still be verified before a live comparison.
"""

from dataclasses import dataclass
from enum import StrEnum

from google.genai import types


class TaskKind(StrEnum):
    """The bounded task classes demonstrated by this exercise."""

    FACT_EXTRACTION = "fact_extraction"
    CREATIVE_IDEATION = "creative_ideation"


@dataclass(frozen=True)
class ModelProfile:
    """A reviewable pairing of model choice and generation controls."""

    task_kind: TaskKind
    model: str
    purpose: str
    generation: types.GenerateContentConfig


def _safety_settings(
    threshold: types.HarmBlockThreshold,
) -> list[types.SafetySetting]:
    """Apply one explicit threshold to the four course safety categories."""

    return [
        types.SafetySetting(category=category, threshold=threshold)
        for category in (
            types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            types.HarmCategory.HARM_CATEGORY_HARASSMENT,
            types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        )
    ]


PROFILES: dict[TaskKind, ModelProfile] = {
    TaskKind.FACT_EXTRACTION: ModelProfile(
        task_kind=TaskKind.FACT_EXTRACTION,
        model="gemini-2.5-flash",
        purpose="Extract only facts present in the supplied text.",
        generation=types.GenerateContentConfig(
            temperature=0.1,
            max_output_tokens=500,
            top_p=0.8,
            top_k=10,
            safety_settings=_safety_settings(
                types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
            ),
        ),
    ),
    TaskKind.CREATIVE_IDEATION: ModelProfile(
        task_kind=TaskKind.CREATIVE_IDEATION,
        model="gemini-2.5-pro",
        purpose="Establish a quality baseline for bounded creative ideation.",
        generation=types.GenerateContentConfig(
            temperature=0.9,
            max_output_tokens=2000,
            top_p=0.95,
            top_k=40,
            safety_settings=_safety_settings(
                types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
        ),
    ),
}


def get_profile(task_kind: TaskKind) -> ModelProfile:
    """Return the declared profile for a task; no implicit fallback is used."""

    return PROFILES[task_kind]
