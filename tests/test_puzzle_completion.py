import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from scripts.mark_puzzle_attempt import mark_attempt
from scripts.render_puzzle_md import attempts_of, due_at, status_of


class PuzzleCompletionTests(unittest.TestCase):
    def test_completed_attempt_is_solved_across_consumers(self):
        puzzle = {
            "fen_before": "8/8/8/8/8/8/4K3/7k w - - 0 1",
            "attempts": [],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "puzzles.json"
            path.write_text(json.dumps([puzzle]), encoding="utf-8")
            now = datetime(2026, 7, 25, tzinfo=timezone.utc)

            self.assertTrue(mark_attempt(path, puzzle["fen_before"], "Ke3", now=now))
            saved = json.loads(path.read_text(encoding="utf-8"))[0]

        expected = {"timestamp": "2026-07-25T00:00:00+00:00", "found": True, "move": "Ke3"}
        self.assertEqual(saved["attempts"], [expected])
        self.assertEqual(status_of(attempts_of(saved)), "solved_first_try")
        self.assertIsNotNone(due_at(attempts_of(saved)))
        self.assertNotIn("completed", saved)

    def test_incorrect_attempt_remains_unsolved(self):
        puzzle = {"fen": "8/8/8/8/8/8/4K3/7k w - - 0 1", "attempts": []}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "puzzles.json"
            path.write_text(json.dumps({"puzzles": [puzzle]}), encoding="utf-8")
            mark_attempt(path, puzzle["fen"], result="incorrect")
            saved = json.loads(path.read_text(encoding="utf-8"))["puzzles"][0]

        self.assertFalse(saved["attempts"][0]["found"])
        self.assertEqual(status_of(attempts_of(saved)), "solved_after_failure")

    def test_unknown_fen_does_not_rewrite_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "puzzles.json"
            path.write_text("[]\n", encoding="utf-8")
            self.assertFalse(mark_attempt(path, "missing"))
            self.assertEqual(path.read_text(encoding="utf-8"), "[]\n")


if __name__ == "__main__":
    unittest.main()
