#!/home/dupl/anaconda2/bin/python
from __future__ import division
import matplotlib.pyplot as plt
def f(J,x):
    return J**x
J=input('plz input J:')
filename=str(J)+'.txt'
X=[t/10.0 for t in range(4,302,2)]
Y=[]
for x in X:
    Y.append(f(J,x))
s=[str(y)+'\n' for y in Y]
f=open(filename,'w+')
f.writelines(s)
f.close()

plt.plot(X,Y,'-r')
plt.title('J='+str(J))
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim([0.4,30.0])
plt.show()
