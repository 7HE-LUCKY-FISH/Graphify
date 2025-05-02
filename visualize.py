import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict

# Draw weighted directed graph of genres

def draw_chain(
    transition_probs: Dict[str, Dict[str, float]],
    figsize: tuple = (10, 8)
) -> None:
    G = nx.DiGraph()
    for src, dests in transition_probs.items():
        for dst, p in dests.items():
            G.add_edge(src, dst, weight=p)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=figsize)
    nx.draw_networkx_nodes(G, pos, node_size=1200)
    nx.draw_networkx_labels(G, pos)
    widths = [5 * w for w in edge_labels.values()]
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=15, width=widths)
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels={k: f"{v:.2f}" for k, v in edge_labels.items()},
        font_size=8
    )
    plt.title("Genre-Transition Markov Chain")
    plt.axis('off')
    plt.show()
