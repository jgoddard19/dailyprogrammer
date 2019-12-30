#!/usr/bin/env python
# coding: utf-8

# In[25]:


def check_balance_xy(str):
    print("Initial string", str)
    xcount = 0
    ycount = 0
    for x in range(0, len(str)):
        if str[x] == "x":
            xcount+=1
        elif str[x] == "y":
            ycount+=1
    if xcount == ycount:
        return True
    else: 
        return False


# In[26]:


check_balance_xy("xxyy")


# In[27]:


check_balance_xy("xyy")    


# In[28]:


check_balance_xy("")


# In[91]:


def check_balance(str):
    print("Initial string", str)
    strlist = list(str)
    print("strlist", strlist)
    unique_list = []
    count_list = []
#     create unique list of values
    for x in strlist:
        if x not in unique_list:
            unique_list.append(x)
#     loop through the unique list, counting occurrences in the original list
    for x in unique_list:
        charcount = strlist.count(x)
        count_list.append(charcount)
#     check the list of counted unique values to see if all the numbers match up
    if(len(set(count_list))==1):
        print("The string is balanced")
        return True
    else:
        print("The string is not balanced")
        return False


# In[92]:


check_balance("xxyyab")


# In[93]:


check_balance("xxxxnnnnnx")


# In[94]:


check_balance("xyxyxyxy")


# In[95]:


check_balance("")


# In[ ]:




