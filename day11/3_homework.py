# Написать калькулятор. Программа должна содержать 4 функции принимающие два аргумента
# и возвращающие результаты сложения, вычитания, умножения и деления.
# Реализовать пользовательский интерфейс с бесконечным циклом.
# Добавить валидацию входных данных.
# Программа должна состоять из четырех файлов(main.py, func.py, ui_func.py exceptions.py).


"""'это будет func.py"""


def user_sum(x, y):
    user_sum = x + y
    return user_sum


def user_sub(x, y):
    user_sub = x - y
    return user_sub


def user_mult(x, y):
    user_mult = x * y
    return user_mult


def user_div(x, y):
    user_div = x / y
    return user_div


"""Это будет exceptions.py"""


def zero_err():
        try:
            if y == 0 in user_div(x, y):
                raise ZeroDivisionError
        except ZeroDivisionError as err:
            print(f"На ноль делить нельзя! - {err}")

def value_err():

    try:
        if type(x) == str:
            raise ValueError
        if type(y) == str:
            raise ValueError
    except ValueError as err:
        print(f'Введите число! - {err}')



"""Это будет ui_func.py"""

while True:
    sign = input("Введите знак (+,-,*,/) \nили 'stop', чтобы выйти из программы: ")
    if sign == 'stop':
        break
    if sign in ('+', '-', '*', '/'):

        x = float(input('Введите x: '))
        y = float(input('Введите y: '))
        if sign == '+':
            print(user_sum(x, y))
        if sign == '-':
            print(user_sub(x, y))
        if sign == '*':
            print(user_mult(x, y))
        if sign == '/':
            if y == 0:
                zero_err()
            else:
                print(user_div(x, y))






# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")
