def average(a, b):
    """
    Среднее арифметическое двух аргументов
    :param a: первый агрумент
    :type a: float
    :param b: второй аргумент
    :type b: float
    :return: сумма двух аргументов разделенная на 2
    :rtype: float
    """
    return (a + b) / 2

while 1:
    x = float(input('Введите a: '))
    y = float(input('Введите b: '))
    print("Среднее арифметическое: ", "%.2f" % average(x, y))
