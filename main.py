#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:30:06 2019

@author: ashubunutu
"""

from collections import Counter
import matplotlib.pyplot as plt
## From Merge 

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
        dict[seq]=0
        return dict
         
    else:
         loss_len=Counter(arr)
         dict[seq]=loss_len
         return dict
        

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
            return dict
       
    else:
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

burst_len,interval,byte_level=[],[],[]
all_runs={}
byte_indices={}

for i in range(0,len(line)):
   if ('========' in line[i] and i<3) or len(line[i].strip()) == 0:
         continue;
   elif '========' in line[i] or i==len(line)-1:
        frame.extend([burst_len,interval])
        all_runs[run]=frame
        byte_indices[run]=Counter(get_byte_loss_data(byte_level))
        burst_len=[]
        interval=[]
        frame=[]
        run+=1
   else:
        seq=get_seq(line[i])
        burst_len.append(burst_len_frame(line[i],seq))
        interval.append(get_interval_frame(line[i],seq))
        byte_level.append(line[i])
        
        

data_clensing=remove_none_type(all_runs)


## Plotting Code Starts here
#print("Total Number of Runs"+str(len(all_runs)))
#runNo=int(input('Please Enter a value between(0'+'-'+str(len(all_runs)-1)+ '): '))
#filter_val=int(input('Enter Filter Value: '))
#
#
#x,y=[],[]
#for key,value in run.items():
#    if int(value) > filter_val:
#        x.append(key)
#        y.append(value)
#plt.bar(x,y)
#plt.savefig('Crc_analysis_for_Run_no'+str(runNo)+'.png')
#plt.clf()
        
ret=get_all_buckets(10)
val=[]

i=1
res={}
run=sorted(byte_indices[1].keys())
for key,value in run.items():
   f=ret[i]
   print(key)
#   if key > f and i<len(ret)-1:
#       bucket_format=str(str(i-1)+'-'+str(i))
#       me_val=sum(val)/len(val)
#       res[bucket_format]=me_val
#       val=[]
#       bucket_format=''
#       i+=1
#   else:
#       print(value)
#       val.append(value)