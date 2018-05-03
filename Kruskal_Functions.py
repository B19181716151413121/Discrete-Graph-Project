#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:33:58 2018

@author: brian
"""

from Weighted_Graph import *

wg = Weighted_Graph('graph.txt')
T = ({},[]) 
edges = []      
vert = []
#Pass in cost and returns edge
def findEdge(cost):
    for i in wg.edge_dict():
        if (cost == wg.edge_dict()[i]):
            #edges.append(i)
            #if edge is in 
            return i
#sorts values from least to greatest
def sortValues():
    costSorted = []
    for i in wg.edge_dict().values():
        costSorted.append(i)
    costSorted.sort()
    return costSorted
  
#returns number of verticies
def numberOfVerts():
    total = 0
    for i in wg.vertex_set():
        total += 1
    return total-1
        
#Finds minimum edge, adds it to graph, deletes from array
def minEdge(edges):
    mini = wg.edge_dict()[edges[0]]
    for edge in edges:
        cost = wg.edge_dict()[edge]
        if cost <= mini:
            mini = cost
            ed = edge 
    T[1].append(ed)
    edges.remove(ed)
    return edges

#Puts all edges of graph into an array to manipulate
def storeEdges():
    for edge in wg.edge_dict():
        edges.append(edge)

def main():
    storeEdges()
    numberOfVerts()
    wg.draw_graph()
    for i in range(numberOfVerts()):
        minEdge(edges)
        wg.draw_subgraph(T)
    


main()



