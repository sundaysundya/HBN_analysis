# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:01:30 2019
This code reads all of the '.edgelist' files in a folder (a single atlas), creates their correlation matrix, 
vectorizes it, and puts it into a total matrix for the atlas where each row is one subject. It also saves each individual 
subject's correlation matrix in a folder of all the matrices for that atlas.
@author: sandhya
"""
from connectome import make_connectome
import os
import numpy as np
cwd = os.getcwd()

atlas = 'tissue'
edgelist = 'edgelists_fmri'+atlas
corrmtx = 'corrmtx_fmri'+atlas
path = cwd+'/'+edgelist
files = [f for f in os.listdir(path) if f.endswith('.edgelist')]
os.mkdir(cwd+'/'+corrmtx)


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