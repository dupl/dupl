#!/usr/bin/python
f=open('HTBH-EN')
i=f.readlines()
#print i
f.close()
l=[]
for j in i:
    v=j.rstrip().split('\t')
    l.append(v)
#print l
for m in range(1,20):
    for n in range(2):
        l[m][n]=float(l[m][n])/627.5095
#print l
print l[3][1]
