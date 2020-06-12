
def system_2_and_8(number, system):
    """
    Перевод десятичного числа в системы octal и binary.
    :param number: Чисто десятичной системы счисления
    :type number: int
    :param system: Система счисления, в которую нужно перевести число десятичной системы
    :type system: int
    :return: число octal/binary в виде списка
    :rtype: list
    """
    if system == 2:
        number_2 = []
        while number != 0:
            number_2.insert('0', number % 2)
            number //= 2
        return ' '.join(str(x) for x in number_2)
    elif system == 8:
        number_8 = []
        while number != 0:
            number_8.insert(0, number % 8)
            number //= 8
        return ' '.join(str(x) for x in number_8)

number = int(input("Enter number: "))
system = int(input("Enter system: "))
print(system_2_and_8(number, system))