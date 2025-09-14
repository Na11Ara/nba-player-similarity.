from __future__ import annotations
from typing import Dict, List, Tuple

STAT_KEYS = ("pts", "reb", "ast")

def compute_min_max(players: List[Dict]) -> Dict[str, Tuple[float, float]]:
    mins_maxs: Dict[str, Tuple[float, float]] = {}
    for k in STAT_KEYS:
        vals = [float(p[k]) for p in players]
        mins_maxs[k] = (min(vals), max(vals))
    return mins_maxs

def normalize_players(players: List[Dict]) -> Dict[str, List[float]]:
    """
    Min-max normalize each stat to [0,1].
    Returns mapping: player_name -> vector [pts_norm, reb_norm, ast_norm]
    """
    mm = compute_min_max(players)
    norm: Dict[str, List[float]] = {}
    for p in players:
        vec = []
        for k in STAT_KEYS:
            lo, hi = mm[k]
            x = float(p[k])
            if hi == lo:
                vec.append(0.0)  # avoid div-by-zero if all same
            else:
                vec.append((x - lo) / (hi - lo))
        norm[p["name"]] = vec
    return norm
