#!/usr/bin/python
l=range(1,8)
for i in l:
    for j in l:
        if i == j:continue
        for k in l:
            if i == k or j == k:continue
            for m in l:
                if i == m or  j == m or  k == m:continue
                for n in l:
                    if i == n or  j == n or  k == n or  m == n:continue
                    for p in l:
                        if i == p or  j == p or  k == p or  m == p or  n == p:continue
                        for q in l:
                            if i == q or  j == q or  k == q or  m == q or  n == q or p == q:continue
                            if (i*100+8*10+j)*k == m*1000+n*100+p*10+q:
                                print i*100+8*10+j,k,m*1000+n*100+p*10+q
