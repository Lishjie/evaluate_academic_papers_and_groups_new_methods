# -*- coding: utf-8 -*-
"""
@author: wangrui
"""

import numpy as np
import pandas as pd
import time
import random
import math 

#def load_files():
#    t_vectors0 = np.load("t_vectors.npy")   # 每列是论文的不同主题概率P
#    Ced0 = np.load("Ced.npy")   # 存储的是FI计算中用到的论文id
#    pr_value = np.load("pr_value.npy").item()   # 存储的是PR值，字典
#    B0 = np.load("B.npy")  # 存储的是施引文献id
#    FI0 = np.load("FI.npy")  # 存储的是论文的FI值
#    sims0 = np.load("sims.npy")  # 存储的是主题相似度
#    t_vectors = np.array(t_vectors0)
#    #t_vectors = np.transpose(t_vectors1)
#    Ced = Ced0.tolist()
#    B = B0.tolist()
#    FI = FI0.tolist()
#    sims = sims0.tolist()
#    return t_vectors, Ced, B, FI, sims, pr_value # Ced, B, FI, sims, pr_value

def cited_cite_dic():
    '''
    output:{paper_id:[施引文献b], }
    '''
    df = pd.read_csv('referenceNet_single05_19.csv', header = None)
    cite = list(df[0])
    cited = list(df[1])
    dic_cited_cite = {}
    for i, K_id in enumerate(cited):
        if K_id in dic_cited_cite:
            dic_cited_cite[K_id].append(cite[i])
        else:
            dic_cited_cite[K_id] = []
            dic_cited_cite[K_id].append(cite[i])
    return dic_cited_cite

def Sim():
    sim = np.load('sims.npy')
    dic_i_j_sim = {}
    for i in range(sim.shape[0]):
        for j in range(sim.shape[1]):
            dic_i_j_sim[tuple([i, j])] = sim[i][j]
    return dic_i_j_sim

def id_pr_fi():
    '''
    return {id: pr}, {id: fi}
    '''
    file_PR = 'content_dfk.xlsx'
    df = pd.read_excel(file_PR)
    key = list(df['key'])
    PR = list(df['pr5'])
    FI = list(df['fi'])
    dic_id_pr = {}
    dic_id_fi = {}
    for i, k in enumerate(key):
        print(i,'====',k)
        dic_id_pr[k] = PR[i]
        dic_id_fi[k] = FI[i]
    return dic_id_pr, dic_id_fi

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

def calculate_div(dic_cited_cite, dic_id_pr, dic_id_fi, doc_topics_dict, dic_i_j_sim):
    dfk = []
    exp_dfk = []
    key = []
    cit_nums = []
    div = []
    pr = []
    fi = []
    i = 0
    time_cur = time.time()
    for cited_paper, citation_list in dic_cited_cite.items():   
#        print('K', cited_paper)
        PR_K = dic_id_pr[cited_paper]
        FI_K = dic_id_fi[cited_paper]
        t_docK = doc_topics_dict[cited_paper]    # 字典
        d_fK = 0    # dfk初始值为0
        if len(citation_list) > 1:
            # 对于大于100的那些论文随机选取100个施引文献
            select_citations = []
            if len(citation_list) > 100:
                select_list = random.sample(range(len(citation_list)),100)
                for number in select_list:
                    select_citations.append(citation_list[number])
            else:
                select_citations = citation_list
#            print('select_citations_length：', len(select_citations))
            for bi1 in range(len(select_citations)-1):
                bi1_id = int(select_citations[bi1])
#                print('bi1:', bi1_id)
                t_bi1 = doc_topics_dict[bi1_id]    # 字典
                for bi2 in range(bi1+1, len(select_citations)):
                    bi2_id = int(select_citations[bi2])
#                    print('bi2:', bi2_id)
                    t_bi2 = doc_topics_dict[bi2_id]    # 字典
                    for topic_j, P_tj_K in t_docK.items():
                        for topic_i1, P_i1_b1 in t_bi1.items():
                            for topic_i2, P_i2_b2 in t_bi2.items():
                                if dic_i_j_sim[(topic_i1, topic_j)] > 0.9:
                                    d_fK += 0
                                elif dic_i_j_sim[(topic_i2, topic_j)] > 0.9:
                                    d_fK += 0
                                else:
                                    mid = (dic_i_j_sim[(topic_i1, topic_i2)])*\
                                    (1-0.5*dic_i_j_sim[(topic_i2, topic_j)])/\
                                    (1-dic_i_j_sim[(topic_i2, topic_j)])
                                    if  mid > 1:
                                        d_fK += P_tj_K*P_i1_b1*P_i2_b2
                                    else:
                                        d_fK += P_tj_K*P_i1_b1*P_i2_b2*mid
#                                print(d_fK)
        else:
            d_fK += 0
        N = len(citation_list)
        if N > 1:
            d_fK = d_fK*2/(N*(N-1))
        else:
            d_fK = 0
        print('d_fK', d_fK)
        dfk.append(d_fK)
        d_f_k = math.exp(d_fK)
        exp_dfk.append(d_f_k)
        div_K = (PR_K - FI_K)*d_f_k
        key.append(cited_paper)
        cit_nums.append(len(citation_list))
        div.append(div_K)
        pr.append(PR_K)
        fi.append(FI_K)
        i += 1
        if i%100 == 0:
            time_now = time.time()
            print('最近100个耗时 {} s'.format(time_now-time_cur))
            time_cur = time_now
    return key, cit_nums, pr, fi, div, dfk, exp_dfk

def restore(res):
    df = pd.DataFrame()
    df['key'] = res[0]
    df['cited_num'] = res[1]
    df['pr'] = res[2]
    df['fi'] = res[3]
    df['div'] = res[4]
    df['dfk'] = res[5]
    df['exp_dfk'] = res[6]
    df.to_csv('div_singleNet_05_19.csv')   
    
if __name__ == '__main__':
    start = time.time()
    dic_cited_cite = cited_cite_dic()
    dic_id_pr_fi = id_pr_fi()
    dic_id_pr = dic_id_pr_fi[0]
    dic_id_fi = dic_id_pr_fi[1]
    doc_topics_dict = doc_topic_dic()
    dic_i_j_sim = Sim()
#    res = calculate_div()
#    restore(res)
    # test
    dfk = []
    exp_dfk = []
    key = []
    cit_nums = []
    div = []
    pr = []
    fi = []
    i = 0
    time_cur = time.time()
    for cited_paper, citation_list in dic_cited_cite.items():   
#        print('K', cited_paper)
        PR_K = dic_id_pr[cited_paper]
        FI_K = dic_id_fi[cited_paper]
        t_docK = doc_topics_dict[cited_paper]    # 字典
        d_fK = 0    # dfk初始值为0
        if len(citation_list) > 1:
            # 对于大于100的那些论文随机选取100个施引文献
            select_citations = []
            if len(citation_list) > 100:
                select_list = random.sample(range(len(citation_list)),100)
                for number in select_list:
                    select_citations.append(citation_list[number])
            else:
                select_citations = citation_list
#            print('select_citations_length：', len(select_citations))
            for bi1 in range(len(select_citations)-1):
                bi1_id = int(select_citations[bi1])
#                print('bi1:', bi1_id)
                t_bi1 = doc_topics_dict[bi1_id]    # 字典
                for bi2 in range(bi1+1, len(select_citations)):
                    bi2_id = int(select_citations[bi2])
#                    print('bi2:', bi2_id)
                    t_bi2 = doc_topics_dict[bi2_id]    # 字典
                    for topic_j, P_tj_K in t_docK.items():
                        for topic_i1, P_i1_b1 in t_bi1.items():
                            for topic_i2, P_i2_b2 in t_bi2.items():
                                if dic_i_j_sim[(topic_i1, topic_j)] > 0.9:
                                    d_fK += 0
                                elif dic_i_j_sim[(topic_i2, topic_j)] > 0.9:
                                    d_fK += 0
                                else:
                                    mid = (dic_i_j_sim[(topic_i1, topic_i2)])*\
                                    (1-0.5*dic_i_j_sim[(topic_i2, topic_j)])/\
                                    (1-dic_i_j_sim[(topic_i2, topic_j)])
                                    if  mid > 1:
                                        d_fK += P_tj_K*P_i1_b1*P_i2_b2
                                    else:
                                        d_fK += P_tj_K*P_i1_b1*P_i2_b2*mid
#                                print(d_fK)
        else:
            d_fK += 0
        N = len(citation_list)
        if N > 1:
            d_fK = d_fK*2/(N*(N-1))
        else:
            d_fK = 0
        print('d_fK', d_fK)
        dfk.append(d_fK)
        d_f_k = math.exp(d_fK)
        exp_dfk.append(d_f_k)
        div_K = (PR_K - FI_K)*d_f_k
        key.append(cited_paper)
        cit_nums.append(len(citation_list))
        div.append(div_K)
        pr.append(PR_K)
        fi.append(FI_K)
        i += 1
        if i%100 == 0:
            time_now = time.time()
            print('最近100个耗时 {} s'.format(time_now-time_cur))
            time_cur = time_now
    df = pd.DataFrame()
    df['key'] = key
    df['cited_num'] = cit_nums
    df['pr'] = pr
    df['fi'] = fi
    df['div'] = div
    df['dfk'] = dfk
    df['exp_dfk'] = exp_dfk
    df.to_csv('div_singleNet_05_19.csv')
    print(time.time()-start)
                   
                        
    