
# coding: utf-8

# In[1]:


def greet(name):
    """this function is going 
    to greet user"""
    print ("Hello "+name+" .Good Evening")

name = input("Enter your name")
greet(name)
    


# In[ ]:


def sum(num1,num2):
    
    


# In[2]:


def absolute_val(num):
    
    if num>=0:
        return num
    else:
        return num+1
print(absolute_val(0))


# In[3]:


def absolute_val(num):
    
    if num>=0:
        return num
    else:
        return num+1
print(absolute_val(-4.3))


# In[5]:


print(max(12,15,22876,3456865,5))


# In[6]:


sort=(5,3,1,7,4,9,2)
print(sorted(sort))


# In[7]:


print(sum(sort))


# In[11]:


names=['Priyanshu','divyanshu','manav']
print(names)
print(names[4])


# In[13]:


#nested lists

mylist=['Happy',[2,0,1,8]]
print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[1][2])
print(mylist[0][2])


# In[14]:


#negative indexing

list1=[1,2,3,4] #-4 -3 -2 -1
print(list1[-3])


# In[17]:


#slicing

list2=['p','r','o','g','r','a','m']
print(list2[2:5])
print(list2[:-5])
print(list2[:5])
print(list[:])


# In[18]:


old=[1,2,3]
print(old)
old[0]=10
print(old)


# In[19]:


old[0:2]=[2,1]
print(old)


# In[20]:


old[0:4]=[2,1,4,5]
print(old)


# In[22]:


list3=[1,9]
print(list3)
list3.insert(1,3)
print(list3)

list3[2:2]=[5,7]
print(list3)


# In[25]:


list2=['p','r','o','g','r','a','m']
print(list2)

del(list2[4:6])
print(list2)


# In[29]:


listn=['n','i','t','i','n']
listn.remove('n')
print(listn)

listn.remove('n')
print(listn)
listn.remove('n')
print(listn)


# In[31]:


list1=[10,20]
list2=[30,40]

list1=list1+list2
print(list1)


# In[39]:


dict1={1:'Priyanshu',2:'Manav',3:'Divs'}

print(dict1)

print(dict1[3])

print(dict1.get(3))

print(dict1.get(1))


# In[40]:


#update dictionary

dict1[1]="Priyanshu Mehta"
print(dict1)


# In[41]:


dict1[5]='Siddhant'
print(dict1)


# In[42]:


dict1[5]='Rishabh'
print(dict1)


# In[43]:


dict1.pop(3)


# In[47]:


del dict1[2]
print(dict1)

