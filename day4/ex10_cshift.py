data = list(range(7))

def shift(plist, steps):
    """
    Циклический сдвиг
    :param plist: какой-либо список
    :type plist: list
    :param steps: количество шагов сдвига, отрицательные числа сдвигают список слева направо,
    положительные - справа налево
    :type steps: int
    :return: измененный список
    :rtype: list
    """
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            plist.append(plist.pop(0))
    else:
        for i in range(steps):
            plist.insert(0, plist.pop())
    return plist

print(shift(data, -2))