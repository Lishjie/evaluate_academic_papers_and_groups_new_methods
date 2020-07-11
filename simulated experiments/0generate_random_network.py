# -*- coding: utf-8 -*-
"""
@author: Rui Wang
"""


import time
import random
import pandas as pd

def init_nodes():
    node_list = [i for i in range(1000)]
    return node_list

def random_link():
    s = []
    t = []
    w = []
    N = 1000
    year = 20
    for y in range(year):
        if y == 0:
            source_start = 0
            source_end = N*(y+1)
            target_start = 0
            target_end = N*(y+1)
            for _ in range(int(N*0.3)):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
        if y == 1:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = 0
            target_end1 = N*y
            for _ in range(int(N*0.3)):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(N*1):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
        if y == 2:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = 0
            target_end1 = N*y
            for _ in range(int(N*0.3)):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(int(N*2.5)):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
        if y == 3:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = N*(y-2)
            target_end1 = N*y
            target_start2 = 0
            target_end2 = N*(y-2)
            for _ in range(int(N*0.3)):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(int(N*2.5)):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
            for _ in range(N*1):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start2,target_end2-1))
                w.append(1)
        if y == 4:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = N*(y-2)
            target_end1 = N*y
            target_start2 = 0
            target_end2 = N*(y-2)
            for _ in range(int(N*0.3)):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(int(N*2.5)):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
            for _ in range(N*2):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start2,target_end2-1))
                w.append(1)
        if y == 5:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = N*(y-2)
            target_end1 = N*y
            target_start2 = N*(y-4)
            target_end2 = N*(y-2)
            target_start3 = 0
            target_end3 = N*(y-4)
            for _ in range(int(N*0.3)): 
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(int(N*2.5)):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
            for _ in range(N*2):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start2,target_end2-1))
                w.append(1)
            for _ in range(int(N*0.6)):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start3,target_end3-1))
                w.append(1)
        if y == 6:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = N*(y-2)
            target_end1 = N*y
            target_start2 = N*(y-4)
            target_end2 = N*(y-2)
            target_start3 = N*(y-5)
            target_end3 = N*(y-4)
            target_start4 = 0
            target_end4 = N*(y-5)
            for _ in range(int(N*0.3)):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(int(N*2.5)):
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
            for _ in range(N*2):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start2,target_end2-1))
                w.append(1)
            for _ in range(int(N*0.6)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start3,target_end3-1))
                w.append(1)
            for _ in range(int(N*0.4)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start4,target_end4-1))
                w.append(1)
        if y == 7:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = N*(y-2)
            target_end1 = N*y
            target_start2 = N*(y-4)
            target_end2 = N*(y-2)
            target_start3 = N*(y-5)
            target_end3 = N*(y-4)
            target_start4 = N*(y-6)
            target_end4 = N*(y-5)
            target_start5 = 0
            target_end5 = N*(y-6)
            for _ in range(int(N*0.3)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(int(N*2.5)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
            for _ in range(N*2):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start2,target_end2-1))
                w.append(1)
            for _ in range(int(N*0.6)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start3,target_end3-1))
                w.append(1)
            for _ in range(int(N*0.4)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start4,target_end4-1))
                w.append(1)
            for _ in range(int(N*0.35)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start5,target_end5-1))
                w.append(1)
        if y == 8:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = N*(y-2)
            target_end1 = N*y
            target_start2 = N*(y-4)
            target_end2 = N*(y-2)
            target_start3 = N*(y-5)
            target_end3 = N*(y-4)
            target_start4 = N*(y-6)
            target_end4 = N*(y-5)
            target_start5 = N*(y-7)
            target_end5 = N*(y-6)
            target_start6 = 0
            target_end6 = N*(y-7)
            for _ in range(int(N*0.3)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(int(N*2.5)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
            for _ in range(N*2):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start2,target_end2-1))
                w.append(1)
            for _ in range(int(N*0.6)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start3,target_end3-1))
                w.append(1)
            for _ in range(int(N*0.4)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start4,target_end4-1))
                w.append(1)
            for _ in range(int(N*0.35)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start5,target_end5-1))
                w.append(1)
            for _ in range(int(N*0.25)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start6,target_end6-1))
                w.append(1)
        if y == 9:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = N*(y-2)
            target_end1 = N*y
            target_start2 = N*(y-4)
            target_end2 = N*(y-2)
            target_start3 = N*(y-5)
            target_end3 = N*(y-4)
            target_start4 = N*(y-6)
            target_end4 = N*(y-5)
            target_start5 = N*(y-7)
            target_end5 = N*(y-6)
            target_start6 = N*(y-8)
            target_end6 = N*(y-7)
            target_start7 = 0
            target_end7 = N*(y-8)
            for _ in range(int(N*0.3)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(int(N*2.5)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
            for _ in range(N*2):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start2,target_end2-1))
                w.append(1)
            for _ in range(int(N*0.6)): 
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start3,target_end3-1))
                w.append(1)
            for _ in range(int(N*0.4)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start4,target_end4-1))
                w.append(1)
            for _ in range(int(N*0.35)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start5,target_end5-1))
                w.append(1)
            for _ in range(int(N*0.25)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start6,target_end6-1))
                w.append(1)
            for _ in range(int(N*0.2)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start7,target_end7-1))
                w.append(1)
        if y == 10:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = N*(y-2)
            target_end1 = N*y
            target_start2 = N*(y-4)
            target_end2 = N*(y-2)
            target_start3 = N*(y-5)
            target_end3 = N*(y-4)
            target_start4 = N*(y-6)
            target_end4 = N*(y-5)
            target_start5 = N*(y-7)
            target_end5 = N*(y-6)
            target_start6 = N*(y-8)
            target_end6 = N*(y-7)
            target_start7 = N*(y-9)
            target_end7 = N*(y-8)
            target_start8 = 0
            target_end8 = N*(y-9)
            for _ in range(int(N*0.3)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(int(N*2.5)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
            for _ in range(N*2):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start2,target_end2-1))
                w.append(1)
            for _ in range(int(N*0.6)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start3,target_end3-1))
                w.append(1)
            for _ in range(int(N*0.4)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start4,target_end4-1))
                w.append(1)
            for _ in range(int(N*0.35)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start5,target_end5-1))
                w.append(1)
            for _ in range(int(N*0.25)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start6,target_end6-1))
                w.append(1)
            for _ in range(int(N*0.2)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start7,target_end7-1))
                w.append(1)
            for _ in range(int(N*0.15)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start8,target_end8-1))
                w.append(1)
        if y == 11:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = N*(y-2)
            target_end1 = N*y
            target_start2 = N*(y-4)
            target_end2 = N*(y-2)
            target_start3 = N*(y-5)
            target_end3 = N*(y-4)
            target_start4 = N*(y-6)
            target_end4 = N*(y-5)
            target_start5 = N*(y-7)
            target_end5 = N*(y-6)
            target_start6 = N*(y-8)
            target_end6 = N*(y-7)
            target_start7 = N*(y-9)
            target_end7 = N*(y-8)
            target_start8 = N*(y-10)
            target_end8 = N*(y-9)
            target_start9 = 0
            target_end9 = N*(y-10)
            for _ in range(int(N*0.3)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(int(N*2.5)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
            for _ in range(N*2):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start2,target_end2-1))
                w.append(1)
            for _ in range(int(N*0.6)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start3,target_end3-1))
                w.append(1)
            for _ in range(int(N*0.4)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start4,target_end4-1))
                w.append(1)
            for _ in range(int(N*0.35)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start5,target_end5-1))
                w.append(1)
            for _ in range(int(N*0.25)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start6,target_end6-1))
                w.append(1)
            for _ in range(int(N*0.2)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start7,target_end7-1))
                w.append(1)
            for _ in range(int(N*0.15)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start8,target_end8-1))
                w.append(1)
            for _ in range(int(N*0.1)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start9,target_end9-1))
                w.append(1)
        if y == 12:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = N*(y-2)
            target_end1 = N*y
            target_start2 = N*(y-4)
            target_end2 = N*(y-2)
            target_start3 = N*(y-5)
            target_end3 = N*(y-4)
            target_start4 = N*(y-6)
            target_end4 = N*(y-5)
            target_start5 = N*(y-7)
            target_end5 = N*(y-6)
            target_start6 = N*(y-8)
            target_end6 = N*(y-7)
            target_start7 = N*(y-9)
            target_end7 = N*(y-8)
            target_start8 = N*(y-10)
            target_end8 = N*(y-9)
            target_start9 = N*(y-11)
            target_end9 = N*(y-10)
            target_start10 = 0
            target_end10 = N*(y-11)
            for _ in range(int(N*0.3)): 
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(int(N*2.5)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
            for _ in range(N*2):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start2,target_end2-1))
                w.append(1)
            for _ in range(int(N*0.6)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start3,target_end3-1))
                w.append(1)
            for _ in range(int(N*0.4)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start4,target_end4-1))
                w.append(1)
            for _ in range(int(N*0.35)): 
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start5,target_end5-1))
                w.append(1)
            for _ in range(int(N*0.25)): 
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start6,target_end6-1))
                w.append(1)
            for _ in range(int(N*0.2)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start7,target_end7-1))
                w.append(1)
            for _ in range(int(N*0.15)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start8,target_end8-1))
                w.append(1)
            for _ in range(int(N*0.1)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start9,target_end9-1))
                w.append(1)
            for _ in range(int(N*0.05)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start10,target_end10-1))
                w.append(1)
        if y > 12:
            source_start = N*y
            source_end = N*(y+1)
            target_start = N*y
            target_end = N*(y+1)
            target_start1 = N*(y-2)
            target_end1 = N*y
            target_start2 = N*(y-4)
            target_end2 = N*(y-2)
            target_start3 = N*(y-5)
            target_end3 = N*(y-4)
            target_start4 = N*(y-6)
            target_end4 = N*(y-5)
            target_start5 = N*(y-7)
            target_end5 = N*(y-6)
            target_start6 = N*(y-8)
            target_end6 = N*(y-7)
            target_start7 = N*(y-9)
            target_end7 = N*(y-8)
            target_start8 = N*(y-10)
            target_end8 = N*(y-9)
            target_start9 = N*(y-11)
            target_end9 = N*(y-10)
            target_start10 = N*(y-12)
            target_end10 = N*(y-11)
            target_start11 = 0
            target_end11 = N*(y-12)
            for _ in range(int(N*0.3)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start,target_end-1))
                w.append(1)
            for _ in range(int(N*2.5)): 
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start1,target_end1-1))
                w.append(1)
            for _ in range(N*2):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start2,target_end2-1))
                w.append(1)
            for _ in range(int(N*0.6)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start3,target_end3-1))
                w.append(1)
            for _ in range(int(N*0.4)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start4,target_end4-1))
                w.append(1)
            for _ in range(int(N*0.35)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start5,target_end5-1))
                w.append(1)
            for _ in range(int(N*0.25)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start6,target_end6-1))
                w.append(1)
            for _ in range(int(N*0.2)): 
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start7,target_end7-1))
                w.append(1)
            for _ in range(int(N*0.15)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start8,target_end8-1))
                w.append(1)
            for _ in range(int(N*0.1)):   
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start9,target_end9-1))
                w.append(1)
            for _ in range(int(N*0.05)):    
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start10,target_end10-1))
                w.append(1)
            for _ in range(int(N*0.1)):  
                s.append(random.randint(source_start, source_end-1))
                t.append(random.randint(target_start11,target_end11-1))
                w.append(1)
    return s, t, w

def filt(s, t):
    dic = {}
    for i in range(len(s)):
        if s[i] in dic:
            if t[i] not in dic[s[i]]:
                dic[s[i]].append(t[i])
        else:
            dic[s[i]] = []
            if t[i] not in dic[s[i]]:
                dic[s[i]].append(t[i])
    ns = []
    nt = []
    nw = []
    for s in dic:
        for t in dic[s]: 
            nt.append(t)
            ns.append(s)
            nw.append(1)
    return ns, nt, nw

if __name__ == '__main__':
    start = time.time()
    links = random_link()
    print(len(links[0]))
    filted = filt(links[0], links[1])
    df = pd.DataFrame()
    print(len(filted[0]))
    df[0] = filted[0]
    df[1] = filted[1]
    df[2] = filted[2]
    df.to_csv('testNet4_1000_20_6.csv', index = None, header = None)
    print(time.time()-start)


















