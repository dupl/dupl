#!/usr/bin/python
f=open('00103.com','r')
l=f.readlines()
n=7
for i in l[7:-1]:
    i=list(i)
    i[0]=i[-3]+i[-2]+' '
    i[-2]=''
    i[-3]=''
    i=''.join(i)
    l[n]=i
    n=n+1
f.close()

f=open('00103.com','w')
f.writelines(l)
f.close()
