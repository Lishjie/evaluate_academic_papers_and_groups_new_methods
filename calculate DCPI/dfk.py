# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 09:46:58 2020
将exp(dfk)的值存储到fi表格中
@author: wangrui
"""
# div_K = (PR_K - FI_K)*d_f_k

import pandas as pd

df = pd.read_csv('div_singleNet_05_19.csv')
dic_dfk = {}
list_key = list(df['key'])
list_dfk = list(df['exp_dfk'])

for i, k in enumerate(list_key):
    dic_dfk[k] = list_dfk[i]
    
exp_dfk = []
df_all = pd.read_excel('../ranks_analysis/PR50.85/content_fi_pr50.85.xlsx')
key_all = list(df_all['key'])
for j, k in enumerate(key_all):
    exp_dfk.append(dic_dfk[k])

df_all['exp_dfk'] = exp_dfk
df_all.to_excel('../ranks_analysis/PR50.85/content_fi_pr50.85_cited5.xlsx')

