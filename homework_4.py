import random


# 1. Написать функцию, которая возвращает среднее арифметическое двух переданных ей аргументов (параметров).
def function_1(number_1, number_2):
    """
    Функция, возвращающая среднее арифметическое двух аргументов
    :param number_1: первый аргумент
    :param number_2: второй аргумент
    :return: среднее арифметическое аргументов
    """
    return (number_1 + number_2) / 2


print(function_1(45, 78))


# 2. Описать функцию вычисления f(x) по формуле:
# f(x)= x^2 при -2<=x<2;
# x^2+4x+5 при x>=2;
# 4 при x<-2.
# Используя эту функцию для n заданных чисел, вычислить f(x).
# Среди вычисленных значений найти наибольшее.
def function_2(number):
    """Функция вычисления f(x) в зависимости от значения x"""
    if -2 <= number < 2:
        return number ** 2
    elif number >= 2:
        return number ** 2 + 4 * number + 5
    elif number < -2:
        return 4


function_2_list = []
function_2_result = []
for _ in range(11):
    function_2_list.append(random.randint(1, 10))
print(f'{function_2_list} - набор значений')

for number in function_2_list:
    function_2_result.append(function_2(number))
print(f'{function_2_result} - результат выполнения функции')

print(f'{max(function_2_result)} - наибольшее значение')


# 3. Возведение выражений в степень с натуральным показателем оформить в виде функции, как нахождение
# произведения одинаковых множителей. Не использовать стандартной математической функции
# вычисления степени.
def function_3(expression, degree):
    """
    Функция возведения в степень
    :param expression: выражение
    :param degree: степень
    :return:
    """
    result = 1
    for _ in range(degree):
        result *= expression
    return result


def function_3_1(x):
    """
    Программа вычисления  выражения: y = (x6*(x-5)3) / (2*x+1)5
    :param x: аргумент функции
    :return:
    """
    result = (function_3(x, 6) * function_3((x - 5), 3)) / function_3((2 * x + 1), 5)
    return result


# 4. С помощью функции заполнить матрицы случайными числами. Написать
# функцию, вычисляющую сумму двух матриц. Вывести на экран две
# исходные матрицы и их сумму
def function_4(matrix_1, matrix_2):
    """
    Сумма матриц
    :param matrix_1: первая матрица
    :type matrix_1: list
    :param matrix_2: вторая матрица
    :type matrix_2: list
    :return: сумма матриц
    :rtype: list
    """
    sum_matrix = []
    for i in range(len(matrix_1)):
        sum = []
        for j in range(len(matrix_1[i])):
            sum.append(matrix_1[i][j] + matrix_2[i][j])
        sum_matrix.append(sum)
    return sum_matrix


matr_1, matr_2 = [], []
for i in range(3):
    list = []
    for j in range(3):
        list.append(random.randint(1, 10))
    matr_1.append(list)

for i in range(3):
    list = []
    for j in range(3):
        list.append(random.randint(1, 10))
    matr_2.append(list)

print('Исходные матрицы')
for l, m in zip(matr_1, matr_2):
    print(l, m)

print('Сумма матриц')
new_matr = function_4(matr_1, matr_2)
for l in new_matr:
    print(l)


# 5. Найти наименьшее общее кратное (НОК) пар целых положительных чисел через наибольший общий делитель (НОД) по
# формуле lcm = ab / gcd(a; b), где lcm - НОК, gcd - НОД, a и b - числа.
def function_5(a, b):
    """
    Наименьшее общее кратное пар чисел
    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: наименьшее общее кратное
    :rtype: int
    """
    lcm = int(a * b / function_8(a, b))
    return lcm


# 6. Написать функцию. Пользователь вводит число, представленное в десятичной системе счисления. Программа должна
# преобразовывать его в число, выраженное в шестнадцатеричной системе счисления. Результат вывести на экран.
def function_6(number_10):
    """
    Перевод десятичного числа в шестнадцатеричное
    :param number_10: число в десятичной системе счисления
    :return: число в шестнадцатеричной системе счисления
    """
    converter = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    number_16 = []
    while number_10:
        number_16.append(converter[number_10 % 16])
        number_10 //= 16

    number_16 = f'0x{"".join(number_16[::-1])}'

    return number_16


# 7. Написать функцию, которая переводит число из десятичной системы счисления в двоичную или восьмеричную
def function_7(number_10, base):
    """
    Перевод десятичного числа в двоичную или восьмеричную систему счисления
    :param number_10: число в десятичной системе счисления
    :param base: основание системы счисления
    :return:
    """
    number_2_8 = []
    if base == 2:
        while number_10:
            number_2_8.append(str(number_10 % 2))
            number_10 //= 2
    elif base == 8:
        while number_10:
            number_2_8.append(str(number_10 % 8))
            number_10 //= 8
    else:
        print('Неверное основание системы счисления')
    return ''.join(number_2_8[::-1])


# 8. Написать функцию, вычисляющую наибольший общий делитель
def function_8(a, b):
    """
    Функция, вычисляющая наибольший общий делитель
    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: наибольший общий делитель
    :rtype: int
    """
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    gsd = a + b

    return gsd


# 9. Переставить по алфавиту буквы слов в строке
def function_9(text):
    """
    СОртировка букв в словах в тексте по алфавиту
    :param text: исхожный текст
    :type text: str
    :return: текст с отсортированными словами
    :rtype: str
    """
    words = []
    for word in text.split():
        words.append(''.join(sorted(word)))
    return ' '.join(words)


# 10. Написать функцию, которая циклически сдвигает одномерный массив вправо или влево на указанное число позиций.
# Сдвиг также должен быть кольцевым, то есть те элементы, которые уходят вправо или влево за пределы массива, должны
# помещаться с другого его конца.
def function_10(list, step):
    """
    Функция циклического сдвига
    :param list: исходный массив
    :type list:
    :param step: шаг сдвига
    :type step: int
    :return: массив со сдвигом
    :rtype: list
    """
    new_list = []
    for index, item in enumerate(list):
        if index + step >= len(list):
            new_list.insert(len(list) - (index + step), item)
        else:
            new_list.insert(index + step, item)
    return new_list


print(function_10([1, 2, 3, 4, 5, 6], 2))



