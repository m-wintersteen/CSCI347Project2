import csv
from itertools import islice
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def connected_component_subgraphs(G):
    for c in nx.connected_components(G):
        print("subgraph")
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
def reduce():
    with open('dataset/amazon0302.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        nodes = []
        edge_list = []
        G = nx.Graph()


    # the total number of pairs = 1048575
    # we are using only 8000

        for row in csvreader:

            fromNode = int(row[0])
            toNode = int(row[1])

            nodes.append(fromNode)
            nodes.append(toNode)

            edge = [fromNode, toNode]
            edge_list.append(edge)


        #return(edge_list)
        G.add_edges_from(edge_list)
        count = 0
        for subgraph in connected_component_subgraphs(G):
            file_name = "reduced_data/reduce{}.edgelist".format(count)
            nx.write_edgelist(subgraph, file_name)
            count += 1
        #nx.draw_networkx(Gc, with_labels=False)
        #plt.show()
    


#print(slice_dataset())
#slice_dataset()
reduce()

#G=nx.read_edgelist("reduced_data/reduce0.edgelist")
#nx.draw_networkx(G, with_labels=False)
#plt.show()

