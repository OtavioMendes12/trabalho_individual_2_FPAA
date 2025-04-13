import networkx as nx
import matplotlib.pyplot as plt

def visualize(graph, path=None):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)

    if path:
        edge_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edge_path, edge_color='red', width=2)

    plt.title("Caminho Hamiltoniano" if path else "Grafo")
    plt.savefig("assets/hamiltonian_path.png")
    plt.show()

# Exemplo de uso
if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    path = [0, 1, 2, 3]  # Exemplo de caminho Hamiltoniano
    visualize(graph, path)
