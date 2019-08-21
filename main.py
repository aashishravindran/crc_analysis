#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:30:06 2019

@author: ashubunutu
"""

from collections import Counter


def burst_len_frame(frame,seq):
    count=0
    arr=[]
    dict={}
    for i in range(0,len(frame)):
        if frame[i] != 'y'and count>=1:
            arr.append(count)
            count=0
        elif frame[i] == 'y':
            count+=1
    if not arr:
         loss_len=Counter(arr)
         dict[seq]=loss_len
         return dict
    return None

def get_interval_frame(frame,seq):
    count=0;
    arr=[]
    dict={}
    for i in range(0,len(frame)):
        count+=1
        if frame[i]=='y' and count>=1:
            arr.append(count)
            count=0
    interval=Counter(arr)
    dict[seq]=interval
    
    return dict
    
    



def get_seq(frame):
#    print(frame)
     temp=[]
     st=''
     seqNo=''
    
     for i in frame:
            if i!='a' and i !='y':
                st+=i   
                if len(st)==3:
                    temp.append(st)
                    st=''
     print(temp)
     d=Counter(temp)
     curr_max_vlaue=max(d.values())
     for key,value in d.items():
            if d[key] == curr_max_vlaue:
                seqNo=key
                
                break
            
     return seqNo
        
                   


file =open('crcanalysis/24_1.txt')
line=file.readlines()
run=0;
frame=[]
burst_len,interval=[],[]
all_runs={}
for i in range(0,len(line)):
   if ('========' in line[i] and i==2) or len(line[i].strip()) == 0:
         continue;
   elif '========' in line[i]:
        frame.extend([burst_len,interval])
        all_runs[run]=frame
        burst_len=[]
        interval=[]
        frame=[]
        run+=1
   else:
        
        seq=get_seq(line[i])
        burst_len.append(burst_len_frame(line[i],seq))
        interval.append(get_interval_frame(line[i],seq))

    
        
        
    
    