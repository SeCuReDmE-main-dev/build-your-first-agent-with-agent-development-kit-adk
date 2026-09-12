"""Offline contract checks for the model configuration exercise."""

import unittest

from model_configuration_demo.agent import creative_agent, factual_agent
from model_configuration_demo.profiles import TaskKind, get_profile


class ModelConfigurationProfileTests(unittest.TestCase):
    def test_factual_profile_is_bounded_and_low_variance(self) -> None:
        profile = get_profile(TaskKind.FACT_EXTRACTION)

        self.assertEqual(profile.generation.temperature, 0.1)
        self.assertEqual(profile.generation.max_output_tokens, 500)
        self.assertEqual(len(profile.generation.safety_settings or []), 4)

    def test_creative_profile_establishes_a_distinct_baseline(self) -> None:
        factual = get_profile(TaskKind.FACT_EXTRACTION)
        creative = get_profile(TaskKind.CREATIVE_IDEATION)

        self.assertGreater(
            creative.generation.temperature,
            factual.generation.temperature,
        )
        self.assertGreater(
            creative.generation.max_output_tokens,
            factual.generation.max_output_tokens,
        )
        self.assertNotEqual(creative.model, factual.model)

    def test_agents_receive_the_declared_profiles(self) -> None:
        self.assertEqual(factual_agent.name, "bounded_fact_extractor")
        self.assertEqual(creative_agent.name, "bounded_idea_baseline")
        self.assertEqual(
            factual_agent.generate_content_config.temperature,
            get_profile(TaskKind.FACT_EXTRACTION).generation.temperature,
        )


if __name__ == "__main__":
    unittest.main()
