# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:05:31 2020
计算论文FI指数
@author: wangrui
"""
import pandas as pd
import numpy as np
import networkx as nx
import csv
import time

def parse(filename):
    DG = nx.DiGraph()
    csv_reader = csv.reader(open(filename,encoding = 'utf-8'))
    font_weight = tuple(csv_reader)
    DG.add_weighted_edges_from(font_weight)
    return DG

def cited_reference():
    '''
    return{文献K：{施引文献1：权重1，施引文献2：权重2...}}
    '''
    df = pd.read_csv('referenceNet_single05_19.csv', header = None)
    source, target, weight = df[0], df[1], df[2]
    cited_ref = {}
    for i in range(len(target)):
        if target[i] in cited_ref:
            cited_ref[target[i]][source[i]] = weight[i]
        else:
            cited_ref[target[i]] = {}
            cited_ref[target[i]][source[i]] = weight[i]
    return cited_ref
    
def index_id():
    '''
    return {id:index}, {index:id}
    '''
    filename = "./referenceNet_single05_19.csv"
    graph = parse(filename)
    dic_index_id = {}
    dic_id_index = {}
    id_list = list(graph.nodes)
    for i, key in enumerate(id_list):
        dic_id_index[key] = i
        dic_index_id[i] = key
    return dic_id_index, dic_index_id

def Sim():
    sim = np.load('sims.npy')
    dic_i_j_sim = {}
    for i in range(sim.shape[0]):
        for j in range(sim.shape[1]):
            dic_i_j_sim[tuple([i, j])] = sim[i][j]
    return dic_i_j_sim

def doc_topic_dic():
    '''
    return {doc_id:{topic_id:概率}}
    '''
    with open('doc_topic.txt') as f:
        lines = f.readlines()
    sum_l = [0]*len(lines)
    for i in range(len(lines)):
        l = lines[i].strip('\n').replace('  ', ' ').split(' ')
        for j in range(1, len(l)):
            sum_l[i] += int(l[j].split(':')[1])
    doc_topics_dict = {}
    for num_line, line in enumerate(lines):
        print(num_line)
        list_line = line.strip('\n').replace('  ', ' ').split(' ')
        key = int(list_line[0])+1
        doc_topics_dict[key] = {}
        for i in range(1, len(list_line)):
            doc_topics_dict[key][int(list_line[i].split(':')[0])] = \
            int(list_line[i].split(':')[1])/sum_l[num_line]
    return doc_topics_dict 

def id_pr():
    '''
    return {id: pr}
    '''
    file_PR = 'PR_1000_0.0001_norm5_0.85_same_first_year_ave.csv'
    key = list(pd.read_csv(file_PR)['key'])
    PR = list(pd.read_csv(file_PR)['PR'])
    dic_id_pr = {}
    for i, k in enumerate(key):
        print(i,'====',k)
        dic_id_pr[k] = PR[i]
    return dic_id_pr

def diff_set(list1, list2):
    '''
    return list1-list2
    '''
    c = list(set(list1) - set(list2))
    return c

def graph_node_sum():
    # return {id, sum_weight}
    filename = "./referenceNet_single05_19.csv"
    df = pd.read_csv(filename, header = None)
    source = df[0] 
    weight = df[2]
    dic = {}
    dic_sum = {}
    dic_counts = {}
    for i in range(len(source)):
        if source[i] in dic:
            if weight[i] != 0:
                dic[source[i]].append(weight[i])
        else:
            dic[source[i]] = []
            if weight[i] != 0:
                dic[source[i]].append(weight[i])
    graph_list = list(pd.read_csv('graph_list_05_19.csv').key)
    # id和权重和一一对应map
    for key in dic:
        dic_sum[key] = sum(dic[key])
        dic_counts[key] = len(dic[key])
    for k in graph_list:
        if k not in dic_sum:
            dic_sum[k] = 0
            dic_counts[k] = 0
    print(len(dic_sum), '*****', len(dic_counts))
    return dic_sum, dic_counts

def caulculate_FI(cited_ref, dic_id_pr, dic_i_j_sim, doc_topics_dict, dic_sum, dic_counts):
    '''
    input:cited_dic, getIP, Sim, doc_topics_dic的输出
    output:list of id, pr, FI
    '''
#    M = 1    # 用均值代替, 验证的时候用 M = 1, 已通过验证
#    M = 0.466*0.246*0.246
    M = 0.028200456    # 一个ave_sim, 两个ave_P
    d = 0.85
    graph_list = list(pd.read_csv('graph_list_05_19.csv').key)
    l_id, l_pr, l_FI = [], [], []
    i = 0
    for K in cited_ref:
        print(i)
        print('当前正在计算的节点 {}'.format(K))
        l_id.append(K)
        l_pr.append(dic_id_pr[K])        
        preFI_K = 0
        # 真实链接
        for b in cited_ref[K]:    # 遍历那些有施引文献的
            print('当前正在计算的施引文献 {}'.format(b))
            for ti in doc_topics_dict[K]:    # ti (0,114)
                W_b_K = cited_ref[K][b]
                P_ti_K = doc_topics_dict[K][ti]
                for tj in doc_topics_dict[b]:
                    P_tj_b = doc_topics_dict[b][tj]
                    preFI_K += dic_i_j_sim[(ti, tj)]*P_ti_K*P_tj_b*dic_id_pr[b]*W_b_K
#                    preFI_K += 1*P_ti_K*P_tj_b*dic_id_pr[b]*W_b_K    # 测试专用
        # 虚拟连接
        last_list = diff_set(graph_list, list(cited_ref[K].keys()))
        for b1 in last_list:
            num_zero_id = len(graph_list) - dic_counts[b1]
            sum_W_zero_id = 1 - dic_sum[b1]
            preFI_K += M * dic_id_pr[b1] * sum_W_zero_id/num_zero_id
        FI_K = d*preFI_K+(1-d)*1000/len(graph_list)
        l_FI.append(FI_K)
        i+=1
    return l_id, l_pr, l_FI

def restore(res):
    df = pd.DataFrame()
    df['key'] = res[0]
    df['PR'] = res[1]
    df['FI'] = res[2]
    df.to_csv('norm5_0.85_fi_same_first_year_ave.csv')
    
if __name__ == '__main__':
    start = time.time()
    cited_ref = cited_reference()
    dic_id_pr = id_pr()
    dic_i_j_sim = Sim()
    doc_topics_dict = doc_topic_dic()
    dic_sum = graph_node_sum()[0]
    dic_counts = graph_node_sum()[1]
    res = caulculate_FI(cited_ref, dic_id_pr, dic_i_j_sim, doc_topics_dict, dic_sum, dic_counts)
    restore(res)
    print(time.time()-start)
    

    


