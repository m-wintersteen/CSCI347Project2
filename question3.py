import preprocessing
import Project2
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# visualize our Graph
def visualize_Graph():
    nx.draw_networkx(G, with_labels=False, node_size=.8)
    plt.show()


# top 10 by betweenness
def top_betweenness():
    betweenness = []
    for i in node_list:
        betweenness.append(Project2.getBC(edge_list, i))
    betweenness.sort()
    return betweenness[:10]


def top_closeness():
    closeness = []
    for i in node_list:
        closeness.append(Project2.getCloseC(edge_list, i))
    closeness.sort()
    return closeness[:10]


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
    edge_list = preprocessing.get_list_data_from_file()
    G.add_edges_from(edge_list)
    node_list = G.nodes()

    visualize_Graph()

    # using our own functions
    top_betweeness_list = top_betweenness()
    top_closeness_list = top_betweenness()

    # using networkx functions
    top_eccentricity_dict = top_eccentricity()
    top_eigenvector_dict = top_eigenvector()
    top_pagerank_dict = top_pagerank()

    # clustering coef of top 5 betweenness centrality nodes
    clusteringC = []
    for i in top_betweeness_list:
        clusteringC.append(Project2.getVertClustC(G, i))

    # clustering coef of top 5 betweenness centrality nodes
    clusteringC = []
    for i in top_closeness_list:
        clusteringC.append(Project2.getCloseC(G, i))

    # find the cluster coefficient of the graph
    Project2.getGraphClustC()

    # compute the average shortest path distance in the graph
    nx.average_shortest_path_length(G)








