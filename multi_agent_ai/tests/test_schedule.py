import unittest
from agents.schedule_agent import ScheduleAgent

class TestScheduleAgent(unittest.TestCase):
    def test_add_event(self):
        agent = ScheduleAgent()
        self.assertIsNotNone(agent)
