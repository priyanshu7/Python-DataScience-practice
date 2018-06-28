
# coding: utf-8

# In[3]:


num= 2    
if num<3:
       print ( "Hello" )
elif num==3:
       print ( "BYE")
       print (num)
      


# In[9]:


age = [0,0,0]
age[0]= input('enter age of first person:')
age[1]= input('enter age of second person:')
age[2]= input('enter age of third person:')
if age[0]>age[1] and age[0]>age[2]:
    print('First person is eldest')
elif age[1]>age[0] and age[1]>age[2]:
    print('Second person is eldest')
elif age[2]>age[0] and age[2]>age[1]:
    print('third person is eldest')
else:
    print('all have equal age')


# In[11]:


number=[10,20,30,40,50,60]
sum=0
for val in number[2:6]:
    sum=sum+val
print(sum)


# In[12]:


music = ['pop','rock','jazz','sufi']
for i in range(len(music)):
    print('I like ',music[i],' music')
    


# In[14]:


music = ['pop','rock','jazz','sufi']
for i in range(len(music)):
    print('I like ',music[i],' music',end=" ")


# In[17]:



for i in range(1,100):
    print (i)


# In[24]:


num=int(input('Enter any number'))
fact=1
if num<0:
    print('Negative number not allowed')
elif num==0:
    print('Factorial of zero is 1')
else:
   for i in range(1,num+1):
       fact=fact*i
print (fact)


# In[1]:


num=1
while num<11:
    print(num)
    num=num+1


# In[4]:


n=10
sums=0
i=1
while i<=n:
    sums=sums+i
    i=i+1
print(sums)
    


# In[5]:


n=10
p=13
i=1
while i<=n:
    print('13 * ',i,'=',p*i)
    i=i+1

