from random import randint
from functools import reduce

plist = []
for x in range(5):
    x = randint(1,51)
    plist.append(x)
print(plist)

# max_value = reduce(lambda x, y: x if x > y else y, plist)
# print(max_value)

# второй вариант, который проще для памяти (key=lambda x - перебирается каждый элемент в списке)
result = max(plist, key=lambda x: int(x))
print(result)