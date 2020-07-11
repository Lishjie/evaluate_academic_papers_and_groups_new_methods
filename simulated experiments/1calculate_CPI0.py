# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:16:37 2020
分块计算PR，归一化
@author: wangrui
"""
import numpy as np
import csv, networkx as nx
import time
import pandas as pd

min_error=0.0001
max_iter=1000

def parse(filename):  
    DG = nx.DiGraph()
    csv_reader = csv.reader(open(filename,encoding = 'utf-8'))
    font_weight = tuple(csv_reader)
    DG.add_weighted_edges_from(font_weight)
    return DG

class PageRank:
    def __init__(self, graph):
        self.graph = graph
        self.d = 0.5   
    
    def rank(self):
        N_nodes = len(self.graph.nodes)
        print(N_nodes)
        graph_list = list(self.graph.nodes) 
        N = 4   
        one_fourthNum = N_nodes//N     
        print('划分节点：'+str(one_fourthNum))
        now = time.time()
        last_time = now
        sum_l = np.zeros(N_nodes,dtype = 'float32')
        print('开始求行和',)
        for num_sum in range(N):
            print('>>>>>>'+str(num_sum))
            if num_sum <N-1:
                    cur = np.zeros((N_nodes,one_fourthNum),dtype='float32')  
                    for key, node, weight in self.graph.edges(data=True):  
                        if graph_list.index(node) >= one_fourthNum*num_sum and graph_list.index(node) < one_fourthNum*(num_sum+1):
                            cur[graph_list.index(key), graph_list.index(node)-one_fourthNum*num_sum] = weight['weight']
            else:  
                cur = np.zeros((N_nodes,N_nodes-one_fourthNum*(N-1)),dtype='float32')
                for key, node, weight in self.graph.edges(data=True):
                    if graph_list.index(node) >= one_fourthNum*(N-1):
                        cur[graph_list.index(key), graph_list.index(node)-one_fourthNum*(N-1)] = weight['weight']
            sum_l += cur.sum(axis=1)
            del cur
            print('<<<<<<')
        x0 = np.zeros(N_nodes,dtype='float32')
        for xnum in range(len(x0)):
            x0[xnum] = 1000/N_nodes
        for j in range(max_iter):
            x_next = []
            for i in range(N):
                if i <N-1:
                    cur = np.zeros((N_nodes,one_fourthNum),dtype='float32')  
                    for key, node, weight in self.graph.edges(data=True):   
                        if graph_list.index(node) >= one_fourthNum*i and graph_list.index(node) < one_fourthNum*(i+1):
                            cur[graph_list.index(key), graph_list.index(node)-one_fourthNum*i] = weight['weight']
                else:   
                    cur = np.zeros((N_nodes,N_nodes-one_fourthNum*(N-1)),dtype='float32')
                    for key, node, weight in self.graph.edges(data=True):
                        if graph_list.index(node) >= one_fourthNum*(N-1):
                            cur[graph_list.index(key), graph_list.index(node)-one_fourthNum*(N-1)] = weight['weight']
                for k in range(N_nodes):
                    if sum_l[k]>0:
                        cur[k, :] /= sum_l[k] 
                    else:
                        cur[k, :] = 1 / N_nodes
                x_cur = self.d * np.dot(x0, cur) + (1.0 - self.d)*1000 / x0.shape[0]
                del cur 
                print(x_cur.shape)
                for each in x_cur:
                    x_next.append(each)
            print(np.array(x_next).shape)
            x_next = np.array(x_next).reshape(-1)
            error = sum(abs(x_next - x0))
#            with open('error0_test5_1000_20_1-d_0.5.txt', 'a',encoding = 'utf-8') as f:
#                f.write(str(error)+'\n')
            print("cur_error: {} ".format(error))
            x0 = x_next
            cur_time = time.time()
            print("cur_total_time {} s".format(cur_time-last_time))
            last_time = cur_time
            if error < min_error:
                break
            print(sum(x0))
        return x0, graph_list

if __name__ == '__main__':
    time_start = time.time()
    filename = "./testNet4_1000_20_6.csv"
    graph = parse(filename)
    p = PageRank(graph)
    A = p.rank()
    df = pd.DataFrame()
    df['key'] = A[1]
    df['PR'] = A[0]
    df.to_csv('./CPI0_test4_1000_20_1-d_0.5.csv',encoding = 'utf-8') # 存储结果
    time_end = time.time()
    print("total time {} s".format(time_end-time_start))

