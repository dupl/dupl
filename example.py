#!/usr/bin/python
import itertools
l=range(1,8)
it=itertools.permutations(l,7)
#print list(it)
for i in it:
    if (i[0]*100+8*10+i[1])*i[2] == i[3]*1000+i[4]*100+i[5]*10+i[6]:
        print i[0]*100+8*10+i[1], i[2], i[3]*1000+i[4]*100+i[5]*10+i[6]
