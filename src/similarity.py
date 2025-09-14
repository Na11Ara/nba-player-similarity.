from __future__ import annotations
from typing import Dict, List, Tuple
import math

Vector = List[float]

def cosine_similarity(a: Vector, b: Vector) -> float:
    dot = sum(x*y for x, y in zip(a, b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(y*y for y in b))
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot / (na * nb)

def top_k_similar(vectors: Dict[str, Vector], target: str, k: int = 5) -> List[Tuple[str, float]]:
    if target not in vectors:
        raise KeyError(f"Target player '{target}' not found.")
    tvec = vectors[target]
    scores: List[Tuple[str, float]] = []
    for name, vec in vectors.items():
        if name == target:
            continue
        scores.append((name, cosine_similarity(tvec, vec)))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:k]
