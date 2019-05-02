# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 11:54:04 2019
This code returns a correlation matrix from a ndmg outputted connectome file.
@author: sandhya
"""
import numpy as np

def make_connectome(file_name):
    with open(file_name, 'r') as f:
        all_lines = []
        for line in f.readlines():
            parsed_line = [float(x) for x in line.split()]
            all_lines.append(parsed_line)
    
    temp_mtx = np.array(all_lines)
    # the dimension of the correlation mtx
    temp_mtx[:,0]=np.round(temp_mtx[:,0])
    temp_mtx[:,1]=np.round(temp_mtx[:,1])
    
    mtx_dim = temp_mtx.max(axis=0)[0]
    corr_mtx = np.zeros([int(mtx_dim), int(mtx_dim)])
    

    #nodeA, nodeB, edge = parsed_line[0], parsed_line[1], parsed_line[2]
    
    for row in temp_mtx:
        nodeA, nodeB, edge = int(row[0]), int(row[1]), row[2]
        corr_mtx[nodeA-1, nodeB-1] = edge
        corr_mtx[nodeB-1, nodeA-1] = edge
    return corr_mtx