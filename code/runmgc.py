# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:13:46 2019

@author: sandhya
"""
test = 'ACE'
import numpy as np
from mgcpy.independence_tests.mgc import MGC
import matplotlib.pyplot as plt; plt.style.use('classic')
import seaborn as sns; sns.set()
atlases = ('JHU','aal','brodmann','CPAC200','desikan','DK','HarOxCort','HarOxSub','hemispheric','pp264','tissue')
results = np.zeros([1,11])
i = 0

for atlas in atlases:
    
        #atlas = 'tissue'
    X = np.load('Xintersect_c_'+atlas+'.npy')
    Y = np.load('Yintersect_c_'+atlas+'.npy')
    mgc = MGC()
    mgc_statistic, independence_test_metadata = mgc.test_statistic(X, Y)
    p_value, metadata = mgc.p_value(X, Y)
    
    print(atlas)
    print("MGC test statistic:", mgc_statistic)
    print("P Value:", p_value)
    results[0,i]=p_value
    i+=1
    
np.save(test+'_results',results)