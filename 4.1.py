
# coding: utf-8

# In[8]:


from bs4 import BeautifulSoup
ecj_data = open("names.html",'r').read()

soup = BeautifulSoup(ecj_data,"html5lib")
table = soup.find_all("table")


# In[9]:


def makelist(table):
  result = []
  allrows = table.findAll('tr')
  for row in allrows:
    result.append([])
    allcols = row.findAll('td')
    for col in allcols:
      thestrings = [unicode(s) for s in col.findAll(text=True)]
      thetext = ''.join(thestrings)
      result[-1].append(thetext)
  return result


# In[10]:


table_parsed = makelist(table[2])


# In[13]:


for i in table_parsed:
    try:
        print i[0],i[1],i[2]
    except:
        continue

