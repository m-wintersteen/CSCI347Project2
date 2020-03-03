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
    betweenness = {}
    for i in node_list:
        betweenness.update({i: Project2.getBC(edge_list, i)})
    betweenness = {k: v for k, v in sorted(betweenness.items(), key=lambda item: item[1])}
    return dict(list(betweenness.items())[0:10])


def top_closeness():
    closeness = {}
    for i in node_list:
        closeness.update({i: Project2.getCloseC(edge_list, i)})
    closeness = {k: v for k, v in sorted(closeness.items(), key=lambda item: item[1])}
    return dict(list(closeness.items())[0:10])


def top_eccentricity():
    eccentricity_dict = nx.eccentricity(G)
    maxium_value_dict = {}
    maxv = 0
    for i in range(10):
        for key, value in eccentricity_dict.items():
            if value > maxv:
                maxv = key
        maxium_value_dict.update({maxv: eccentricity_dict[maxv]})
    return maxium_value_dict


def top_eigenvector():
    eigenvector_dict = nx.eigenvector_centrality(G)
    maxium_value_dict = {}
    maxv = 0
    for i in range(10):
        for key, value in eigenvector_dict.items():
            if value > maxv:
                maxv = key
        maxium_value_dict.update({maxv: eigenvector_dict[maxv]})
    return maxium_value_dict

def top_pagerank():
    pagerank_dict = nx.pagerank(G)
    maxium_value_dict = {}
    maxv = 0
    for i in range(10):
        for key, value in pagerank_dict.items():
            if value > maxv:
                maxv = key
        maxium_value_dict.update({maxv: pagerank_dict[maxv]})
    return maxium_value_dict




if __name__ == "__main__":
    G = nx.Graph()
    edge_list = preprocessing.get_list_data_from_file()
    G.add_edges_from(edge_list)
    node_list = G.nodes()

    #visualize_Graph()

    # using our own functions
    top_betweeness_list = top_betweenness()
    print(top_betweeness_list)
    top_closeness_list = top_closeness()
    print(top_closeness_list)

    # using networkx functions
    top_eccentricity_dict = top_eccentricity()
    print(top_eccentricity_dict)
    top_eigenvector_dict = top_eigenvector()
    print(top_eigenvector_dict)
    top_pagerank_dict = top_pagerank()
    print(top_pagerank_dict)

    # clustering coef of top 5 betweenness centrality nodes
    clusteringC = []
    for i in top_betweeness_list:
        clusteringC.append(Project2.getVertClustC(edge_list, i))
    print(clusteringC)

    # clustering coef of top 5 betweenness centrality nodes
    clusteringC = []
    for i in top_closeness_list:
        clusteringC.append(Project2.getCloseC(edge_list, i))
    print(clusteringC)

    # find the cluster coefficient of the graph
    print(Project2.getGraphClustC(edge_list))

    # compute the average shortest path distance in the graph
    print(nx.average_shortest_path_length(G))
    print(Project2.getMeanShortPath(edge_list))








