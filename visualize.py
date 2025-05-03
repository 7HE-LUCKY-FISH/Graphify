import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, Optional
import matplotlib
# Draw weighted directed graph of genres
matplotlib.use('TkAgg')

def draw_chain(
    transition_probs: Dict[str, Dict[str, float]],
    figsize: tuple = (16, 9),
    predicted_genre: Optional[str] = None,
    current_genre: Optional[str] = None
) -> None:
    
    filtere_prob = {}
    for src, dests in transition_probs.items():
        filtered_dests = {dst: p for dst, p in dests.items() if p > 0.05}
        if filtered_dests:
            filtere_prob[src] = filtered_dests

    G = nx.DiGraph()
    for src, dests in transition_probs.items():
        for dst, p in dests.items():
            G.add_edge(src, dst, weight=p)

    pos = nx.spring_layout(G, seed=42, k = 0.3)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=figsize, facecolor= '#f5f5f5')
    plt.title("Genre Transition Markov Chain")
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue', alpha=0.7, edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', font_weight='bold')
    widths = [5 * w for w in edge_labels.values()]
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=10, width=widths, edge_color='gray', alpha=0.5)
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels={k: f"{v:.2f}" for k, v in edge_labels.items()},
        font_size=8
    )
    plt.title("Genre-Transition Markov Chain")

    if predicted_genre:
        prediction_text = f"Predicted next genre: {predicted_genre}"
        if current_genre:
            prediction_text = f"Current genre: {current_genre}\n{prediction_text}"
        plt.figtext(0.98, 0.98, prediction_text, 
                   horizontalalignment='right', 
                   verticalalignment='top',
                   fontsize=12,
                   fontweight='bold',
                   bbox=dict(facecolor='white', alpha=0.8, edgecolor='black', boxstyle='round,pad=0.5'))

    plt.axis('off')

    manager = plt.get_current_fig_manager()
    if hasattr(manager, 'toolbar'):
        manager.toolbar.pan()  #

    plt.tight_layout()
    plt.show()
