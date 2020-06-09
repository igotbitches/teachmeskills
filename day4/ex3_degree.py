x = int(input('Задайте x: '))

def degree(x, degree):
    """
    Функция возведения в степень
    :param x: число или выражение
    :param degree: степень
    :type degree: int
    :return:
    """
    result = 1
    for i in range(degree):
        result *= x
    return result

y = (degree(x, 6) * degree((x - 5), 3)) / degree((2 * x + 1), 5)
print(y)







