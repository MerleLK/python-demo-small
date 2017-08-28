"""
@description: lambda的基本demo
@author: merle
@contact: merle.liukun@gmail.com
@date: 2017/8/28 
"""

a = lambda num: "Eat.{}".format(num)

for i in map(a, [1, 2, 3]):
    print(i)

l = [1, 2, 4, 5, -9, 0, -99]
for i in map(lambda x: abs(x), l):
    print(i, end=",")
print("")

for k in filter(lambda x: x <= 0, l):
    print(k, end=", ")
print("")

# lambda x,y: "x*y={}".format(x*y)

print(
    '\n'.join(map(lambda x: ' '.join(map(lambda y: "%s x %s = %2s" % (y, x, x * y), range(1, 10)[:x])), range(1, 10))))
