#!/usr/bin/python2
#coding:utf-8
def gen(n):
    for i in range(n):
        yield i**2

for i in gen(5):
    print i

print "hello world"
print u"世界,你好"