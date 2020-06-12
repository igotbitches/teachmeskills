#Дополнительыне функции работы со строками

string = 'Hello,_my_name_is_Alex'
string_list = string.split('_')
result = ' '.join(string_list)
print(result)

string = 'ping pong'
result_string = string.replace('p', 'k')
print(result_string)
--------------------------------
#Задание 3.03
data = 'computer network'
plist = data.split()
new_data = ' '.join(plist[::-1])
print(f'!{new_data}!')
#то же самое, только в одну строку
print(f'! {" ".join(data.split()[::-1])} !')
--------------------------------
#пример функции
def result(a,b):
    return a+b
a = 2
b = 3
print(result(a,b))
--------------------------------
#Задание 3.04
data = 'Something interesting'
if len(data)%3 == 0:
    print(f'{data}!')
else:
    print('Предложение не кратно 3')
--------------------------------
#Задание 3.05
data = input('Введите предложение: ').split()
if "code" in data:
    print('YES')
else:
    print('NO')
--------------------------------
#Задание 3.06
data = int(input('Введите свой возраст: '))
if data < 0:
    print('Wrong input')
elif data < 18:
    print('CocaCola')
else:
    print('Beer')
--------------------------------
import math
#ax^2+bx+c=0
a = 1
b = 70
c = 600
d = b**2 - 4 * a * c
x1 = -b - math.sqrt(d) / (2 * a)
x2 = -b + math.sqrt(d) / (2 * a)
if x1 != x2:
    print(f"x1: {x1}, x2: {x2}")
elif x1 == x2:
    print(f"x1,2 = {x1}")
else:
    print('NO')
--------------------------------
#задание 3.11
#data = input('Введите почтовый адрес: ').split('@')
#if "gmail.com" in data:
#    print('@'.join(data))
#elif '@' not in data:
#    print("Enter @")
#else:
#    print('DOMAIN NAME is not supported')


____________________________________
#читает строку в обратную сторону
data = input('Enter: ')

def newgame():
    n = data.split()
    for x in range(len(n)):
        if x <= len(n):
            new_word = []
            n[x] = n[x][::-1]
            new_word = new_word + n
    return ' '.join(new_word)

print(newgame())