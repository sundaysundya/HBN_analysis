# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:01:30 2019

@author: sandhya
"""
from connectome import make_connectome
import os
import numpy as np


path = '/cis/home/sandhya/NDD/edgelists_fmriJHU'
files = [f for f in os.listdir(path) if f.endswith('.edgelist')]

names = [None] * 337
X = np.zeros([337,2304])

for i in range(0,337):
    names[i] = files[i][4:16]
    corr_mtx = make_connectome('edgelists_fmriJHU/'+files[i])
    np.save(os.path.join('corrmtx_fmriJHU/'+names[i]),corr_mtx)
    vec = np.reshape(corr_mtx,(1, 2304))
    X[i]=vec
    
np.save('Xdata',X)