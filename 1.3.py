
# coding: utf-8

# In[3]:


import numpy as np
lines = []
with open("sun.txt") as f:
    for line in f:
        lines.append(line)

    


# In[13]:


max_len = 0
for i in lines:
    if len(i)> max_len:
        max_len=len(i)
    


# In[15]:


for i in lines:
    if len(i)==max_len:
        print i

