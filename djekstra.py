'''
For given graph write dijkstra algoright to find shortest path
'''
import networkx as nx
import matplotlib.pyplot as plt
def viewGrpah(G):
    
    pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
    edgelist = G.edges()
    
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist, width=3)

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
def dijkstra(G,s,vNode=[]):
    minDict = {}
    vNode.append(s)
    nList = [n for n in G.neighbors(s)]
    is_subset = set(nList).issubset(set(vNode))
    if is_subset:
        return
    sc = nx.get_node_attributes(G,"cost")[s]
    for n in G.neighbors(s):
        if n not in vNode:
            nc = nx.get_node_attributes(G,"cost")[n]
            ec = nx.get_edge_attributes(G,'weight')[(s,n)]
            print(f"For edge:({s},{n}), weight = {ec}")
            print(f"For Node {n}, cost is {nc}")
            if nc > sc+ec:
                nc = sc+ec
                nx.set_node_attributes(G, nc, "cost")
            minDict[n] = nc

    s = min(minDict, key=minDict.get)
    dijkstra(G,s)
if __name__=="__main__":
    edge_list = [(0,1,4),(0,7,8),(1,2,8),(1,7,11),(7,6,1),(7,8,7),(2,3,7),(2,8,2),(2,5,4),(6,8,6),(6,5,2),(5,4,10),(5,3,14),(4,3,9)]
    node_list = [(0,{'cost':0}),(1,{'cost':float('inf')}),(2,{'cost':float('inf')}),(3,{'cost':float('inf')}),(4,{'cost':float('inf')}),(5,{'cost':float('inf')}),(6,{'cost':float('inf')}),(7,{'cost':float('inf')}),(8,{'cost':float('inf')})]
    G = nx.Graph()
    G.add_nodes_from(node_list)
    G.add_weighted_edges_from(edge_list)
    print(nx.get_node_attributes(G,"cost")[0])
    print(nx.get_edge_attributes(G,'weight')[(0,1)])
    dijkstra(G,0)
    viewGrpah(G)