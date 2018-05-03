#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 22:41:59 2018

@author: brian
"""


from Weighted_Graph import *
g = Weighted_Graph('graph3.txt')
T = ({},[])
 
edges = []      
vert = []

totalCost = 0

def numVert():
    num = 0
    for i in g.vertex_set():
        num += 1
    return num  # len(g.vertex_set())
    
print(g.edge_set())

def storeEdgesIntoArray(edges):
    for edge in g.edge_dict():
        edges.append(edge)
        # return list(g.edge_set())

def findMinEdge(edges):
    mini = g.edge_dict()[edges[0]] # cost of edge edges[0]
    ed = edges[0]
    for i in edges:
        cost = g.edge_dict()[i]
        if cost < mini:  # if g.edge_dict()[i] < mini
            mini = cost
            ed = i
    if ed[0] not in vert or ed[1] not in vert:
        T[1].append(ed)
        vert.append(ed[1])
        vert.append(ed[0])
        g.draw_subgraph(T)
        global totalCost 
        totalCost += mini
        edges.remove(ed)
    else:
        edges.remove(ed)
    return edges
        


g.draw_graph()
numVert = numVert()
storeEdgesIntoArray(edges)


while len(set(vert)) < numVert:
    findMinEdge(edges)
g.draw_subgraph(T)
print("Total Cost:", totalCost)
   
