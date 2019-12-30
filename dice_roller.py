#!/usr/bin/env python
# coding: utf-8

# In[229]:


import random

def dice_roll(roll):
    
    rolls = roll.split(' ')
    print(roll, rolls)
    total = 0
    
    for i in range(len(rolls)):
        roll_list = list(rolls[i])
        dice = int(rolls[i].split('d')[0])
        print("dice:", dice)
        sides = int(rolls[i].split('d')[1])
        print("sides:", sides)
        newlist = list(rolls[i])

        result = dice*random.randrange(1, sides)
        total = total + result
        print(result)
    
    return total
    


# In[230]:


dice_roll("3d4 5d6")


# In[231]:


dice_roll("5d12 1d6 4d20")


# In[ ]:




