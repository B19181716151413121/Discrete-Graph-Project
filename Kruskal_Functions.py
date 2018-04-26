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

def findEdge(cost):
    for i in wg.edge_dict():
        if (cost == wg.edge_dict()[i]):
            #edges.append(i)
            #if edge is in 
            return i

def sortValues():
    costSorted = []
    for i in wg.edge_dict().values():
        costSorted.append(i)
    costSorted.sort()
    return costSorted
  

def minEdge():
    mini = 10000000000000
    for i in wg.edge_dict():
        if(wg.edge_dict()[i] < mini):
            print(wg.edge_dict()[i], mini)
            mini = wg.edge_dict()[i]  
            
    
    return i


        
print(minEdge())
"""costs =[]
vert = []
costs = sortValues()

wg.draw_graph()


for i in range (len(costs)-1):
    #print(costs[i])
    edge = findEdge(costs[i])
    print(edge)
    if ( edge[0] or edge[1] not in vert):
        T[1].append(findEdge(costs[i]))
        vert.append(edge[1])
   

    #T[1].append(findEdge(i))
wg.draw_subgraph(T)

"""


