
# coding: utf-8

# In[10]:


#data science in python

#numpy

import numpy as np

a = np.array([1,2,3])

print(type(a))

print(a.shape)

print(a)

a[0]=5

print(a)


b=np.array([[1,2,3],[4,5,6]])

print (b.shape)


# In[13]:


print(np.zeros((2,2)))

print(np.ones((1,4)))

print(np.full((8,8),100))


# In[16]:


print(np.ones((2,4,5,7)))


# In[24]:


#size and type of data in array

x = np.array([1,2])
print(x.dtype)

y=np.array(["divyanshu",'Priyanshu'])
print(y.dtype)

z=np.array([4,5], dtype=np.int64)
print(z.dtype)


# In[31]:


#sum of matrices
arr1= np.array([[1,2],[3,4]])
arr2= np.array([[1,2000],[33456,4]])
print ( arr1+arr2)

print(np.add(arr1,arr1))
print


# In[37]:


arr3=np.array([[1,12,5],[13,4,7]])
print(np.sum(arr3))
print(arr3.shape)

print(np.sum(arr3 , axis=0)) #vertical


print(np.sum(arr3 , axis=1)) #horizontal


# In[38]:


#transpose of  a matrix
print(arr3)
print(arr3.T)


# In[39]:


#sorting in array

print(np.sort(arr3))

