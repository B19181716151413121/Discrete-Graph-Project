#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:33:58 2018

@author: brian
"""

from Weighted_Graph import *

wg = Weighted_Graph('graph.txt')

def updateInfo():
    #Prints Edges and costs
    print("\nEdges and costs", wg.edge_dict())

    #Prints Edges
    print("\nEdges", wg.edge_set())

    #Prints Vertexes
    print("\nVertexes", wg.vertex_set())    

def minEdge():
    minValue = min(wg.edge_dict().values())
    for i in wg.edge_dict():
        if (minValue == wg.edge_dict()[i]):
            del wg.edge_dict()[i]
            return i

mins = minEdge()
print(mins)

#del[ wg.edge_dict()[3,2] ]
print(wg.edge_dict())
#T = ({}, []) #initial, verticies connected



