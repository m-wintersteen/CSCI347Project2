import csv
from itertools import islice
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def connected_component_subgraphs(G):
    for c in nx.connected_components(G):
        yield G.subgraph(c)

def slice_dataset():
    with open('dataset/amazon0302.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        nodes = []
        edge_list = []
        G = nx.Graph()


    # the total number of pairs = 1048575
    # we are using only 8000

        for row in islice(csvreader, 1047575, None):
        #for row in csvreader:

            fromNode = int(row[0])
            toNode = int(row[1])

            nodes.append(fromNode)
            nodes.append(toNode)

            edge = [fromNode, toNode]
            edge_list.append(edge)


        #return(edge_list)
        G.add_edges_from(edge_list)
        H = G.subgraph(nodes)
        nx.draw_networkx(H, with_labels=False)
        plt.show()
def randomreduce():
    with open('dataset/amazon0302.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        edge_list = []
        G = nx.Graph()
        
        for row in csvreader:
            fromNode = int(row[0])
            toNode = int(row[1])

            edge = [fromNode, toNode]
            edge_list.append(edge)


        #return(edge_list)
        G.add_edges_from(edge_list)
        for n in list(G.nodes):
            if random.randint(0,100) < 84:
                G.remove_node(n)
        return G


#print(slice_dataset())
#slice_dataset()
G = randomreduce()

Gc = max(connected_component_subgraphs(G), key=len)
file_name = "reduced_data/reduce_random.edgelist"
nx.write_edgelist(Gc, file_name)

#nx.draw_networkx(Gc, with_labels=False)
#plt.show()



