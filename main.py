#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:30:06 2019

@author: ashubunutu
"""

from collections import Counter,OrderedDict
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import numpy as np
import statistics
## From Merge 

def burst_len_frame(frame,seq):
    count=0
    arr=[]
    idx=[]
    dict={}
    for i in range(0,len(frame)):
        if frame[i] != 'y'and count>=1:
            arr.append(count)
            idx.append(i)
            count=0
        elif frame[i] == 'y':
            count+=1
    if not arr:
        return []
         
    else:
         loss_len=Counter(arr)
         dict[seq]=loss_len
         return [dict,loss_len,idx]
        

def get_interval_frame(frame,seq):
    count=0;
    arr=[]
    dict={}
    for i in range(0,len(frame)):
        count+=1
        if frame[i]=='y' and count>=1:
            arr.append(count)
            count=0
            
    if  not arr:
            dict[seq]=0
            return []
       
    else:
         interval=Counter(arr)
         dict[seq]=interval
         return [dict,interval]
    

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
#     print(temp)
     d=Counter(temp)
     curr_max_vlaue=max(d.values())
     for key,value in d.items():
            if d[key] == curr_max_vlaue:
                seqNo=key
                
                break
            
     return seqNo


def remove_none_type(allruns):
    keynoto=[]
    for key,value in allruns.items():
        for val in value:
            if not val:
                keynoto.append(key)
                
    for i in keynoto:
        allruns.pop(i,None)
    return all_runs
            

def get_byte_loss_data(frame):
    arr=[]
    st=''
    for i in range(0,len(frame)):
        st+=(frame[i])
        for k in range(0,len(st)):
            if st[k]=='y':
                arr.append(k)
        st=''
            
         
    return arr

def get_all_buckets(bucket_val):
    bucket_interval=1024/bucket_val
    
    start,end=0,bucket_interval
    arr=[]
    for i in range(1,bucket_val+1):
        arr.append(start)
        start=end+1
        end=end+bucket_interval
    return arr


              

file =open('crcanalysis/24_1.txt')
line=file.readlines()
run=0;
frame=[]

burst_len,index,byte_level=[],[],[]
all_runs,all_runs_int={},{}
byte_indices={}

for i in range(0,len(line)):
   if ('========' in line[i] and i<3) or len(line[i].strip()) == 0:
         continue;
   elif '========' in line[i] or i==len(line)-1:
        
#        frame.append(burst_len)
        
        per_run=Counter(burst_len)
        per_run_interval=Counter(index)
        for key,value in per_run.items():
            per_run[key]=round(value/len(burst_len)*100)
            
        
        for key,value in per_run_interval.items():
            per_run_interval[key]=round(value/len(index)*100)
    
        all_runs[run]=per_run
        all_runs_int[run]=per_run_interval
        byte_indices[run]=Counter(get_byte_loss_data(byte_level))
        burst_len=[]
        index=[]
        frame=[]
        run+=1
   else:
        seq=get_seq(line[i])
#        burst_len.append(burst_len_frame(line[i],seq))
#        interval.append(get_interval_frame(line[i],seq))
        burst_len_ret=burst_len_frame(line[i],seq)
        interval=get_interval_frame(line[i],seq)
        if len(burst_len_ret)>0:
            burst_len_count=burst_len_ret[1]
#            print(burst_len_ret[0])
            for key,value in burst_len_count.items():
                burst_len.append(key)   
        if len(interval) >0:
            interval_cnt=interval[1]
            for key,value in interval_cnt.items():
                index.append(key)
                
            
        
        byte_level.append(line[i])
             


#Burst Len within a frame across runs
## Corruption ever 2 bytes happens 7% of the timie per 
        

data_clensing=remove_none_type(all_runs)
single_run=all_runs[7]
print(single_run)
x,y=zip(*(single_run.items()))
plt.bar(x,y)

## Interval within a frame across runns 
##  chance of corruption happening every 2 bytes is 6% the hghest

single_run_int=all_runs_int[7]
print(single_run_int)
x,y=zip(*(single_run_int.items()))
plt.bar(x,y)


ret=get_all_buckets(10)

runN0=7


run=byte_indices[runN0]
max_val=max(byte_indices[runN0].values())
min_val=min(byte_indices[runN0].values())
median_val=round(statistics.median(byte_indices[runN0].values()))

max_val_loc,min_val_loc,median_val_loc,outliers,out_inde=[],[],[],[],[]
maxval_val,median_val_val,min_val_val=[],[],[]

for key,value in run.items():
    if value > min_val and value<median_val:
        min_val_loc.append(key)
        min_val_val.append(value)
    elif value > median_val and value<max_val:
        median_val_loc.append(key)
        median_val_val.append(value)
    elif value >= max_val:
        max_val_loc.append(key)
        maxval_val.append(value)

#
plt.bar(min_val_loc,min_val_val,color='red',label='Min_val-'+str(min_val)+'Med -'+str(median_val))
plt.legend()





        
    

