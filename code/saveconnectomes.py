# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:01:30 2019

@author: sandhya
"""
from connectome import make_connectome
import os
import numpy as np

atlas = 'tissue'
edgelist = 'edgelists_fmri'+atlas
corrmtx = 'corrmtx_fmri'+atlas
path = '/cis/home/sandhya/NDD/'+edgelist
files = [f for f in os.listdir(path) if f.endswith('.edgelist')]
os.mkdir('/cis/home/sandhya/NDD/'+corrmtx)


names = [None] * (len(files))
corr_mtx = make_connectome(edgelist+'/'+files[0])   # to get dimension of specific atlas
X = np.zeros([(len(files)),len(corr_mtx)**2])

for i in range(0,(len(files))):
    names[i] = files[i][4:16]
    corr_mtx = make_connectome(edgelist+'/'+files[i])
    np.save(os.path.join(corrmtx+'/'+names[i]),corr_mtx)
    vec = np.reshape(corr_mtx,(1, len(corr_mtx)**2))
    X[i]=vec
    
np.save('Xdata'+'_'+atlas,X)