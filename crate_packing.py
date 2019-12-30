#!/usr/bin/env python
# coding: utf-8

# In[17]:


import math

def fit1(X, Y, x, y):
    print(X, Y, x, y)
    xaxis = math.floor(X/x)
    yaxis = math.floor(Y/y)
    total = xaxis*yaxis
    print(total)
    return total


# In[19]:


fit1(25, 18, 6, 5)


# In[20]:


fit1(10, 10, 1, 1)


# In[27]:


def fit2(X, Y, x, y):
    print(X, Y, x, y)
    total = math.floor(X/x)*math.floor(Y/y)
    total_rotate = math.floor(X/y)*math.floor(Y/x)
    return max(total, total_rotate)


# In[28]:


fit2(25, 18, 6, 5)


# In[29]:


fit2(12, 34, 5, 6)


# In[30]:


def fit3(X, Y, Z, x, y, z):
    print(X, Y, Z, x, y, z)
    total = math.floor(X/x)*math.floor(Y/y)*math.floor(Z/z)
    total1 = math.floor(X/y)*math.floor(Y/z)*math.floor(Z/x)
    total2 = math.floor(X/z)*math.floor(Y/x)*math.floor(Z/y)
    return max(total, total1, total2)


# In[31]:


fit3(10, 10, 10, 1, 1, 1)


# In[33]:


fit3(123, 456, 789, 10, 11, 12)


# In[ ]:




