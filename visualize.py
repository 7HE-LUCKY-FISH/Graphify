import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, Optional, Tuple, Union
import matplotlib
import math
import random
from collections import defaultdict

matplotlib.use('TkAgg')

def project_to_first_order(higher_order_probs):
    """
    Projects a higher-order Markov chain to a first-order representation for visualization.
    """
    first_order = defaultdict(lambda: defaultdict(float))
    
    for history, transitions in higher_order_probs.items():
        src = history[-1] if isinstance(history, tuple) else history
        
        for dst, prob in transitions.items():
            first_order[src][dst] += prob
    
    # noramlization
    for src, transitions in first_order.items():
        total = sum(transitions.values())
        if total > 0:
            for dst in transitions:
                first_order[src][dst] /= total
    return {k: dict(v) for k, v in first_order.items()}




def draw_chain(
    transition_probs: Dict[Union[str, Tuple[str, ...]], Dict[str, float]],
    figsize: tuple = (16, 9),
    predicted_genre: Optional[str] = None,
    current_genre: Optional[str] = None
) -> None:
    
    transition_probs = project_to_first_order(transition_probs)
    
    filtered_probs = {}
    for src, dests in transition_probs.items():
        if src == "unknown" or (isinstance(src, tuple) and "unknown" in src):
            continue
        filtered_dests = {dst: p for dst, p in dests.items() 
                         if p > 0.05 and dst != "unknown"}
        if filtered_dests:
            filtered_probs[src] = filtered_dests

    G = nx.DiGraph()
    for src, dests in filtered_probs.items():  
        for dst, p in dests.items():
            G.add_edge(src, dst, weight=p)

    num_nodes = len(G.nodes())
    k_value = 3.45 / (num_nodes ** 0.5)
    pos = nx.spring_layout(G, scale= 1.5, seed=30, k=k_value, iterations=200)

    node_sizes = [1000 + 200 * G.degree(node) for node in G.nodes()]
    
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=figsize, facecolor='#f5f5f5')
    plt.title("Genre Transition Markov Chain")
    
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='lightblue', alpha=0.7, edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', font_weight='bold')
    
    widths = [max(1, 3 * w) for w in edge_labels.values()]
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=10, width=widths, edge_color='gray', alpha=0.5, min_source_margin= 20, min_target_margin=20)
    nx.draw_networkx_edge_labels(
        G, pos,
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
        manager.toolbar.pan() 

    plt.tight_layout()
    plt.show()
