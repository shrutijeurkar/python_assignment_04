
# coding: utf-8

# In[18]:


def reverse_copy(file_name):
    with open(file_name) as f:
        f2 = open(file_name[:-4]+"_reversed.txt","w")
        lines = []
        for line in f:
            lines.append(line[::-1])
        f2.writelines(lines)
        f2.close()
        
reverse_copy("sun.txt")        

