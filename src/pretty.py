from __future__ import annotations
from typing import Iterable, Tuple

def print_similarity_table(target: str, rows: Iterable[Tuple[str, float]]) -> None:
    """
    rows: iterable of (player_name, similarity_score)
    """
    header = f"Most similar to {target}"
    print("\n" + header)
    print("-" * len(header))
    print(f"{'Rank':<5} {'Player':<25} {'Similarity':>10}")
    print("-" * 45)
    for i, (name, score) in enumerate(rows, start=1):
        print(f"{i:<5} {name:<25} {score:>10.3f}")
