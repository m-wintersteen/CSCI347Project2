'''
    Matthew Wintersteen
    Bruce Clark
    Norhan Abbas

    Data Mining Project 2
'''

import numpy as np
import pandas as pd
import math

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

    denominator = (len(v_neighbors)*(len(v_neighbors)-1))/2
    return numerator/denominator

# Takes a graph G and returns the clustering coefficent of G
def getGraphClustC(G):
    return 0

# Takes a graph G and a vertex v and return the closeness centrality of v
def getCloseC(G, v):
    return 0

# Takes a graph G and a vertex v and return the betweenness centrality of v
def getBC(G, v):
    return 0

# Takes a graph G and returns the average shortest path
def getMeanShortPath(G):
    return 0

def testFunc():
    G = np.array([[1,2],[2,3],[1,3],[3,4],[4,2],[4,5],[5,1]])
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

#driver for function testing
testFunc()
    
