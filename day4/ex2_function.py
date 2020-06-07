from random import randint

def math_function(x):
    """
    Функция вычисления f(x) в зависимости от значения x
    :param x: любое число
    :type x: int
    :return: значение n
    :rtype: int
    """
    if x >= -2 and x < 2:
        n = x**2
    elif x >= 2:
        n = x**2 + 4 * x + 5
    elif x < -2:
        n = 4
    return n

# пять рандомных чисел - наш рандомный (x)
plist = []
for i in range(5):
    x = randint(-10, 20)
    plist.append(x)

# полученные пять рандомных чисел вычисляем по функции f(x)
new_list = []
for i in plist:
    new_list.append(math_function(i))

print(new_list)
print(max(new_list))





