from collections import defaultdict
from typing import Dict, List
import random

# Build Markov chain transition probabilities
'''
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
'''

#higher order markov chain
def build_chain(sequence, order=2, alpha=0.1):
    counts = defaultdict(lambda: defaultdict(int))
    for i in range(len(sequence) - order):
        history = tuple(sequence[i:i+order])
        nxt = sequence[i+order]
        counts[history][nxt] += 1

    all_states = set(sequence)
    probs = {}
    for history, nxts in counts.items():
        total = sum(nxts.values()) + alpha * len(all_states)
        probs[history] = {
            s: (nxts.get(s, 0) + alpha) / total
            for s in all_states
        }
    return probs



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