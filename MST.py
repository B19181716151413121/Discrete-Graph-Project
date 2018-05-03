#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 13:35:49 2018

@author: brian
"""

from Prims_Algorithm import Prims
#from Kurskals...

def MST(textfile, method = 'Prims', starting_vertex=0, show_cost = False, show_path = False, show=False):
    
    if method == 'Prims':
        return Prims(textfile, starting_vertex, show_cost, show_path, show)
    