import networkx as nx
import matplotlib.pyplot as plt

def viewGrpah(G):
        pos = nx.spring_layout(G, seed=7)
        nx.draw_networkx_nodes(G, pos, node_size=700)
        nx.draw_networkx_edges(G, pos , width=3, alpha=0.5, edge_color="b", style="dashed")
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels,font_size=10, font_family="sans-serif")
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

def djesktra(s,G):
    print([n for n in G.neighbors(s)])
    print(G.nodes[s]['cost'])
    

if __name__=="__main__":
    node_list = [(0,{"cost": 0}),(1,{"cost": float('inf')}),(2,{"cost": float('inf')}),(3,{"cost": float('inf')}),(4,{"cost": float('inf')}),(5,{"cost": float('inf')}),(6,{"cost": float('inf')}),(7,{"cost": float('inf')}),(8,{"cost": float('inf')})]
    edge_list = [(0,1,4),(1,2,8),(2,3,7),(0,7,8),(7,8,7),(7,6,1),(2,5,4),(2,8,2),(8,6,6),(3,5,14),(3,4,9),(5,4,10)]
    G = nx.Graph()
    G.add_nodes_from(node_list)
    G.add_weighted_edges_from(edge_list)
    djesktra(0,G)
