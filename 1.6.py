
# coding: utf-8

# In[10]:


def write_name_file(file_name):
    with open(file_name) as f:
        f2 = open(file_name[:-4]+"_names.txt","w")
        lines = []
        for line in f:
            lines.append(line.split('/')[-1])
        f2.writelines(lines)
        f2.close()
        
write_name_file("sun.txt")  

