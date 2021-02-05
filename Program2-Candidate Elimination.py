#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
a=[]
with open("/Users/Chachu/Documents/Python Scripts/enjoysport.csv","r") as csvfile:
    fdata=csv.reader(csvfile)
    for row in fdata:
        a.append(row)
        print(row)
num_att=len(a[0])-1
S=['0']*num_att
G=['?']*num_att
print(S)
print(G)
temp=[]
for i in range(0,num_att):
    S[i]=a[0][i]
print("................................................")
for i in range(0,len(a)):
    if a[i][num_att]=="Yes":
        for j in range(0,num_att):
            if S[j]!=a[i][j]:
                   S[j]='?'
        for j in range(0,num_att):
              for k in range(0,len(temp)):
                    if temp[k][j]!=S[j] and temp[k][j]!='?':
                        del temp[k]
    if a[i][num_att]=='No':
        for j in range(0,num_att):
            if a[i][j]!=S[j] and S[j]!='?':
                G[j]=S[j]
                temp.append(G)
                G=['?']*num_att
    print(S)
    if len(temp)==0:
        print(G)
    else: 
        print(temp)
    print("......................................................................")


# In[ ]:





# In[ ]:




