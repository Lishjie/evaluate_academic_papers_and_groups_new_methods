# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:13:24 2020
测试群组之间依存度
@author: wangrui
"""

import pandas as pd
import time
import networkx as nx
import csv

def parse():
    DG = nx.DiGraph()
    csv_reader = csv.reader(open('../referenceNet_single05_19.csv'))
    font_weight = tuple(csv_reader)
    DG.add_weighted_edges_from(font_weight)
    return DG

def dic_id_year_country_PR():
    dic = {}
    df = pd.read_excel('./random_fill_country_content_graph_list_05_19.xlsx')
    df.set_index(df["key"], inplace=True)
    keys = list(df['key'])
    for i, key in enumerate(keys):
        dic[key] = dict()
    for i, key in enumerate(keys):
        dic[key]['year'] = df.at[key, 'paperYear']
        dic[key]['meeting'] = df.at[key, 'meeting']
        dic[key]['paperRank'] = df.at[key, 'meetingRank']
        dic[key]['triRank'] = df.at[key, 'triRank']
        dic[key]['res2_first_coun'] = df.at[key, 'coun']
        dic[key]['PR0.5'] = df.at[key, 'PR0.5']
    return dic

def dic_referenceNet():
    dic = {}
    for key, node, weight in graph.edges(data=True):
        if int(key) in dic:
            dic[int(key)][int(node)] = float(weight['weight'])
        else:
            dic[int(key)] = dict()
            dic[int(key)][int(node)] = float(weight['weight'])
    sum_dic = {}
    for k in dic:
        sum_dic[k] = sum(dic[k].values())
    for source in dic:
        if sum_dic[source]:
            for tatget in dic[source]:
                dic[source][tatget] /= sum_dic[source]
    return dic

def surplus_country(refer_dic, iyc_dic, country1, country2):
    sum_c_u, sum_u_c, sum_c, sum_u = 0, 0, 0, 0
    dic_c_u = {2005:[0,0], 2006:[0,0], 2007:[0,0], 2008:[0,0], 2009:[0,0], \
               2010:[0,0], 2011:[0,0], 2012:[0,0], 2013:[0,0], 2014:[0,0], \
               2015:[0,0], 2016:[0,0], 2017:[0,0], 2018:[0,0], 2019:[0,0], 2020:[0,0]}
    dic_u_c = {2005:[0,0], 2006:[0,0], 2007:[0,0], 2008:[0,0], 2009:[0,0], \
               2010:[0,0], 2011:[0,0], 2012:[0,0], 2013:[0,0], 2014:[0,0], \
               2015:[0,0], 2016:[0,0], 2017:[0,0], 2018:[0,0], 2019:[0,0], 2020:[0,0]}
    nums_c = {2005:0, 2006:0, 2007:0, 2008:0, 2009:0, \
              2010:0, 2011:0, 2012:0, 2013:0, 2014:0, \
              2015:0, 2016:0, 2017:0, 2018:0, 2019:0, 2020:0}
    nums_u = {2005:0, 2006:0, 2007:0, 2008:0, 2009:0, \
              2010:0, 2011:0, 2012:0, 2013:0, 2014:0, \
              2015:0, 2016:0, 2017:0, 2018:0, 2019:0, 2020:0}
    for s in refer_dic:    # 施引文献
        coun = iyc_dic[s]['meeting']    # 施引文献的国家
        if country1 == coun:
            nums_u[iyc_dic[s]['year']] += 1    # 该国家当年的施引数量
            for t in refer_dic[s]:    # t是被引文献
                sum_u += iyc_dic[s]['PR0.5']*refer_dic[s][t]    # s被外界影响的总数
                coun1 = iyc_dic[t]['meeting']
                if coun1 != coun:
#                    dic_u_c[iyc_dic[s]['year']][0] += iyc_dic[s]['PR0.5']*refer_dic[s][t]    # 字典的第一个表示不分年份的影响总量
                    dic_u_c[iyc_dic[s]['year']][0] += refer_dic[s][t]
                    if country2 == coun1:
                        sum_u_c += iyc_dic[s]['PR0.5']*refer_dic[s][t]    # s被t影响的总数
#                        dic_u_c[iyc_dic[s]['year']][1] += iyc_dic[s]['PR0.5']*refer_dic[s][t]    # t对s的逐年影响
                        dic_u_c[iyc_dic[s]['year']][1] += refer_dic[s][t]

        if country2 == coun:
            nums_c[iyc_dic[s]['year']] += 1
            for t in refer_dic[s]:
                sum_c += iyc_dic[s]['PR0.5']*refer_dic[s][t]
                coun2 = iyc_dic[t]['meeting']
                if coun2 != coun:
#                    dic_c_u[iyc_dic[s]['year']][0] += iyc_dic[s]['PR0.5']*refer_dic[s][t]
                    dic_c_u[iyc_dic[s]['year']][0] += refer_dic[s][t]
                    if country1 == coun2:
                        sum_c_u += iyc_dic[s]['PR0.5']*refer_dic[s][t]
#                        dic_c_u[iyc_dic[s]['year']][1] += iyc_dic[s]['PR0.5']*refer_dic[s][t]
                        dic_c_u[iyc_dic[s]['year']][1] += refer_dic[s][t]
    return sum_u_c, sum_c_u, sum_u, sum_c, dic_u_c, dic_c_u, nums_u, nums_c

def calculate(dic):
    res= {}
    s1 = 0
    s0 = 0
    for key in dic:
        if dic[key][0] != 0:
            res[key] = dic[key][1]/dic[key][0]
        else:
            res[key] = 0
        s0 += dic[key][0]
        s1 += dic[key][1]
    if s0 == 0:
        res1 = 0
    else:
        res1 = s1/s0
    return res, res1

if __name__ == '__main__':
    start = time.time()
    graph = parse()
    dic = dic_referenceNet()
    dic1 = dic_id_year_country_PR()
    l = ['IJCV','CVPR','TPAMI','NeurIPS','ICML','ICCV','ECCV','EMNLP','ACL','JMLR','CONLL','COLT','NAACL','Machine Learning','AISTATS']
    for k in range(len(l)-1):
        u = l[k]
        for j in range(k+1,len(l)):
            c = l[j]
            res1 = surplus_country(dic, dic1, u, c)    # u在是country1, c是country2
            sum_u_c = res1[0]
            sum_c_u = res1[1]
            dic_u_c = res1[4]
            dic_c_u = res1[5]
            u_c = calculate(dic_u_c)[0]
            u_c_all = calculate(dic_u_c)[1]
            c_u = calculate(dic_c_u)[0]
            c_u_all = calculate(dic_c_u)[1]
            df = pd.DataFrame()
            col1 = u+'_'+c
            col2 = c+'_'+u
            y = [e for e in range(2005,2020)]
            l_u_c = []
            l_c_u = []
            for t in y:
                l_u_c.append(u_c[t])
                l_c_u.append(c_u[t])
            df['year'] = y
            df[col1] = l_u_c
            df[col2] = l_c_u
            df.to_excel('./conference_result/'+u+'VS'+c+'.xlsx')
#    res3 = trade_others(dic, dic1, 'Germany')
#    nums_cur_other = res3[2]
#    sum_cur_other = res3[-1]
#    cur_other = calculate_cur_other(nums_cur_other, sum_cur_other)[0]
#    cur_other_ave = calculate_cur_other(nums_cur_other, sum_cur_other)[1]
    
    print(time.time()-start)















