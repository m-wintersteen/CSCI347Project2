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
    return 0

# Takes a graph G and a vertex v and returns
# the clustering coefficient of v
def getVertClustC(G, v):
    return 0

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
    G = np.array([[1,2],[1,3],[3,4],[4,2],[4,5],[5,1]])
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
    
