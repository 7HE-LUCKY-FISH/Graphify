from collections import defaultdict
from typing import Dict, List
import random

# Build Markov chain transition probabilities

def build_chain(
    sequence: List[str]
) -> Dict[str, Dict[str, float]]:
    transition_counts = defaultdict(lambda: defaultdict(int))

    for prev, nxt in zip(sequence, sequence[1:]):
        transition_counts[prev][nxt] += 1

    transition_probs = {}
    for state, next_states in transition_counts.items():
        total = sum(next_states.values())
        transition_probs[state] = {n: count / total for n, count in next_states.items()}

    return transition_probs


def predict_next(
    current_genre: str,
    transition_probs: Dict[str, Dict[str, float]]
) -> str:
    """
    Predicts the next genre given the current genre state.
    """
    probs = transition_probs.get(current_genre)
    if not probs:
        return random.choice(list(transition_probs.keys()))  # fallback

    choices, weights = zip(*probs.items())
    return random.choices(choices, weights=weights)[0]