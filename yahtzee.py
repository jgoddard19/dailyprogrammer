#!/usr/bin/env python
# coding: utf-8

# In[80]:


def upper(seq):
    print(seq)
    dupeSet = []
    maxVal = 0
    for i in range(len(seq)):
        if len(seq) == len(set(seq)):
#         no duplicates in the list--return the highest value
            return max(seq)
        if seq.count(seq[i]) > 1:
            dupeSet.append([seq[i], seq.count(seq[i])])
            for j in range(len(dupeSet)):
#                 if dupeSet[j][0]*dupeSet[j][1] > maxVal:
#                     maxVal = dupeSet[j][0]*dupeSet[j][1]
                calc = dupeSet[j][0]*dupeSet[j][1]
                if calc > maxVal:
                    maxVal = calc
    
    return maxVal


# In[81]:


upper([1,2,3,5,6,6])


# In[82]:


upper([0,0,0,0,0,0])


# In[83]:


upper([1,2,3,4,5,6])


# In[84]:


upper([1654, 1654, 50995, 30864, 1654, 50995, 22747, 1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654, 30864, 4868, 30864])


# In[ ]:




