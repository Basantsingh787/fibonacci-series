#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###Write a Python program to square the elements of a list using map() function.
#Sample List: [4, 5, 2, 9]
#Square the elements of the list:
#[16, 25, 4, 81]


# In[1]:


def square(x):
    return x**2
list1=[int(x) for x in input().split()]
print("list before any operation is " , list1)
result=map(square,list1)
print("list after sqaure of number",list(result))

