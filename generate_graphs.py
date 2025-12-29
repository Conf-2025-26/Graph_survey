from pyvis.network import Network
import networkx as nx

def create_graph_A():
    G = nx.DiGraph()

    # Example nodes
    G.add_node("Perceivable", color="green")
    G.add_node("choose photo", color="yellow")
    G.add_node("app crashes", color="red")

    # Edges
    G.add_edge("Perceivable", "choose photo")
    G.add_edge("choose photo", "app crashes")

    net = Network(height="600px", width="100%", directed=True)
    net.from_nx(G)
    net.save_graph("static/graphA.html")

def create_graph_B():
    G = nx.DiGraph()

    G.add_node("Operable", color="green")
    G.add_node("upload slow", color="yellow")
    G.add_node("timeout error", color="red")

    G.add_edge("Operable", "upload slow")
    G.add_edge("upload slow", "timeout error")

    net = Network(height="600px", width="100%", directed=True)
    net.from_nx(G)
    net.save_graph("static/graphB.html")

if __name__ == "__main__":
    create_graph_A()
    create_graph_B()
