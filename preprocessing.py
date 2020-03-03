import csv
from itertools import islice
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

file_name = "reduced_data/reduce_random.edgelist"

def connected_component_subgraphs(G):
    for c in nx.connected_components(G):
        yield G.subgraph(c)


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
            if random.randint(0,100) < 90:
                G.remove_node(n)
        return G

def get_list_data_from_file():
    edge_list = []
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=" ")
        for row in readCSV:
            fromNode = int(row[0])
            toNode = int(row[1])
            edge = [fromNode, toNode]
            edge_list.append(edge)
    return edge_list


# driver for preprocessing
if __name__ == "__main__":
    G = randomreduce()
    Gc = max(connected_component_subgraphs(G), key=len)
    
    nx.write_edgelist(Gc, file_name)
    get_list_data_from_file()



