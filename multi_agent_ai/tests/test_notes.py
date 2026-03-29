import unittest
from agents.notes_agent import NotesAgent

class TestNotesAgent(unittest.TestCase):
    def test_save_note(self):
        agent = NotesAgent()
        self.assertIsNotNone(agent)
