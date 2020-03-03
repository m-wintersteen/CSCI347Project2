import preprocessing
import Project2
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# visualize our Graph
def visualize_Graph():
    nx.draw_networkx(G, with_labels=False, node_size=.9)
    plt.show()


# top 10 by betweenness
def top_betweenness():
    betweenness = {}
    for i in node_list:
        print(i)
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
    for i in range(10):
        maxv = 0
        for key, value in eccentricity_dict.items():
            if value > maxv:
                maxv = key
        maxium_value_dict.update({maxv: eccentricity_dict[maxv]})
        eccentricity_dict.pop(maxv)
    return maxium_value_dict


def top_eigenvector():
    eigenvector_dict = nx.eigenvector_centrality(G)
    maxium_value_dict = {}
    
    for i in range(10):
        maxv = 0
        for key, value in eigenvector_dict.items():
            if value > maxv:
                maxv = key
        maxium_value_dict.update({maxv: eigenvector_dict[maxv]})
        eigenvector_dict.pop(maxv)
    return maxium_value_dict

def top_pagerank():
    pagerank_dict = nx.pagerank(G)
    maxium_value_dict = {}
    
    for i in range(10):
        maxv = 0
        for key, value in pagerank_dict.items():
            if value > maxv:
                maxv = key
        maxium_value_dict.update({maxv: pagerank_dict[maxv]})
        pagerank_dict.pop(maxv)
    return maxium_value_dict




if __name__ == "__main__":
    G = nx.Graph()
    edge_list = preprocessing.get_list_data_from_file()
    G.add_edges_from(edge_list)
    node_list = G.nodes()

    #visualize_Graph()

    # using our own functions
    top_betweeness_list = top_betweenness()
    print("top_betweeness")
    print(top_betweeness_list)

    print("top_closeness")
    top_closeness_list = top_betweenness()
    print(top_closeness_list)

     using networkx functions
    top_eccentricity_dict = top_eccentricity()
    print("top_eccentricity")
    print(top_eccentricity_dict)
    top_eigenvector_dict = top_eigenvector()
    print("top_eigenvector")
    print(top_eigenvector_dict)
    top_pagerank_dict = top_pagerank()
    print("top_pagerank")
    print(top_pagerank_dict)


    #clustering coef of top 5 betweenness centrality nodes

    top_betweeness_list = [112648, 74251, 164876, 197137, 201234]
    clusteringC = []
    for i in top_betweeness_list:
        clusteringC.append(Project2.getCloseC(edge_list, i))
    print("clustering coefiecient of top betweenness nodes")
    print(clusteringC)

    top_closeness_list = [112648, 74251, 164876, 197137, 201234]
    # clustering coef of top 5 betweenness centrality nodes
    clusteringC = []
    for i in top_closeness_list:
        clusteringC.append(Project2.getCloseC(edge_list, i))
    print("clustering coefiecient of top closeness nodes")
    print(clusteringC)
    

    # find the cluster coefficient of the graph
    print("clustering coefficient of the graph")
    print(Project2.getGraphClustC(edge_list))

    # compute the average shortest path distance in the graph
    print("average shortest path distance in the graph")
    print(nx.average_shortest_path_length(G))

    

    # plot degree distribution
    

    



    f = np.asarray(nx.degree_histogram(G))/sum(np.asarray(nx.degree_histogram(G)))
    nx.degree_histogram(G)
    plt.show()
    plt.loglog(np.arange(len(nx.degree_histogram(G))), f, 'r.')
    plt.xlabel('k (degree)')
    plt.ylabel('log f(k) (proportion of nodes with degree k)')
    plt.show()
    
    degree = dict(nx.degree(G)).values()
    plt.loglog((degree), 'r.')
    plt.xlabel('node degree')
    plt.ylabel('avg clustering coef by each degree)')
    plt.show()
    








