# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:09:17 2020
@author: wangrui
"""
import pandas as pd

l = []
for i in range(2005, 2015):
    df0 = pd.read_csv('../singleNet_05_19/singleNet_'+str(i)+'.csv', header = None)
    l.append(df0)
df = pd.concat(l)

source = list(df[0])
target = list(df[1])
weight = list(df[2])
dic = {}
for i in range(len(source)):
    if source[i] in dic:
        dic[source[i]][target[i]] = weight[i]
    else:
        dic[source[i]] = dict()
        dic[source[i]][target[i]] = weight[i]
        
df_all = pd.read_csv('referenceNet_single05_19.csv', header = None)
new_weight = []
s = list(df_all[0])
t = list(df_all[1])
w = list(df_all[2])
for j in range(len(s)):
    print(s[j])
    if s[j] in dic:
        if t[j] in dic[s[j]]:
            new_weight.append(0)
        else:
            new_weight.append(w[j])
    else:
        new_weight.append(w[j])

df_all['finetune_w'] = new_weight
df_all.to_csv('finetune_Net_single_05_19.csv')











