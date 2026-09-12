"""Two ADK agents that make task-specific model configuration visible."""

from google.adk.agents import LlmAgent

from .profiles import TaskKind, get_profile


factual_profile = get_profile(TaskKind.FACT_EXTRACTION)
creative_profile = get_profile(TaskKind.CREATIVE_IDEATION)

factual_agent = LlmAgent(
    model=factual_profile.model,
    name="bounded_fact_extractor",
    description=factual_profile.purpose,
    instruction=(
        "Extract only facts explicitly stated in the supplied text. "
        "Do not infer, embellish, or add outside knowledge. Return a short "
        "bullet list and mark missing requested fields as not provided."
    ),
    generate_content_config=factual_profile.generation,
)

creative_agent = LlmAgent(
    model=creative_profile.model,
    name="bounded_idea_baseline",
    description=creative_profile.purpose,
    instruction=(
        "Generate varied ideas for the bounded problem supplied by the user. "
        "Keep assumptions visible, avoid claims of validation, and finish with "
        "criteria that can be used to compare the ideas."
    ),
    generate_content_config=creative_profile.generation,
)

# ADK requires one root entry point. The comparison remains explicit: switch
# this reference only after choosing the task being tested.
root_agent = factual_agent
