#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:34:56 2019

@author: aashishubuntu
"""
from require import *
import matplotlib.pyplot as plt

def plot_burst_len(run,path_to_file,frame_rate):
    for key,value in run.items():
        fig,ax=plt.subplots(nrows=1,ncols=2,sharex=False,sharey=False,squeeze=False)
        loss_burs=get_loss_burst_perc(value)
        lists=loss_burs.items()
        x, y = zip(*lists)
        ax[0][0].bar(x,y)
        ax[0][0].set_xlabel('Loss Burst Len')
        ax[0][0].set_ylabel('percent')

        interval=get_interval_perc(value)
#        print(interval)
        lists=interval.items()
        x, y = zip(*lists)
        print(x,y)
        ax[0][1].bar(x,y)
        ax[0][1].set_xlabel('Interval')
        ax[0][1].set_ylabel('Pmf')
        fig.suptitle(str(path_to_file.split('/')[1])+path_to_file[path_to_file.index('Node'):path_to_file.rfind('/')]+':'+'loss Burst Perc and interval for Run_no'+str(key))
        fig.savefig(str(path_to_file)+'Pmf_Run_no'+str(key)+'.png')
        fig.clf()
        plt.close(fig)
     
    return 0

def plot_consolidated_run_master(receivers,path):
    """
    this function plots across all runs the pmf for burst len and interval per receiver
    input: Array of all receivers raw Data 'Y' and 'N'
    rtype= none    
    """ 
    ## Aggragated Pmf Master
    nrows=3
    ncols =2

    fig,ax=plt.subplots(nrows,ncols,figsize=(20,10))
    i=0
    while i < nrows:
        j=0
        while j < ncols:
            receiver=get_all_runs(receivers[i])
            ret=get_loss_burst_perc(receiver)
            lists=ret.items()
            x,y=zip(*lists)
            ax[i][j].bar(x,y)
            ax[i][j].set_title('Burst Len  Vs Perc across all runs Node'+str(i+1),fontsize=10,pad=-10)  
            j+=1
            ret=get_interval_perc(receiver)
            lists=ret.items()
            x,y=zip(*lists)
            ax[i][j].bar(x,y)
            ax[i][j].set_title('Interval Vs Perc across all runs Node'+str(i+1),fontsize=10,pad=-10)
            j+=1
    
        i+=1

    fig.suptitle('Plot Recv wise aggregation of Burse size and Interval for'+path.split('/')[1])
    fig.savefig(path+'/Aggregared.png')
    plt.close(fig)
    return 0



