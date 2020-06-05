def nod(a, b):
    """
    Находим наибольший общий делитель (НОД) двух чисел по методу Евклида.
    :param a: первое число
    :type a: int
    :param b: второе число
    :type b: int
    :return: сумма a и b, т.к. одно из чисел будет равно нулю
    :rtype: int
    """
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

while 1:
    x = int(input('Введите первое число: '))
    if x == 0:
        break
    y = int(input('Введите второе число: '))
    print('НОД:', nod(x, y))

