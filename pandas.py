#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


obj = pd.Series([4, -7, -5, 3])
obj


# In[5]:


print (obj.values)
print (obj.index)


# In[9]:


obj = pd.Series([4, -7, -5, 3], index = ["four", 'minus seven', 'minus five', 'three'])
obj


# In[10]:


print(obj[['three','minus five']])


# In[11]:


print(obj[obj < 0])


# In[13]:


print(obj*3)


# In[14]:


from numpy import exp
print (exp(obj))


# In[17]:


print(4 in obj)


# In[18]:


voc = {"Ohio": 35000, "Texas":71000, "Oregon":16000, "Utah":50000}
obj = pd.Series(voc)
obj


# In[20]:


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada','Nevada','Nevada'],
        'year': ['2000','2001','2002','2000','2001','2002'],
        'population': ['35000','37000','38000','29000','32000','31000']}
data


# In[23]:


df=pd.DataFrame(data)
df


# In[24]:


df = pd.DataFrame(data,columns = ['population','year','state'])
df


# In[27]:


df = pd.DataFrame(data,columns = ['population','year','state','Nan'], index = ['one','two','three', 'four', 'five', 'six'])
df


# In[28]:


df["year"]


# In[30]:


df.loc['six']


# In[32]:


df['Nan'] = 'Nan'
df


# In[59]:


inventory_dict = dict(right_hand='sword', left_hand='shield')


# In[62]:


h=dict(g='s', l='d')
h


# In[66]:


t = 'gl'
for i in h.keys():
    print(h[i], end='')


# In[69]:


for i in t: 
    print(h[i])


# In[ ]:




