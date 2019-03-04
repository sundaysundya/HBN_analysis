# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 15:19:31 2019

@author: sandhya
"""

import numpy as np
import scipy.io as scp
import pandas as pd
import os

atlas = 'aal'
path = '/cis/home/sandhya/NDD/edgelists_fmri' + atlas
files = [f for f in os.listdir(path) if f.endswith('.edgelist')]

names = [None] * len(files)


for i in range(0,len(files)):
    names[i] = files[i][4:16]


X = np.load('Xdata_'+atlas+'.npy')

ASSQ = pd.ExcelFile('aut_pheno/ASSQ.xlsx')
ASSQ = ASSQ.parse('Sheet1')
ASSQ = ASSQ.values
assqnam=ASSQ[:,0].astype('str')
for i in range(0, len(assqnam)):
    assqnam[i] = assqnam[i][1:13]
assqnam2 = assqnam.reshape(1401,1)
assqnam= np.ndarray.tolist(assqnam)
assqdat = ASSQ[:,1].astype('int').reshape(1401,1)
assqtab = np.concatenate((assqnam2, assqdat), axis=1)


SCQ = pd.ExcelFile('aut_pheno/SCQ.xlsx')
SCQ = SCQ.parse('Sheet1')
SCQ = SCQ.values
scqnam=SCQ[:,0].astype('str')
for i in range(0, len(scqnam)):
    scqnam[i] = scqnam[i][1:13]
scqnam2 = scqnam.reshape(1406,1)
scqnam= np.ndarray.tolist(scqnam)
scqdat = SCQ[:,1].astype('int').reshape(1406,1)
scqtab = np.concatenate((scqnam2, scqdat), axis=1)


SRS = pd.ExcelFile('aut_pheno/SRS.xlsx')
SRS = SRS.parse('Sheet1')
SRS = SRS.values
srsnam=SRS[:,0].astype('str')
for i in range(0, len(srsnam)):
    srsnam[i] = srsnam[i][1:13]
srsnam2 = srsnam.reshape(1303,1)
srsnam= np.ndarray.tolist(srsnam)
srsdat = SRS[:,1].astype('int').reshape(1303,1)
srstab = np.concatenate((srsnam2, srsdat), axis=1)


SRSPre = pd.ExcelFile('aut_pheno/SRSPre.xlsx')
SRSPre = SRSPre.parse('Sheet1')
SRSPre = SRSPre.values
srsprenam=SRSPre[:,0].astype('str')
srsprenam= np.ndarray.tolist(srsprenam)
for i in range(0, len(srsprenam)):
    srsprenam[i] = srsprenam[i][1:13]


subjectsASSQ = list(set(names) & set(assqnam))
subjectsSCQ = list(set(names) & set(scqnam))
subjectsSRS = list(set(names) & set(srsnam))
subjectsSRSPre = list(set(names) & set(srsprenam))

intersection = list(set(subjectsASSQ) & set(subjectsSCQ) & set(subjectsSRS))


Yintersect = np.zeros([len(intersection),3])
for i in range(0,len(intersection)):
    for j in range(0,len(assqtab)):
        if intersection[i]==assqtab[j,0]:
            Yintersect[i,0] = assqtab[j,1]
    for j in range(0,len(scqtab)):
        if intersection[i]==scqtab[j,0]:
            Yintersect[i,1] = scqtab[j,1]
    for j in range(0,len(srstab)):
        if intersection[i]==srstab[j,0]:
            Yintersect[i,2] = srstab[j,1]

names2 = np.array(names).reshape(len(files),1)
Xdata = np.concatenate((names2,X), axis=1)

Xintersect = np.zeros([len(intersection),X.shape[1]])
for i in range(0, len(intersection)):
    for j in range(0,len(Xdata)):
        if intersection[i] == Xdata[j,0]:
            Xintersect[i,:]=Xdata[j,1:(X.shape[1]+1)]
            
np.save('Xintersect_'+atlas,Xintersect)
np.save('Yintersect_'+atlas,Yintersect)