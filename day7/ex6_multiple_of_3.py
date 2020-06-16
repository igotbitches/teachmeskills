from functools import reduce
data = [1, 3, 6, 7, 10, 9, 12]

# value_list = list(filter(lambda x: x % 3 == 0, data))
# value = reduce(lambda x, y: x * y, value_list)
# print(value)

# второй вариант в одну строку
result = reduce(lambda x, y: x * y, filter(lambda x: x % 3 == 0, data))
print(result)