from __future__ import annotations
from typing import List, Dict
import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "players.json"

def load_players(path: Path = DATA_PATH) -> List[Dict]:
    """Load players from JSON. Each player must have name, team, pts, reb, ast."""
    with path.open("r", encoding="utf-8") as f:
        payload = json.load(f)
    players = payload.get("players", [])
    if not isinstance(players, list) or not players:
        raise ValueError("players.json must contain a non-empty 'players' list.")
    required = {"name", "team", "pts", "reb", "ast"}
    for p in players:
        missing = required - set(p.keys())
        if missing:
            raise ValueError(f"Player missing keys: {missing} -> {p}")
    return players

def find_player(players: List[Dict], name: str) -> Dict | None:
    name_lower = name.strip().lower()
    for p in players:
        if p["name"].lower() == name_lower:
            return p
    return None
