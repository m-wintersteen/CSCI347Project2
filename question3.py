import preprocessing
import Project2
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#visualize our Graph
def visualize_Graph():
    edge_list = preprocessing.slice_dataset()
    G = nx.Graph()
    G.add_edges_from(edge_list)
    nx.draw_networkx(G, with_labels=True, node_size=1)
    plt.show()

# top 10 by betweenness
def top_betweenness():
    Project2.getBC()




if __name__ == "__main__":
    visualize_Graph()
    #print(preprocessing.slice_dataset())

