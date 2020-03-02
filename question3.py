import preprocessing
import Project2
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# visualize our Graph
def visualize_Graph():
    nx.draw_networkx(G, with_labels=False, node_size=1)
    plt.show()


# top 10 by betweenness
def top_betweenness():
    betweenness = []
    for i in node_list
        print(i)
        betweenness.append(Project2.getBC(edge_list, i))
    print(type(betweenness))


if __name__ == "__main__":
    G = nx.Graph()
    edge_list = preprocessing.slice_dataset()
    G.add_edges_from(edge_list)
    node_list = G.nodes()


    #visualize_Graph()

    top_betweenness()
