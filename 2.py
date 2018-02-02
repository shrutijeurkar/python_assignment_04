
# coding: utf-8

# In[1]:


f1 = open("file_A.txt")
f2 = open("file_B.txt")

a = [int(i[:-2]) for i in f1]
b = [int(i[:-2]) for i in f2]


# In[2]:


a = set(a)
b = set(b)


# In[4]:


print "common_elements :", a.intersection(b)


# In[5]:


f1.close()
f2.close()

