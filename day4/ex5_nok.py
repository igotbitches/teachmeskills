def lcm(a, b):
    """
    Вычисление наименьшего общего кратного (НОК)
    :param a: целочисленное значение a
    :type a: int
    :param b: целочисленное значение b
    :type b: int
    :return: произведение a и b делённое на НОД этих чисел
    :rtype: int
    """
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)

while 1:
    x = int(input('a = '))
    if x == 0:
        break
    y = int(input('b = '))
    print('НОК:', lcm(x, y))
