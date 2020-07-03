#!/home/dupl/anaconda3/bin/python
def gen(n):
    for i in range(n):
        yield i**2

for i in gen(5):
    print(i)

print("hello world")
print("世界,你好")
