import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from data_loader import load_players


def test_load_players_non_empty():
    players = load_players(Path(__file__).resolve().parents[1] / "data" / "players.json")
    assert isinstance(players, list)
    assert len(players) >= 3
    for p in players:
        for key in ("name", "team", "pts", "reb", "ast"):
            assert key in p
