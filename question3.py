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
    for i in node_list:
        print(i)
        betweenness.append(Project2.getBC(edge_list, i))
    print(type(betweenness))


def top_eccentricity():
    eccentricity_dict = nx.eccentricity(G)
    maxium_value_dict = {}

    for i in range(10):
        for key, value in eccentricity_dict.items():
            if value > max:
                max = key
        maxium_value_dict.update({max: eccentricity_dict[max]})
    return maxium_value_dict


def top_eigenvector():
    eigenvector_dict = nx.eigenvector_centrality(G)
    maxium_value_dict = {}

    for i in range(10):
        for key, value in eigenvector_dict.items():
            if value > max:
                max = key
        maxium_value_dict.update({max: eigenvector_dict[max]})
    return maxium_value_dict

def top_pagerank():
    pagerank_dict = nx.pagerank(G)
    maxium_value_dict = {}

    for i in range(10):
        for key, value in pagerank_dict.items():
            if value > max:
                max = key
        maxium_value_dict.update({max: pagerank_dict[max]})
    return maxium_value_dict




if __name__ == "__main__":
    G = nx.Graph()
    edge_list = preprocessing.slice_dataset()
    G.add_edges_from(edge_list)
    node_list = G.nodes()

    visualize_Graph()

    top_betweenness()
