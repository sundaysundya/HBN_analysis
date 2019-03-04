# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:13:46 2019

@author: sandhya
"""

import numpy as np
from mgcpy.independence_tests.mgc.mgc import MGC
import matplotlib.pyplot as plt; plt.style.use('classic')
import matplotlib.ticker as ticker
import seaborn as sns; sns.set()

atlas = 'aal'

X = np.load('Xintersect_'+atlas+'.npy')
Y = np.load('Yintersect_'+atlas+'.npy')
Y1 = Y[:,0].reshape(X.shape[0],1)
Y2 = Y[:,1].reshape(X.shape[0],1)
Y3 = Y[:,2].reshape(X.shape[0],1)

mgc = MGC()
mgc_statistic, independence_test_metadata = mgc.test_statistic(Y1, Y3, is_fast=True)
p_value, metadata = mgc.p_value(Y1, Y3, is_fast=True)

print("MGC test statistic:", mgc_statistic)
print("P Value:", p_value)
print("Optimal Scale:", independence_test_metadata["optimal_scale"])

            #phenotypic heatmap calc

#tests = Y.shape[1]
#pvalheat = np.zeros([tests,tests])
#for i in range(0,tests):
#    for j in range (0,tests):
#        mgc = MGC()
#        mgc_statistic, independence_test_metadata = mgc.test_statistic(Y[:,i].reshape(Y.shape[0],1), Y[:,j].reshape(Y.shape[0],1), is_fast=True)
#        p_value, metadata = mgc.p_value(Y[:,i].reshape(Y.shape[0],1), Y[:,j].reshape(Y.shape[0],1), is_fast=True)
#        pvalheat[i,j]=p_value
#


#
## local correlation map
#local_corr = independence_test_metadata["local_correlation_matrix"]
#
## define two rows for subplots
#fig, (ax, cax) = plt.subplots(ncols=2, figsize=(9.45, 7.5),  gridspec_kw={"width_ratios":[1, 0.05]})
#
## draw heatmap
#fig.suptitle("Local Correlation Map", fontsize=17)
#ax = sns.heatmap(local_corr, cmap="YlGnBu", ax=ax, cbar=False)
#
## colorbar
#fig.colorbar(ax.get_children()[0], cax=cax, orientation="vertical")
#ax.invert_yaxis()
#
## optimal scale
#optimal_scale = independence_test_metadata["optimal_scale"]
#ax.scatter(optimal_scale[0], optimal_scale[1], marker='X', s=200, color='red') 
#
## other formatting
#ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
#ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
#ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
#ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
#ax.set_xlabel('#Neighbors for X', fontsize=15)
#ax.set_ylabel('#Neighbors for Y', fontsize=15) 
#ax.xaxis.set_tick_params(labelsize=15)
#ax.yaxis.set_tick_params(labelsize=15)
#cax.xaxis.set_tick_params(labelsize=15)
#cax.yaxis.set_tick_params(labelsize=15)
## fig.suptitle('cMGC = ' + str(mgc_statistic) + ', pMGC = ' + str(p_value), fontsize=20)
#
#plt.show()