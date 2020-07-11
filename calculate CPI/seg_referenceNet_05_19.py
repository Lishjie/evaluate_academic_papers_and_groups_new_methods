# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:29:27 2020
划分不同年份区间的链接，并存入相应的链接文件中
@author: wangrui
"""

import pandas as pd
import os
import time

def dic_id_year(filename):
    df2 = pd.read_excel(filename)
    key_list = list(df2['key'])
    year_list = list(df2['paperYear'])
    dic_id_year = dict()
    for i in range(len(key_list)):
#        print('正在映射{}的年份'.format(list(df2['key'])[i]))
        dic_id_year[key_list[i]] = year_list[i]
    return dic_id_year

def every_six_year_keys(year):
    df_list = []
    for i in range(6):
        df_list.append(pd.read_excel('./content_05_19/content_'+str(year+i)+'.xlsx'))
    df = pd.concat(df_list)
    key_list = list(df['key'])
    return key_list

def seg_net(filename):
    df1 = pd.read_csv(filename, header = None)
    year = [i for i in range(2005, 2015)]
    for y in year:
        print(y)
        key_list = every_six_year_keys(y)
        df_cur = df1[df1[0].isin(key_list)]
        df_cur = df_cur[df_cur[1].isin(key_list)]
        print(df_cur.shape[0])
        df_cur.to_csv('./singleNet_05_19/singleNet_'+str(y)+'.csv')
        
if __name__ == '__main__':
    start_time = time.time()
    file_referenceNet = 'referenceNet_single05_19.csv'
    seg_net(file_referenceNet)
    print(time.time()-start_time)
    














