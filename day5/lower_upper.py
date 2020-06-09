
def lower_upper(string):
    """
    Функция, изменяющая регистр букв в слове
    :param string: слово или фраза с разным регистром букв
    :type string: str
    :return: возвращает слово или фразу в верхнем или в нижнем регистре
    :rtype: str
    """
    lower = ''
    upper = ''
    for i in range(len(string)):
        if string[i].isupper():
            upper += string[i]
        else:
            lower += string[i]
    if len(lower) > len(upper) or len(lower) == len(upper):
        return string.lower()
    if len(upper) > len(lower):
        return string.upper()

string = input('Enter: ')
print(lower_upper(string))