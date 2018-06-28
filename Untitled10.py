
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv("H:\weather1.csv")
df


# In[3]:


#max temp in data

a = df['Temperature'].max()

print(a)


# In[4]:


#mean

df['Temperature'].mean()


# In[8]:


#days of rain

df['EST'][df['Events']=='Rain']


# In[9]:


#days of rain

df['EST'][df['Events']=='NaN']


# In[10]:


df['WindSpeedMPH'].mean()


# In[11]:


#cleaning up of data array

#fill NAN
df.fillna(0,inplace=True) #permission 

df['WindSpeedMPH'].mean()


# In[12]:


df1=pd.read_csv('H:\weather_data.csv')
df1new


# In[14]:


type(df1.day[0])


# In[15]:


type(df1.temperature[0])


# In[16]:


type(df1.event)


# In[17]:


#change date format

df2=pd.read_csv('H:\weather_data.csv', parse_dates=['day'])
df2


# In[19]:


new_df = df2.fillna(10)
new_df


# In[21]:


new_df = df2.fillna({'event':'ROMANTIC' , 'temperature':'HOT','windspeed':100})
new_df


# In[23]:


new_df = df2.fillna(method='ffill') #filled by previous value
new_df


# In[24]:


new_df = df2.fillna(method='bfill') #filled by next value
new_df


# In[25]:


df1=pd.read_csv('H:\weather_data.csv')
df1


# In[26]:


new_df=df.fillna(method='bfill',axis='column')
new_df


# In[28]:


new_df=df1.fillna(method='bfill',axis='columns')
new_df


# In[29]:


type(new_df.day[0])


# In[37]:


new_df=df1.fillna(method='ffill',axis='columns',limit=1) #apply fill to the limited column/rows
new_df


# In[39]:


new_df=df1.interpolate()    #guess values in table integer float double
new_df


# In[40]:


new_df=df1.dropna()  #drop nan
new_df


# In[49]:


new_df=df1.dropna(thresh=2)  #drop nan
new_df

