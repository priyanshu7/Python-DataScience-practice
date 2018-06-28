
# coding: utf-8

# In[6]:


#hierarchical indexing

import pandas as pd

raw_data={'city':['Delhi','Delhi','Mumbai','Mumbai','Chennai','Chennai'], 'rank':['1st','2nd','1st','2nd','1st','2nd'], 
          'name':['A','B','C','D','E','F'], 'score1':[33,44,55,66,77,88],'score2':[54,25,76,54,87,39]}
df=pd.DataFrame(raw_data,columns=['city','rank','name','score1','score2'])
df


# In[7]:


df1=df.set_index(['city','rank'],drop=False) 
df1


# In[8]:


df2=df.set_index(['city','rank'],drop=True) 
df2


# In[9]:


raw_data={'city':['Delhi','Delhi','Mumbai','Mumbai','Chennai','Chennai'], 'rank':['1st','2nd','1st','2nd','1st','2nd'], 
          'name':['A','B','C','D','E','F'], 'score1':[33,44,55,66,77,88],'score2':[54,25,76,54,87,39]}

df_new=pd.DataFrame(raw_data,
                   index=pd.Index(['A','B','C','D','E','F'],name='myIndex'),
                   columns=pd.Index(['city','rank','name','score1','score2'],name='myCol'))
df_new


# In[13]:


address = pd.read_csv("F:\mtcars.csv")
address


# In[12]:


#Data Aggregation

cars_groups= address.groupby(['cyl'])
cars_groups


# In[15]:


cars_groups= address.groupby(address['cyl'])
print(cars_groups)


# In[16]:


cars_groups.mean()


# In[17]:


cars_groups.max()


# In[18]:


cars_groups.min()

