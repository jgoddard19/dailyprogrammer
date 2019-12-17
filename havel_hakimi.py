#!/usr/bin/env python
# coding: utf-8

# In[86]:
# Challenge #378

def rem_zero(seq):
#     take a list and return the same set with all 0's removed
    for x in range(0, len(seq)):
        if 0 in seq:
            seq.remove(0)
        else:
            return seq


# In[87]:


rem_zero([1,2,3,4,0,7,0,6])


# In[88]:


def rev_sort(seq):
    seq.sort(reverse=True)
    return seq


# In[ ]:


rev_sort([1,2,3,4,0,7,0,6])


# In[90]:


def n_len(n, seq):
    if n > len(seq):
        return True
    else:
        return False


# In[91]:


n_len(3, [1,2,3,4,0,7,0,6])


# In[92]:


n_len(10, [1,2,3,4,0,7,0,6])


# In[93]:


def subtract_one(n, seq):
    print("Before subtraction", seq)
    for x in range(n):
        seq[x] = seq[x]-1
        return seq


# In[94]:


subtract_one(4, [1,2,5,4,0,7,0,6])


# In[118]:


def Havel_Hakimi(seq):
    og_list = seq
    while(True):
        rem_zero(seq)
        print(seq, "Removed 0's")
        if len(seq) < 1:
            return True
        rev_sort(seq)
        print(seq, "Sorted in descending order")
        topval = seq.pop(0)
        print(topval, "Highest value popped")
        print(seq, "Current list")
        if n_len(topval, seq):
            return False
        subtract_one(topval, seq)


# In[119]:


Havel_Hakimi([1,2,3,4,0,7,0,6])


# In[120]:


Havel_Hakimi([5, 3, 0, 2, 6, 2, 0, 7, 2, 5])


# In[138]:


def Short_Havel(seq):
    while(True):
        for x in range(0, len(seq)):
            if 0 in seq: seq.remove(0)
            if len(seq) < 1: return True
            seq.sort(reverse=True)
            topval = seq.pop(0)
            if topval > len(seq): return False
            for x in range(topval):
                seq[x] = seq[x]-1


# In[139]:


Short_Havel([1,2,3,4,0,7,0,6])


# In[140]:


Short_Havel([5, 3, 0, 2, 6, 2, 0, 7, 2, 5])


# In[ ]:




