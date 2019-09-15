#!/usr/bin/python
f=file('f1.m','r')
l=f.readlines()
f.close()
#print l
n=-1
l0=[]
for i in l:
    j='result('+str(n)+')='+i
    l0.append(j)
    n+=1
#print l0
f0=file('h1.m','w')
f0.writelines(l0)
f0.close()
