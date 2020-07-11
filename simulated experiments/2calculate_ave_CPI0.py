# -*- coding: utf-8 -*-
"""
@author: Rui Wang
"""

import pandas as pd

df = pd.read_csv('./CPI0_test4_1000_20_1-d_0.5.csv')
keys = list(df['key'])
pr = list(df['PR'])
N = 1000
dic = {}
year = 40
for i in range(year):
    dic[i] = 0

for j in range(len(keys)):
    dic[keys[j]//1000] += pr[j]
    