from __future__ import annotations
import argparse
from data_loader import load_players, find_player
from preprocess import normalize_players
from similarity import top_k_similar
from pretty import print_similarity_table

def run(name: str, k: int) -> None:
    players = load_players()
    # validate target exists (case-insensitive match)
    target = find_player(players, name)
    if not target:
        sample = ", ".join(p["name"] for p in players[:8])
        raise SystemExit(f"Player '{name}' not found. Try one of: {sample} ...")
    vectors = normalize_players(players)
    results = top_k_similar(vectors, target["name"], k=k)
    print_similarity_table(target["name"], results)

def main() -> None:
    parser = argparse.ArgumentParser(
        description="NBA Player Similarity (cosine on normalized pts/reb/ast)"
    )
    parser.add_argument("--name", required=True, help="Full player name, e.g. 'LeBron James'")
    parser.add_argument("--k", type=int, default=5, help="How many similar players to show")
    args = parser.parse_args()
    run(args.name, args.k)

if __name__ == "__main__":
    main()

