# add these 3 lines at the very top:
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.preprocess import normalize_players
from src.similarity import cosine_similarity, top_k_similar

def test_cosine_identical_is_one():
    a = [0.2, 0.5, 0.8]
    assert abs(cosine_similarity(a, a) - 1.0) < 1e-9

def test_top_k_returns_list():
    players = [
        {"name": "A", "team": "X", "pts": 10, "reb": 5, "ast": 5},
        {"name": "B", "team": "Y", "pts": 20, "reb": 5, "ast": 5},
        {"name": "C", "team": "Z", "pts": 15, "reb": 7, "ast": 6},
    ]
    vecs = normalize_players(players)
    res = top_k_similar(vecs, "A", k=2)
    assert len(res) == 2
    assert res[0][0] in {"B", "C"}
