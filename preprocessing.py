import csv
from itertools import islice
import numpy as np

def slice_dataset():
    with open('dataset/amazon0302.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        nodes = []
        edge_list = []


    # the total number of pairs = 1048575
    # we are using only 8000

        for row in islice(csvreader, 1047575, None):

            fromNode = int(row[0])
            toNode = int(row[1])

            nodes.append(fromNode)
            nodes.append(toNode)

            edge = [fromNode, toNode]
            edge_list.append(edge)


        return(edge_list)


if __name__ == "__main__":
    print(slice_dataset())

