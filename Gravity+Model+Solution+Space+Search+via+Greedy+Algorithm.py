#!/usr/bin/env python
# coding: utf-8

# Gravity Problem:

# In[1]:


import pandas as pd
import numpy as np
import scipy as sp
import itertools as ip


# Objective function calculator:

# In[2]:


def median_select(tup):
    W=0.0
    for i in range(len(P)):
        H=0.0
        G=0.0
        I=0.0
        for j in range(len(X_Y_existing)):
            G += 1/(((X_Y[i][0]-X_Y_existing[j][0])**2 + (X_Y[i][1]-X_Y_existing[j][1])**2)**(1/2))**(1/2)
        for j in tup:
            H += 1/(((X_Y[i][0]-X_Y_medians[j][0])**2 + (X_Y[i][1]-X_Y_medians[j][1])**2)**(1/2))**(1/2)
        for j in range(len(X_Y_all)):
            I += 1/(((X_Y[i][0]-X_Y_all[j][0])**2 + (X_Y[i][1]-X_Y_all[j][1])**2)**(1/2))**(1/2)
        W+=P[i]*(G/(H+I))
    return W


# Read data

# In[4]:


data_0=pd.read_excel("E:/EBAC/7 DMO/PKL/Assignment/Data.xlsx",0)
P=list(data_0.POPULATION)
X_Y=list(zip(data_0.X, data_0.Y))
data_1=pd.read_excel("E:/EBAC/7 DMO/PKL/Assignment/Data.xlsx",1)
X_Y_self=list(zip(data_1.X,data_1.Y))
data_2=pd.read_excel("E:/EBAC/7 DMO/PKL/Assignment/Data.xlsx",2)
X_Y_existing=list(zip(data_2.X,data_2.Y))
data_3=pd.read_excel("E:/EBAC/7 DMO/PKL/Assignment/Data.xlsx",3)
X_Y_medians=list(zip(data_3.X,data_3.Y))
X_Y_all=X_Y_self + X_Y_existing


# Minimizer function for given greedy precedence

# In[5]:


def get_minima(N,tup):
    df_result=[]
    full_set = set(range(len(X_Y_medians)))
    for subset in find_combinations(tup,full_set,N):
            print(subset)
            df_result.append([subset,median_select(subset)])
    df_result=pd.DataFrame(df_result,columns=["Store_Code","Objective_Value"])
    return df_result.Store_Code[df_result.Objective_Value.idxmin()]


# Implement greedy search for the submodular objective function

# In[6]:


def greedy_optimizer(N):
    holder=[[]]
    for i in range(N):        
        holder[0] = get_minima(1,holder)

    return holder


# Greedy combination generator

# In[7]:


def find_combinations(begin_sequences, full_set,N):
    for begin_sequence in begin_sequences:
        remaining_set = full_set - set(begin_sequence)
        for ending in ip.combinations(remaining_set,N):
            yield begin_sequence + list(ending)


# Need to open 5 new stores based on data ... get location indices in list ... lookup in excel

# In[8]:


greedy_optimizer(5)


# In[ ]:




