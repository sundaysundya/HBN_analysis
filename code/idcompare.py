# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 15:19:31 2019
This code finds the intersection of connectome data and phenotypic data for one test at a time, for each atlas.
@author: sandhya
"""

import numpy as np
import scipy.io as scp
import pandas as pd
import os
cwd = os.getcwd()

        #find intersection of correlation matrix data and phenotypic data subjects
atlases = ('JHU','aal','brodmann','CPAC200','desikan','DK','HarOxCort','HarOxSub','hemispheric','pp264','tissue')
for atlas in atlases:
    path = cwd+'/edgelists_fmri' + atlas
    files = [f for f in os.listdir(path) if f.endswith('.edgelist')]
    
    names = [None] * len(files)
    
    
    for i in range(0,len(files)):
        names[i] = files[i][4:16]
    
    
    X = np.load('Xdata_'+atlas+'.npy')
    
    
                #single test at a time
    testname = 'ACE'
    test = pd.ExcelFile('cleaned_pheno/clean_'+testname+'.xlsx') #'aut_pheno/ASSQ.xlsx'
    test = test.parse('Sheet1')
    test = test.values
    testnam=test[:,0].astype('str')
    sz = testnam.size
    testnam2 = testnam.reshape(sz,1)
    testnam= np.ndarray.tolist(testnam)
    testdat = test[:,1].astype('int').reshape(sz,1)
    testtab = np.concatenate((testnam2, testdat), axis=1)
    
    intersection = list(set(names) & set(testnam))
    
    
    
    Yintersect = np.zeros([len(intersection),1])
    for i in range(0,len(intersection)):
        for j in range(0,len(testtab)):
            if intersection[i]==testtab[j,0]:
                Yintersect[i,0] = testtab[j,1]
    
    names2 = np.array(names).reshape(len(files),1)
    Xdata = np.concatenate((names2,X), axis=1)
    
    Xintersect = np.zeros([len(intersection),X.shape[1]])
    for i in range(0, len(intersection)):
        for j in range(0,len(Xdata)):
            if intersection[i] == Xdata[j,0]:
                Xintersect[i,:]=Xdata[j,1:(X.shape[1]+1)]
                
    np.save('Xintersect_c_'+atlas,Xintersect)
    np.save('Yintersect_c_'+atlas,Yintersect)