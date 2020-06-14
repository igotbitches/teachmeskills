from random import randint
from functools import reduce

plist = []
for x in range(5):
    x = randint(1,51)
    plist.append(x)
print(plist)

max_value = reduce(lambda x, y: x if x > y else y, plist)
print(max_value)