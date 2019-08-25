#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:14:07 2019

@author: aashishubuntu
"""


from collections import Counter,OrderedDict
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import numpy as np
import statistics







def file_read(file):
    line=file.readlines()
    runN0=0;
    frame=[]
    file_master={}
    for i in range(0,len(line)):
        if ('========' in line[i] and i<3) or len(line[i].strip()) == 0:
            continue;
        elif ('========' in line[i]  or i==len(line)-1) and len(line[i].strip()) != 0:
            if not(not frame):
                file_master[runN0]=frame
                frame=[]
                runN0+=1
            else:
                continue
        else:
            seq=get_seq(line[i])
            frame.append(line[i])
    
    return file_master


def get_loss_burst_perc(run):
    arr=[]
    count=0
    lb={}
    temp=[]
    for frame in run:
        for idx,i in enumerate(frame):
            
            if i != 'y'and count>=1:
                arr.append(count)
                count=0
            elif i == 'y':
                 count+=1
       
        
    loss_len=Counter(arr)
    for key,value in loss_len.items():
       lb[key]=value/len(arr)*100
    return lb



def get_interval_perc(run):
    arr=[]
    count=0
    intval={}
    for frame in run:
        for idx,i in enumerate(frame):
            
            if i =='y' and count>=1:
                arr.append(count)
                count=0
            elif i!='y':
                count+=1
    print(len(arr))
    if len(arr)>0:
        interval=Counter(arr)
        print(interval)
        for key,value in interval.items():
            intval[key]=(value/len(arr)*100)
        return intval
    else:
        return 0
        

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
            


def get_all_runs(recv):
    arr=[]
    for key,value in recv.items():
         for i in value:
                arr.append(i) 
    return arr



def get_byte_loss_data(frame,length):
    arr=[]
    d={}
    st=''
    for i in range(0,len(frame)):
        st+=(frame[i])
        for k in range(0,len(st)):
            if st[k]=='y':
                arr.append(k)
        st=''
    
    byte_loss=Counter(arr)
    
    
    max_val_loc,min_val_loc,median_val_loc=[],[],[]
    maxval_val,median_val_val,min_val_val=[],[],[]
   
    max_val=max(byte_loss.values())
    min_val=min(byte_loss.values())
    median_val=round(statistics.median(byte_loss.values()))
    
    
    for key,value in byte_loss.items():
        if value > min_val and value<median_val:
            min_val_loc.append(key)
            min_val_val.append(value)
        elif value > median_val and value<max_val:
            median_val_loc.append(key)
            median_val_val.append(value)
        elif value >= max_val:
            max_val_loc.append(key)
            maxval_val.append(value)

         
    return [byte_loss,min_val_loc,min_val_val,median_val_loc,median_val_val,max_val_loc,maxval_val]



