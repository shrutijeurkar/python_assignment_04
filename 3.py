
# coding: utf-8

# In[19]:


f = open("marks.txt")
lines = []
for line in f:
    lines.append(line.split())


# In[20]:


lines = [lines[1][-3:],lines[3][-3:],lines[5][-3:]]


# In[24]:


import numpy as np
lines = np.array(lines)


# In[28]:


lines = lines.astype(float)


# In[30]:


print "studentwise sum:"
for i in lines:
    print sum(i)


# In[37]:


print "subjectiwise sum:"
lines_tr = lines.transpose()
for i in lines_tr:
    print sum(i)

