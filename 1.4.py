
# coding: utf-8

# In[8]:


def copy(file_name):
    with open(file_name) as f:
        f2 = open(file_name[:-4]+"_copied.txt","w")
        lines = []
        for line in f:
            lines.append(line)
        f2.writelines(lines)
        f2.close()
        
copy("sun.txt")        


# In[10]:


get_ipython().system(u'cat sun_copied.txt')

