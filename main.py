#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:30:06 2019

@author: ashubunutu
"""

from require import *
from plot_vizualization_master import *
import os

from collections import Counter,OrderedDict


file =open('crcanalysis/24_1.txt')
line=file.readlines()


frame1=24
dirName='img/'+str(frame1)+'Mbps'

try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")


for i in range (1,5):
    try:
        st=dirName+'/Node_'+str(i)
        os.mkdir(st)
        print("Directory " , st ,  "Created")
    except FileExistsError:
        print("Directory " , st ,  " already exists")

st='img/'+str(frame1)+'Mbps'+'/Node_1/Run_no'

name= open("crcanalysis/"+str(frame1)+"_1.txt")
name_1=open("crcanalysis/"+str(frame1)+"_2.txt")
name_2=open("crcanalysis/"+str(frame1)+"_3.txt")



recv_1=file_read(name)
recv_2=file_read(name_1)
recv_3=file_read(name_2)



arr=[recv_1,recv_2,recv_3]


st=''
inte={}
#
#for key,value in recv_4.items():
#      print(key)
#      inte[key]=get_interval_perc(value)
#
#print(len(inte))

for i,value in enumerate(arr):
    if i == 0:
        st=dirName+'/Node_1/Run_no'
    elif i ==1:
         st=dirName+'/Node_2/Run_no'
    elif i==2:
        st=dirName+'/Node_3/Run_no'

    
    plot_burst_len(value,st,frame1) 


path=dirName
plot_consolidated_run_master(arr,path)


    

  # used to compuet pmf and interval across all runs



#Burst Len within a frame across runs
## Corruption ever 2 bytes happens 7% of the timie per 
        






        
    

