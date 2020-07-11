# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:16:37 2020
PR5
@author: wangrui
"""

# -*- coding: utf-8 -*-
import numpy as np
import re, csv, networkx as nx
import time
import pandas as pd

min_error=0.0001
max_iter=100

def graph_node_sum(filename):
    # return {id, sum_weight}
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
    # id和权重和一一对应map
    for key in dic:
        dic_sum[key] = sum(dic[key])
        dic_counts[key] = len(dic[key])
    return dic_sum, dic_counts

def parse(filename):    # 解析csv
#    reader = csv.reader(open(filename, 'r'), delimiter=',')
    DG = nx.DiGraph()
    csv_reader = csv.reader(open(filename,encoding = 'utf-8'))
    font_weight = tuple(csv_reader)
    DG.add_weighted_edges_from(font_weight)
    return DG

class PageRank:
    def __init__(self, graph):
#    def __init__(self):
        self.graph = graph
#        self.V = len(self.graph)    # 一共多少施引文献
        self.d = 0.25  # 阻尼系数
#        self.ranks = dict()  # 存储迭代结果
    
    def rank(self):
        graph_list = list(self.graph.nodes) # 元素是节点id
        N_nodes = len(self.graph.nodes)
        print(N_nodes)
        N = 1  # 定义矩阵的块数
        one_fourthNum = N_nodes//N     
        print('划分节点：'+str(one_fourthNum))
        # 读取分块
        now = time.time()
        last_time = now
        last_block_time = now

        # 初始化向量
#        x0 = np.zeros(N_nodes,dtype='float32')
#        for xnum in range(len(x0)):
#            x0[xnum] = 1000/N_nodes
        x0 = pd.read_csv('./PR_1000_0.0001_norm5_1-0.65_same_first_year_ave.csv')['PR'].values
        print(type(x0))
        print(len(x0))
        print('迭代开始前，x0中0的个数 {} 个'.format(np.sum(x0==0)))
        #开始迭代
        for j in range(max_iter):
            print('开始第 {} 轮迭代！'.format(j))
            x_next = [] # 初始化x_next
            for i in range(N):
                if i <N-1:
                    cur = np.zeros((N_nodes,one_fourthNum),dtype='float32')  # 前三个矩阵，每个形状为[N, noe_fouethNum] 
                    for key, node, weight in self.graph.edges(data=True):   # 遍历节点和边
                        if graph_list.index(node) >= one_fourthNum*i and graph_list.index(node) < one_fourthNum*(i+1):
                            # 如果出链节点id在当前分块矩阵列索引范围内，则添加对应权重
                            cur[graph_list.index(key), graph_list.index(node)-one_fourthNum*i] = weight['weight']
                    cur_wp = wp[one_fourthNum*i:one_fourthNum*(i+1)]
                else:   # 涉及到非整除，最后一个单独处理
                    cur = np.zeros((N_nodes,N_nodes-one_fourthNum*(N-1)),dtype='float32')
                    for key, node, weight in self.graph.edges(data=True):
                        if graph_list.index(node) >= one_fourthNum*(N-1):
                            cur[graph_list.index(key), graph_list.index(node)-one_fourthNum*(N-1)] = weight['weight']
                    cur_wp = wp[one_fourthNum*(N-1):]
                # 归一化
                for k in range(N_nodes):
#                    print(cur[k, :])
                    if sum_l[k]>0:
                        cur[k, :][cur[k, :]==0] = (1-sum_l[k])/(N_nodes-count_l[k])
                    else:
                        cur[k, :][cur[k, :]==0] = 1/N_nodes
#                    print(cur[k,:])
#                    print(sum(cur[k, :]))
                cur_block_time = time.time()
                print("当前分块消耗total time {} s".format(cur_block_time-last_block_time))
                last_block_time = cur_block_time
                # 每次分块矩阵求当前分块的PR值
#                x_cur = self.d * np.dot(x0, cur) + (1.0 - self.d)*1000 / x0.shape[0]
                x_cur = self.d * np.dot(x0, cur) + (1.0 - self.d)*np.array(cur_wp)*1000
                del cur # 释放内存
                del cur_wp
                print(x_cur.shape)
                for each in x_cur:
                    x_next.append(each)
            print(np.array(x_next).shape)
            x_next = np.array(x_next).reshape(-1)
            print(str(j)+'次迭代，PR向量为0的元素有：'+str(np.sum(x_next==0)))
            error = sum(abs(x_next - x0))
            with open('./error_PR5_d_1-d_0.75_same_first_year_ave.txt', 'a',encoding = 'utf-8') as f:
                f.write(str(error)+'\n')
            print("当前迭代误差 {} ".format(error))
            x0 = x_next
            cur_time = time.time()
            print("当前消耗total time {} s".format(cur_time-last_time))
            last_time = cur_time
            if error < min_error:
                break
            print(sum(x0))
        return x0, graph_list

if __name__ == '__main__':
    time_start = time.time()
    filename = "./referenceNet_single05_19.csv"
#    filename = "./papers_test.csv"
    graph = parse(filename)
    graph_list = list(graph.nodes)
    graph_list1 = [int(graph_list[i]) for i in range(len(graph_list))]
    dic_sum = graph_node_sum(filename)[0]
    dic_counts = graph_node_sum(filename)[1]
    sum_l = []
    count_l = []
    for i in range(len(graph_list1)):
        if graph_list1[i] in dic_sum:
            sum_l.append(dic_sum[graph_list1[i]])
            count_l.append(dic_counts[graph_list1[i]])
        else:
            sum_l.append(0)
            count_l.append(0)
    df_wp = pd.read_csv('./wp_final_normal_first_year_ave.csv')
    dic_key_wp = {}
    key_list = list(df_wp['key'])
    wp_list = list(df_wp['PR'])
    for j, k in enumerate(key_list):
        dic_key_wp[k] = wp_list[j]
    wp = []
    for z, e in enumerate(graph_list1):
        wp.append(dic_key_wp[e])
    print(wp[0])
    p = PageRank(graph)
    A = p.rank()
    df = pd.DataFrame()
    df['key'] = A[1]
    df['PR'] = A[0]
    df.to_csv('./PR_1000_0.0001_norm5_1-0.75_same_first_year_ave.csv',encoding = 'utf-8') # 存储结果
    time_end = time.time()
    print("total time {} s".format(time_end-time_start))

