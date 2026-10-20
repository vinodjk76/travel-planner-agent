import os
import unittest
from unittest.mock import MagicMock, patch

# Import the new class layout from your source directory
from src.agent import TravelPlannerCrew


class TestTravelPlannerCrewYAML(unittest.TestCase):

    def setUp(self):
        """Set up dynamic dictionary inputs representing user selections."""
        self.inputs = {
            "destination": "Tokyo, Japan",
            "days": 5,
            "budget": 2000.0,
            "interests": "food, anime, history"
        }
        
    def test_yaml_paths_exist(self):
        """Ensure the agent setup class accurately loads valid configuration dictionaries."""
        crew_instance = TravelPlannerCrew()
        
        # CrewAI parses the configuration files into dictionaries behind the scenes.
        # We assert that they are dictionaries and contain our expected agent/task keys.
        self.assertIsInstance(crew_instance.agents_config, dict, "agents_config failed to parse into a dictionary")
        self.assertIsInstance(crew_instance.tasks_config, dict, "tasks_config failed to parse into a dictionary")
        
        # Verify specific structural keys are present inside the loaded configurations
        self.assertIn("destination_researcher", crew_instance.agents_config)
        self.assertIn("research_task", crew_instance.tasks_config)

    @patch("src.agent.ChatOpenAI")
    @patch("src.agent.Crew")
    def test_crew_instantiation_maps_decorators(self, mock_crew, mock_chat_openai):
        """Verify agents and tasks register smoothly from YAML dictionary selectors."""
        # Arrange
        crew_instance = TravelPlannerCrew()

        # Act
        assembled_crew = crew_instance.crew()

        # Assert: Verify CrewAI decorators generated internal attributes dynamically
        self.assertIsNotNone(assembled_crew)
        self.assertEqual(len(crew_instance.agents), 3)
        self.assertEqual(len(crew_instance.tasks), 3)

    @patch("src.agent.ChatOpenAI")
    @patch("src.agent.Crew")
    def test_kickoff_receives_input_context(self, mock_crew, mock_chat_openai):
        """Ensure input tokens parse cleanly during crew workflow invocation."""
        # Arrange
        mock_crew_instance = MagicMock()
        mock_crew.return_value = mock_crew_instance
        
        # Simulate CrewAI's output class structure
        expected_raw_output = "Day 1 Itinerary..."
        mock_crew_instance.kickoff.return_value.raw = expected_raw_output

        # Act
        crew_instance = TravelPlannerCrew()
        result = crew_instance.crew().kickoff(inputs=self.inputs)

        # Assert: Check that input objects passed cleanly to the workflow execution engine
        mock_crew_instance.kickoff.assert_called_once_with(inputs=self.inputs)
        self.assertEqual(result.raw, expected_raw_output)


if __name__ == "__main__":
    unittest.main()
