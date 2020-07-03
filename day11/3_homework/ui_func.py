from func import *

def user_ui_func():
    while True:
        sign = input("Введите знак (+,-,*,/) \nили 'stop', чтобы выйти из программы: ")
        if sign == 'stop':
            break
        if sign in ('+', '-', '*', '/'):
            x = float(input('Введите x: '))
            y = float(input('Введите y: '))
            if sign == '+':
                print(user_sum(x,y))
            if sign == '-':
                print(user_sub(x,y))
            if sign == '*':
                print(user_mult(x,y))
            if sign == '/':
                print(user_div(x, y))


