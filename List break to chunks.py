#!/usr/bin/env python
# coding: utf-8

# In[8]:


import ast
input_str = input()
input_list = ast.literal_eval(input_str)
lis=input_list[0]
k=input_list[1] #chunks

length=len(lis)
mod=length%k 
pdiv=length//k
x=0 #number of lists after creating chunks
if mod==0:
    x=pdiv
else:
    x=pdiv+1
row=[]
list1=[list(row) for i in range(x)]

while len(lis)>=k:
    for i in range(pdiv):
        for j in range(k):
            list1[i].append(lis[0])
            lis.pop(0)

while lis:
    for i in range(mod):
        list1[-1].append(lis[0])
        lis.pop(0)


for i in list1:
    print(i)


#method2
import ast
input_str = input()
input_list = ast.literal_eval(input_str)
lis=input_list[0]
k=input_list[1] #chunks
for i in range(0,len(lis),k): #preparing a step to give starting values of i for each chunk. eg. for k=5, it will return i=0 & 5
    print(lis[i:i+k])




