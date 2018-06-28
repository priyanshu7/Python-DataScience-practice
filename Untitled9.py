
# coding: utf-8

# In[2]:


import pandas as pd
print('imported panda success')


# In[5]:


print('Date for formatting : ',pd.to_datetime(['20181215','somestring'],format='%Y%m%d',errors='ignore') ) #ignore coerce raise


# In[3]:


date1={'Year': [2018,2019,2020], 'Month' : [1,2,3] , 'Day': [12,13,14] }
print(date1)


# In[4]:


date1=pd.DataFrame({'Year': [2018,2019,2020], 'Month' : [1,2,3] , 'Day': [12,13,14] })
print(date1)


# In[7]:


date1=pd.DataFrame({'Year': [2018,2019,2020], 'Month' : [1,2,3] , 'Day': [12,13,14] })

print(date1)

pd.to_datetime(date1)


# In[10]:


Data = pd.read_csv("F:\ebooks\stock.csv",parse_dates=[0])
Data


# In[11]:


Data = pd.read_csv("F:\ebooks\stock.csv", skiprows=1)
Data


# In[12]:


Data = pd.read_csv("F:\ebooks\stock.csv", header=None)
Data


# In[15]:


Data = pd.read_csv("F:\ebooks\stock.csv", nrows=3)
Data


# In[16]:


Data = pd.read_csv("F:\ebooks\stock.csv",na_values=['not available' , 'n.a.'])
Data


# In[18]:


#create csv file

Data.to_csv('F:\\ebooks\\new.csv')


# In[19]:


Data.to_csv('F:\\ebooks\\new.csv', index='False' , header =None) #header none removes the column heads


# In[20]:


read = pd.read_excel("F:\\ebooks\\sample.xls")
read


# In[21]:


read = pd.read_excel("F:\\ebooks\\sample.xls", "Sheet2")
read

