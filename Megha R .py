#!/usr/bin/env python
# coding: utf-8

# In[6]:


a=open(r'sample input.txt')
m,n,o,p,j,k=[],[],[],[],[],[]
for x in a:
    x=x.split()
    o.append(x)
    m.append(x[1])
for x in m:
    n.append(int(x))
    j.append(int(x))
n.sort()
b=int(input('Number of employees : '))
print()
s=(len(n)//2)-(b//2)
e=(len(n)//2)+(b//2)
for r in range(len(n)):
    if b%2==0:
        if r>=s and r<e:
            p.append(n[r])
    else:
        if r>=s and r<=e:
            p.append(n[r])
for l in p:
    k.append(j.index(l))
for z in k:
    print(''.join(o[z]))
print('\nAnd the difference between the chosen goodie with highest price and lowest price is',(p[-1]-p[0]))


# In[ ]:




