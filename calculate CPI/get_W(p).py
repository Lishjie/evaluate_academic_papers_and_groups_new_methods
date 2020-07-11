# -*- coding: utf-8 -*-
import pandas as pd
import time
start = time.time()

#df = pd.read_csv('./before_W(p)/2005.csv')
#df_2005_id = pd.read_csv('./pr_id_year/2005.csv')
#key_list = list(df_2005_id['key'])
#df_2005 = df[df.key.isin(key_list)]
#sum_first_year = sum(df_2005.PR)
#num_first_year = df_2005.shape[0]
#same_ave = sum_first_year/num_first_year

# 保持均值一样
#for i in range(2006, 2015):
#    print(i)
#    df_cur = pd.read_csv('./before_W(p)/'+str(i)+'.csv')
#    df_year = pd.read_csv('./pr_id_year/'+str(i)+'.csv')
#    cur_year_list = list(df_year['key'])
#    df_cur_year = df_cur[df_cur.key.isin(cur_year_list)]
#    nums2 = df_cur_year.shape[0]
#    sum2 = sum(df_cur_year.PR)
#    df_cur['PR_same_ave'] = df_cur['PR'].map(lambda x: x*same_ave*nums2/sum2)  
#    test_df = df_cur[df_cur.key.isin(cur_year_list)]
#    print(sum(test_df['PR_same_ave'])/nums2)
#    df_cur.to_csv('./wp_first_year_same_ave/'+str(i)+'.csv')

## 拼接
#l = []
#for i in range(2005, 2015):
#    print(i)
#    key_list = list(pd.read_csv('./pr_id_year/'+str(i)+'.csv')['key'])
#    df = pd.read_csv('./wp_first_year_same_ave/'+str(i)+'.csv')
#    df[df.key.isin(key_list)].to_csv('./wp_first_year_same_ave/same_ave_'+str(i)+'.csv')
#    print(df[df.key.isin(key_list)].shape)
#    
#    df = pd.read_csv('./wp_first_year_same_ave/'+str(i)+'.csv')
#    df = pd.read_csv('./wp_first_year_same_ave/same_ave_'+str(i)+'.csv')
#    l.append(df)
#    print(df.shape)
#df_final = pd.read_csv('./wp_first_year_same_ave/same_ave_'+str(2014)+'.csv')
#df = pd.concat(l)
#df.to_csv('./wp_first_year_same_ave/same_first_year_ave_first_year_before_Wp.csv', index = None)
#
## 填充
#df_all = pd.read_csv('./wp_first_year_same_ave/same_first_year_ave_all_year_before_Wp.csv')
#df_already = pd.read_csv('./wp_first_year_same_ave/same_first_year_ave_first_year_before_Wp.csv')
#key_list = list(df_already['key'])
#df = df_all[~df_all.key.isin(key_list)]
#df1 = df.drop_duplicates(['key'])    # 去重函数, 计算过，但是没被保留下来的
##df1.to_csv('./wp_first_year_same_ave/0.csv', index = None)    # 把计算过但是没保存下来的存储
##df1 = pd.read_csv('./wp_first_year_same_ave/0.csv')
##df = pd.read_csv('./wp_first_year_same_ave/same_ave_05_14_before_Wp.csv')
#df2 = pd.concat([df_already, df1])
#df3 = df2.drop_duplicates(['key'])
#df3.to_csv('wp_first_year_same_ave/wp_already_cal_05-19.csv', index = None)
#
## 检查剩下的那些都是哪年的
#df_year = pd.read_excel('graph_list_05_19_id_year.xlsx')
#df_year[~df_year['key'].isin(list(df3.key))].to_csv('wp_first_year_same_ave/havent_been_cal.csv', index = None)
## 经过验证,原因确实和之前猜想的一样,这里存储还是为了修改他们的pr值
#
## 最后没有的那几千个用最小值填充
#df4 = pd.read_csv('wp_first_year_same_ave/havent_been_cal_pr.csv')
#df5 = pd.concat([df3, df4])
#df6 = df5.drop_duplicates(['key'])  
#df5.to_csv('wp_first_year_same_ave/all_wp_before_normal.csv', index = None)
#
## 归一化
#key_list = list(pd.read_csv('graph_list_05_19.csv')['key'])
#df7 = pd.read_csv('wp_first_year_same_ave/all_wp_before_normal.csv')
#key = list(df7['key'])
#value = list(df7['PR'])
#dic = {}
#for i, e in enumerate(key):
#    print(i, '===', e)
#    dic[e] = value[i]
#
#l = []
#l_ave = []
#for j, k in enumerate(key_list):
#    print(j)
#    l.append(dic[k])
#    l_ave.append(dic[k]/5127.76487148722)
#    
#df1 = pd.DataFrame()
#df1['key'] = key_list
#df1['PR'] = l_ave
#df1.to_csv('./wp_first_year_same_ave/wp_final_normal.csv')






















