
# coding: utf-8

# In[8]:


def check_duplicate(file_name):
    flag = "Duplicates Not Found"
    with open(file_name) as f:
        lines = []
        for line in f:
            lines.append(line.split('/')[-1])
#         print lines
        for i in range(len(lines)):
            for j in range(len(lines)):
                if lines[i]==lines[j]and i !=j:
                    flag = "Duplicates Found"
                    print "Duplicate: ",i ,j, " ", lines[i]
        print flag
        
check_duplicate("sun.txt")  

