#!/usr/bin/env python
# coding: utf-8

# In[2]:


list1 =[]
n=int(input("enter number "))
for i in range(n):
    t=tuple(map(int,input().split()))
    list1.append(t)
print("List of Tuple before sorting : " + str(list1))



for i in range(0, len(list1)):  
    for j in range(0, len(list1) - i - 1):  
        if(list1[j][-1] > list1[j + 1][-1]): 
            swap = list1[j]
            list1[j] =list1[j + 1]
            list1[j + 1] = swap


print("List of Tuple after sorting : " + str(list1))


# In[ ]:




