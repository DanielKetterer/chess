import importlib.util
from pathlib import Path

MODULE = Path(__file__).parents[1] / "scripts" / "build_opening_explorer.py"
spec = importlib.util.spec_from_file_location("opening_builder", MODULE)
builder = importlib.util.module_from_spec(spec); spec.loader.exec_module(builder)


def test_san_replay_handles_common_opening_moves():
    board = builder.initial_board()
    assert builder.apply_san(board, "e4", True) == "e2e4"
    assert builder.apply_san(board, "e5", False) == "e7e5"
    assert builder.apply_san(board, "Nf3", True) == "g1f3"
    assert builder.apply_san(board, "Nc6", False) == "b8c6"
    assert board["f3"] == "N"


def test_build_keeps_only_book_path_and_first_deviation():
    data = builder.build()
    assert data["games"]
    for game in data["games"]:
        assert game["moves"]
        assert all(move["book"] for move in game["moves"][:-1])
        assert set(game["moves"][-1]["board"]).issubset({f+r for f in "abcdefgh" for r in "12345678"})
