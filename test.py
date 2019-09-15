#!/usr/bin/python
def f(x,n):
    f=open('hello.txt')
    l=f.readlines()
    #print l
    f.close()
    d={}
    for i in l:
        j=i.rstrip().split('\t')
        #print j
        u=int(float(j[0])*1000)
        d[u]=map(float,j)
    #print d.keys()
    for m in d.keys():
        if (x-m)*(x-m-5)<0:
            return d[m][n]+(d[m+5][n]-d[m][n])/5*(x-m)
    return d[x][n]
#print f(286.1,8)
#x,n=input('plz input x,n:\n')
#print 'energy:','f(',x,',',n,')=',f(x,n)
def g(order,v):
    f=open('HTBH-EN')
    i=f.readlines()
    #print i
    f.close()
    l=[]
    for j in i:
        r=j.rstrip().split('\t')
        l.append(r)
    #print l
    for m in range(1,20):
        for n in range(2):
            l[m][n]=float(l[m][n])/627.5095
    return l[order][v]
#print g(1,1)
#print f(240,22)-f(285,3)-f(340,10)-g(1,1)
if __name__=='__main__':
    print f(321.4,1)
