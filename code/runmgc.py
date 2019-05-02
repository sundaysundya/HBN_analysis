# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:13:46 2019

@author: sandhya
"""
test = 'ACE'
import numpy as np
from mgcpy.independence_tests.mgc.mgc import MGC
import matplotlib.pyplot as plt; plt.style.use('classic')
import seaborn as sns; sns.set()
atlases = ('JHU','aal','brodmann','CPAC200','desikan','DK','HarOxCort','HarOxSub','hemispheric','pp264','tissue')
results = np.zeros([1,11])
i = 0

for atlas in atlases:
    
        #atlas = 'tissue'
    X = np.load('Xintersect_c_'+atlas+'.npy')
    Y = np.load('Yintersect_c_'+atlas+'.npy')
    #Y1 = Y[:,0].reshape(X.shape[0],1)
    #Y2 = Y[:,1].reshape(X.shape[0],1)
    #Y3 = Y[:,2].reshape(X.shape[0],1)  
    mgc = MGC()
    mgc_statistic, independence_test_metadata = mgc.test_statistic(X, Y)#, is_fast=True)
    p_value, metadata = mgc.p_value(X, Y)#, is_fast=True)
    
    print(atlas)
    print("MGC test statistic:", mgc_statistic)
    print("P Value:", p_value)
    results[0,i]=p_value
    i+=1
    #print("Optimal Scale:", independence_test_metadata["optimal_scale"])
    
np.save(test+'_results',results)


        #pheno vs pheno
testname = 'ARI_P'
testname2 = 'ARI_S'
import numpy as np
from mgcpy.independence_tests.mgc.mgc import MGC
import matplotlib.pyplot as plt; plt.style.use('classic')
import seaborn as sns; sns.set()
X = np.load('Xintersect_c_'+atlas+'.npy')
    Y = np.load('Yintersect_c_'+atlas+'.npy')
    #Y1 = Y[:,0].reshape(X.shape[0],1)
    #Y2 = Y[:,1].reshape(X.shape[0],1)
    #Y3 = Y[:,2].reshape(X.shape[0],1)  
    mgc = MGC()
    mgc_statistic, independence_test_metadata = mgc.test_statistic(X, Y)#, is_fast=True)
    p_value, metadata = mgc.p_value(X, Y)#, is_fast=True)
    
    print(atlas)
    print("MGC test statistic:", mgc_statistic)
    print("P Value:", p_value)