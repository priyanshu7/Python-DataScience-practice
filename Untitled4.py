
# coding: utf-8

# In[1]:


#pandas
print("Hello")
import pandas as pd

s = pd.Series()

s


# In[2]:


import numpy as np

data = np.array(['a','b','c','d'])
print(data)

s = pd.Series(data)
s


# In[3]:


#associative array (giving indexes to the array)

data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,200,300,400])
s


# In[4]:


print(s.get(100))


# In[5]:


#slicing in associative array

print(s[:2])


# In[6]:


data1 = [['john', 23],['alex', 13],['ram', 33]]
print(data1)

df=pd.DataFrame(data1)
df


# In[7]:


df=pd.DataFrame(data1, columns=['Name','Age'] , index = [1,2,3])
df


# In[8]:


data2={'Name':['Steve',"Virat",'Root'], 'Age':[27,24,31]}
print(data2)


df2=pd.DataFrame(data2)
df2


# In[9]:


#import csv files import urllib (fetches data from internet)

import urllib

myUrl="http://devanshushukla.com/hackveda.in/pythonfiles/stock.csv"

urlRequest = urllib.request.Request(myUrl)

file=urllib.request.urlopen(urlRequest)

file_url= pd.read_csv(file,sep=",",header=None,decimal=".",names=['company','eps','revenue','price','people'])
file_url


# In[11]:


import urllib

myUrl="http://devanshushukla.com/hackveda.in/pythonfiles/stock.csv"

urlRequest = urllib.request.Request(myUrl)

file=urllib.request.urlopen(urlRequest)

file_url= pd.read_csv(file,sep=",",header=None,decimal=".",names=['com','eps','revue','pre','pe'])
file_url


# In[12]:


import urllib

myUrl="http://devanshushukla.com/hackveda.in/pythonfiles/stock.csv"

urlRequest = urllib.request.Request(myUrl)

file=urllib.request.urlopen(urlRequest)

file_url= pd.read_csv(file,sep=",",header=None,decimal=".",names=['company','eps','revenue','price','people'])
file_url  #last wala print hoga, otherwise use print()
file_url.head(3)


# In[13]:


import urllib

myUrl="http://devanshushukla.com/hackveda.in/pythonfiles/stock.csv"

urlRequest = urllib.request.Request(myUrl)

file=urllib.request.urlopen(urlRequest)

file_url= pd.read_csv(file,sep=",",header=None,decimal=".")
file_url


# In[14]:


import urllib

myUrl="http://devanshushukla.com/hackveda.in/pythonfiles/stock.csv"

urlRequest = urllib.request.Request(myUrl)

file=urllib.request.urlopen(urlRequest)

file_url= pd.read_csv(file,header=None)
file_url


# In[18]:


import urllib

myUrl="http://devanshushukla.com/hackveda.in/pythonfiles/stock.csv"

urlRequest = urllib.request.Request(myUrl)

file=urllib.request.urlopen(urlRequest)

file_url= pd.read_csv(file)

print(type(file_url))

file_url


# In[21]:


#json services

import json

json_data = open("C:\\Users\\priyanshumehta\\Downloads\\data.json")

data3=json.load(json_data)
json_data.close()
data3

