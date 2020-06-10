def system_16(number):
    """
    Функция, которая преобразует число десятичной системы счисления в число шестнадцатеричной системы
    :param number: число в десятичной системе счисления
    :type number: int
    :return: строковое значение списка number_16
    :rtype: str
    """
    dict_numbers_16 = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    number_16 = []
    while number != 0:
        number_16.insert(0, dict_numbers_16.get(number % 16))
        number //= 16
    return ''.join(number_16)


while 1:
    number = int(input('Введите число: '))
    if number == 0:
        break
    print(system_16(number))