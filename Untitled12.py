#!/usr/bin/env python
# coding: utf-8

# #Write a Python program to triple all numbers of a given list of integers. Use Python map.
# #sample list: [1, 2, 3, 4, 5, 6, 7]
# #Triple of list numbers:[3, 6, 9, 12, 15, 18, 21]# 

# In[1]:


def  triple(x):
    return 3*x
    
list1=[int(x) for x in input().split()]
print("list before any operation is " , list1)
result=list(map(triple,list1))
print("list after triple of number",result)


# In[ ]:




