#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
num_attribute=6
a=[]
with open('/Users/Chachu/Documents/Python Scripts/enjoysport.csv', 'r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        a.append(row)
        print(row)
print("\n The total number of training instances are : ",len(a))
num_attribute = len(a[0])-1
print("\n The initial hypothesis is : ")
hypothesis = ['0']*num_attribute
print(hypothesis)
for j in range(0,num_attribute):
    hypothesis[j]=a[0][j]

print("\n Find-S: Finding maximally specific Hypothesis\n")

for i in range(0,len(a)):
    if a[i][num_attribute]=='Yes':
        for j in range(0,num_attribute):
            if a[i][j]!=hypothesis[j]:
                 hypothesis[j]='?'
            else:
                hypothesis[j]=a[i][j]
    print("\n For training Example No:{0} the hypothesis is".format(i),hypothesis)
print("\n The Maximally specific hypothesis for the training instance is ")
print(hypothesis)


# In[ ]:





# In[ ]:





# In[ ]:




