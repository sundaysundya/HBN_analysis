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

        #find intersection of correlation matrix data and phenotypic data subjects
atlases = ('JHU','aal','brodmann','CPAC200','desikan','DK','HarOxCort','HarOxSub','hemispheric','pp264','tissue')
for atlas in atlases:
    path = '/cis/home/sandhya/NDD/edgelists_fmri' + atlas
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
    #for i in range(0, len(assqnam)):
    #    assqnam[i] = assqnam[i][1:13]
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



        #find intersection of two phenotypic tests
testname = 'ARI_P'
test = pd.ExcelFile('cleaned_pheno/clean_'+testname+'.xlsx')
test = test.parse('Sheet1')
test = test.values
testnam=test[:,0].astype('str')
sz = testnam.size
testnamb = testnam.reshape(sz,1)
testnam= np.ndarray.tolist(testnam)
testdat = test[:,1].astype('int').reshape(sz,1)
testtab = np.concatenate((testnamb, testdat), axis=1)

testname2 = 'ARI_S'
test2 = pd.ExcelFile('cleaned_pheno/clean_'+testname2+'.xlsx')
test2 = test2.parse('Sheet1')
test2 = test2.values
testnam2=test2[:,0].astype('str')
#for i in range(0, len(assqnam)):
#    assqnam[i] = assqnam[i][1:13]
sz = testnam2.size
testnamb2 = testnam2.reshape(sz,1)
testnam2= np.ndarray.tolist(testnam2)
testdat2 = test2[:,1].astype('int').reshape(sz,1)
testtab2 = np.concatenate((testnamb2, testdat2), axis=1)

intersection = list(set(testnam) & set(testnam2))

Yintersect = np.zeros([len(intersection),1])
for i in range(0,len(intersection)):
    for j in range(0,len(testtab)):
        if intersection[i]==testtab[j,0]:
            Yintersect[i,0] = testtab[j,1]

Xintersect = np.zeros([len(intersection),1])
for i in range(0,len(intersection)):
    for j in range(0,len(testtab2)):
        if intersection[i]==testtab2[j,0]:
            Xintersect[i,0] = testtab2[j,1]
            
np.save('Xintersect_'+testname,Xintersect)
np.save('Yintersect_'+testname2,Yintersect)
