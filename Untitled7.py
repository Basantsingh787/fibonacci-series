#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to print a dictionary whose keys should
#be the alphabet from a-z and the value should be corresponding ASCII values
# Create the dictionary
x={}
n1=int(input("enter the number from where range start"))
n2=int(input("enter the number end of range"))
for i in range(n1,n2+1):
     x[chr(i)] = i
print("dictionary = " , x)


# In[ ]:




