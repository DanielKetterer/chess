import importlib.util
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parents[1]
spec = importlib.util.spec_from_file_location("puzzle_builder", ROOT / "scripts/build_puzzle_dataset.py")
builder = importlib.util.module_from_spec(spec); spec.loader.exec_module(builder)


def test_dataset_is_compact_and_has_required_fields(tmp_path):
    data = builder.build(ROOT / "puzzles.json")
    assert data["puzzles"]
    puzzle = data["puzzles"][0]
    assert {"id", "fen", "prompt", "expectedMove", "category", "dueAt", "attemptSummary"} <= puzzle.keys()
    assert "sacrifice" not in puzzle and "source_game" not in puzzle
    output = tmp_path / "data.js"
    subprocess.run(["python", str(ROOT / "scripts/build_puzzle_dataset.py"), "--source", str(ROOT / "puzzles.json"), "--output", str(output)], check=True)
    assert output.read_text().startswith("// Generated")


def test_browser_queue_matches_failed_due_unattempted_semantics():
    script = r'''const q=require('./docs/puzzle-queue.js');
const base={dueAt:null,attemptSummary:{status:'unattempted',lastAt:null}};
const ps=[{...base,id:'new'},{...base,id:'due',attemptSummary:{status:'solved_first_try',lastAt:'2026-01-01'}},{...base,id:'failed',attemptSummary:{status:'failed_repeatedly',lastAt:'2026-02-01'}},{...base,id:'future',dueAt:'2027-01-01',attemptSummary:{status:'solved_first_try',lastAt:'2026-03-01'}}];
console.log(JSON.stringify(q.order(ps,new Date('2026-08-01')).map(x=>x.id)));'''
    result = subprocess.run(["node", "-e", script], cwd=ROOT, text=True, capture_output=True, check=True)
    assert json.loads(result.stdout) == ["failed", "due", "new", "future"]


def test_fen_orientation_and_uci_san_grading():
    script = r'''const c=require('./docs/chess-core.js');
const w=c.parseFen('4k3/8/8/8/8/8/4P3/4K3 w - - 0 1');
const b=c.parseFen('4k3/8/8/8/8/8/4P3/4K3 b - - 0 1');
console.log(JSON.stringify([c.orientation('8/8/8/8/8/8/8/8 w - - 0 1'),c.orientation('8/8/8/8/8/8/8/8 b - - 0 1'),c.grade(w,'e2e4','e2e4','e4'),c.grade(w,'e4','e2e4','e4'),c.grade(b,'e2e4','e2e4','e4')]));'''
    result = subprocess.run(["node", "-e", script], cwd=ROOT, text=True, capture_output=True, check=True)
    white, black, uci, san, illegal = json.loads(result.stdout)
    assert (white, black) == ("white", "black")
    assert uci == {"legal": True, "correct": True}
    assert san == {"legal": True, "correct": True}
    assert illegal == {"legal": False, "correct": False}
