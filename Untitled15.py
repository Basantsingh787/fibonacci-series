#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###Write a Python class to implement pow(x, n)
#Explanation:
#Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)
#You must implement it using Class
#Sample Input:x: 10
#n: 2
#Sample Output:100


# In[1]:


class pow:
    def __init__(self,x,n):
        self.x=x
        self.n=n
    def power(self):
        self.x=x**n
        print("result is = ",self.x)
x=int(input("Enter the number = "))
n=int(input("Enter the power = "))
c=pow(x,n)
c.power()


# In[ ]:




