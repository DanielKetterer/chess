import json

from blunder_report import parse_sidecar


def test_old_sidecar_backfills_accuracy_from_markdown(tmp_path):
    sidecar = tmp_path / "game.json"
    sidecar.write_text(json.dumps({
        "game_id": "game-1",
        "game_date": "2026.07.29",
        "white": "DanielKetterer",
        "black": "Opponent",
        "player_color": "white",
        "metrics": {"player_moves": 12},
        "errors": [],
    }), encoding="utf-8")
    sidecar.with_suffix(".md").write_text(
        "- Lichess accuracy: you 87.4%, opponent 91.2%\n",
        encoding="utf-8")

    record = parse_sidecar(sidecar, "DanielKetterer")

    assert record.metrics["player_accuracy"] == 87.4
    assert record.metrics["opponent_accuracy"] == 91.2


def test_sidecar_accuracy_takes_precedence_over_markdown(tmp_path):
    sidecar = tmp_path / "game.json"
    sidecar.write_text(json.dumps({
        "game_id": "game-1",
        "game_date": "2026.07.29",
        "white": "DanielKetterer",
        "black": "Opponent",
        "player_color": "white",
        "metrics": {"player_accuracy": 95.0, "opponent_accuracy": 90.0},
        "errors": [],
    }), encoding="utf-8")
    sidecar.with_suffix(".md").write_text(
        "- Lichess accuracy: you 1.0%, opponent 2.0%\n",
        encoding="utf-8")

    record = parse_sidecar(sidecar, "DanielKetterer")

    assert record.metrics["player_accuracy"] == 95.0
    assert record.metrics["opponent_accuracy"] == 90.0
