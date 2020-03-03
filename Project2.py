'''
    Matthew Wintersteen
    Bruce Clark
    Norhan Abbas

    Data Mining Project 2
'''

import numpy as np
import pandas as pd
import math
import networkx as nx


# Takes a graph G (list of edges) and a vertex v and returns the degree of v
def getDegree(G, v):
    degree = 0
    for e in G:
        if v in e:
            degree += 1
    return degree


# Takes a graph G and a vertex v and returns
# the clustering coefficient of v
def getVertClustC(G, v):
    # get v neighbors first
    v_neighbors = []
    for e in G:
        if v in e:
            if e[0] == v:
                v_neighbors.append(e[1])
            else:
                v_neighbors.append(e[0])
    # now find all the edges only between v neighbors
    numerator = 0
    for e in G:
        if e[0] in v_neighbors and e[1] in v_neighbors:
            numerator += 1

    denominator = (len(v_neighbors) * (len(v_neighbors) - 1)) / 2
    if denominator != 0:
        return numerator / denominator
    else:
        return 0


# Takes a graph G and returns the clustering coefficent of G
def getGraphClustC(G):
    cc = 0
    # get list of vertices in G
    vert = []
    for e in G:
        if e[0] not in vert:
            vert.append(e[0])
        if e[1] not in vert:
            vert.append(e[1])

    # sum individual clustering coefficients
    for v in vert:
        cc += getVertClustC(G, v)

    return cc


# Takes a graph G and a vertex v and return the closeness centrality of v
def getCloseC(G, v):
    # make networkx graph
    Gprime = nx.Graph()
    Gprime.add_edges_from(G)
    # all other nodes in graph
    y = []
    for e in G:
        if e[0] != v:
            if e[0] not in y:
                y.append(e[0])
        if e[1] != v:
            if e[1] not in y:
                y.append(e[1])

    spsum = 0
    for i in y:
        spsum += len(nx.shortest_path(Gprime, source=v, target=i))

    return 1 / spsum


# Takes a graph G and a vertex v and return the betweenness centrality of v
def getBC(G, v):
    # make networkx graph
    Gprime = nx.Graph()
    Gprime.add_edges_from(G)
    # all other nodes in graph
    y = []
    for e in G:
        if e[0] != v:
            if e[0] not in y:
                y.append(e[0])
        if e[1] != v:
            if e[1] not in y:
                y.append(e[1])

    spsum = 0
    num = 0
    den = 0
    for i in y:
        for k in y:
            if i != k:
                for p in nx.all_shortest_paths(Gprime, source=i, target=k):
                    den += 1
                    if v in p:
                        num += 1
    return num / den


# Takes a graph G and returns the average shortest path
def getMeanShortPath(G):
    # make networkx graph
    Gprime = nx.Graph()
    Gprime.add_edges_from(G)
    # get list of nodes
    v = list(Gprime.nodes)
    total = 0
    num = 0
    for i in range(len(v)):
        for k in range(len(v)):
            if i != k:
                total += len(nx.shortest_path(Gprime, v[i], v[k]))
                num += 1
    avg = (total / num)-1
    return avg


def testFunc():
    G = np.array([[1, 2], [2, 3], [1, 3], [3, 4], [4, 2], [4, 5], [5, 1]])
    Gprime = nx.Graph()
    Gprime.add_edges_from(G)
    v = 1
    print("Part 2.\n4.\ngetDegree")
    print(getDegree(G, v))
    print("\n5.\ngetVertClustC")
    print(getVertClustC(G, v))
    print("\n6.\ngetGraphClustC")
    print(getGraphClustC(G))
    print("\n7.\ngetCloseC")
    print(getCloseC(G, v))
    print("\n8.\ngetBC")
    print(getBC(G, v))
    print("\n9.\ngetMeanShortPath")
    print(getMeanShortPath(G))


# driver for function testing
if __name__ == "__main__":
    testFunc()
