# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:16:37 2020
分块计算PR，归一化
@author: wangrui
"""

# -*- coding: utf-8 -*-
import numpy as np
import os, csv, networkx as nx
import time
import pandas as pd

min_error=0.0001
max_iter=1000

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
        self.d = 0.2   # 阻尼系数
#        self.ranks = dict()  # 存储迭代结果
    
    def rank(self):
#        for key in self.graph.nodes:
#            self.ranks[key] = 0.0   # 初始化所有节点的rank值都是0
        N_nodes = len(self.graph.nodes)
        print(N_nodes)
        graph_list = list(self.graph.nodes) # 元素是节点id
        N = 1   # 定义矩阵的块数
        one_fourthNum = N_nodes//N     
        print('划分节点：'+str(one_fourthNum))
        # 读取分块
        now = time.time()
        last_time = now
        last_block_time = now
        # 求行和
        sum_l = np.zeros(N_nodes,dtype = 'float32')
        print('开始求行和',)
        start_sum_time = time.time()
        sum_time = time.time()
        for num_sum in range(N):
            print('>>>>>>'+str(num_sum))
            if num_sum <N-1:
                    cur = np.zeros((N_nodes,one_fourthNum),dtype='float32')  # 前三个矩阵，每个形状为[N, noe_fouethNum] 
                    for key, node, weight in self.graph.edges(data=True):   # 遍历节点和边
                        if graph_list.index(node) >= one_fourthNum*num_sum and graph_list.index(node) < one_fourthNum*(num_sum+1):
                            # 如果出链节点id在当前分块矩阵列索引范围内，则添加对应权重
                            cur[graph_list.index(key), graph_list.index(node)-one_fourthNum*num_sum] = weight['weight']
            else:   # 涉及到非整除，最后一个单独处理
                cur = np.zeros((N_nodes,N_nodes-one_fourthNum*(N-1)),dtype='float32')
                for key, node, weight in self.graph.edges(data=True):
                    if graph_list.index(node) >= one_fourthNum*(N-1):
                        cur[graph_list.index(key), graph_list.index(node)-one_fourthNum*(N-1)] = weight['weight']
            sum_l += cur.sum(axis=1)
            del cur
            end_sum_time = time.time()
            print('当前分块耗时 {} s:'.format(end_sum_time-start_sum_time))
            start_sum_time = end_sum_time
            print('<<<<<<')
        print('行和已求完,用时 {} s'.format(time.time()-sum_time))
#        sum_l = pd.read_csv('norm1_sum.csv')['sum'].values
        # 初始化向量
#        x0 = np.zeros(N_nodes,dtype='float32')
#        for xnum in range(len(x0)):
#            x0[xnum] = 1000/N_nodes
        x0 = pd.read_csv('PR0_0.0001_1000_1-d_0.55.csv')['PR'].values
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
                else:   # 涉及到非整除，最后一个单独处理
                    cur = np.zeros((N_nodes,N_nodes-one_fourthNum*(N-1)),dtype='float32')
                    for key, node, weight in self.graph.edges(data=True):
                        if graph_list.index(node) >= one_fourthNum*(N-1):
                            cur[graph_list.index(key), graph_list.index(node)-one_fourthNum*(N-1)] = weight['weight']
                # 归一化
                for k in range(N_nodes):
                    if sum_l[k]>0:
                        cur[k, :] /= sum_l[k]  # L
                    else:
                        cur[k, :] = 1 / N_nodes
                print(cur)
                cur_block_time = time.time()
                print("当前分块消耗total time {} s".format(cur_block_time-last_block_time))
                last_block_time = cur_block_time
                # 每次分块矩阵求当前分块的PR值
                x_cur = self.d * np.dot(x0, cur) + (1.0 - self.d)*1000 / x0.shape[0]
                del cur # 释放内存
                print(x_cur.shape)
                for each in x_cur:
                    x_next.append(each)
            print(np.array(x_next).shape)
            x_next = np.array(x_next).reshape(-1)
            print(str(j)+'次迭代，PR向量为0的元素有：'+str(np.sum(x_next==0)))
            error = sum(abs(x_next - x0))
            with open('error0_1000_0.0001_1-d_0.8.txt', 'a',encoding = 'utf-8') as f:
                f.write(str(error)+'\n')
            print("当前迭代误差 {} ".format(error))
            x0 = x_next
            cur_time = time.time()
            print("当前消耗total time {} s".format(cur_time-last_time))
            last_time = cur_time
            if error < min_error:
                break
            print(sum(x0))
        return x0,graph_list

if __name__ == '__main__':
    time_start = time.time()
    filename = "./NORM1Net_single05_19.csv"
    graph = parse(filename)
    p = PageRank(graph)
    A = p.rank()
    df = pd.DataFrame()
    df['key'] = A[1]
    df['PR'] = A[0]
    df.to_csv('./PR0_0.0001_1000_1-d_0.8.csv',encoding = 'utf-8') # 存储结果

    time_end = time.time()
    print("total time {} s".format(time_end-time_start))

