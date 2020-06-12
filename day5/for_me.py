# Задание 5.01
# создаем и заполняем матрицу случаными числами (первый вариант)
import random
# n = 3
# matrix = [[random.randrange(1, 10) for x in range(n)] for y in range(n)]
# print(matrix)


# Задание 5.01 и 5.02
# создаем и заполняем матрицу случаными числами (второй вариант)
# и скаладываем все числа, кратные 3

# def generate_matrix(n):
#     data = []
#     sum_matrix = 0
#     tree = []
#     for i in range(0, n):
#         pstr = []
#         for j in range(0, n):
#             number = random.randrange(1, 100)
#             pstr.append(number)
#             if number % 3 == 0:
#                 tree.append(number)
#                 sum_matrix += number
#         data.append(pstr)
#     print(data)
#     print(tree)
#     print(sum_matrix)
#
# print(generate_matrix(3))


#Задача 5.03
# Дан двумерный массив n × m элементов.
# Определить, сколько раз встречается число 7 среди элементов массива

# n, m = 3, 4
#
# def generate_matrix(n, m):
#     data = []
#     counter = 0
#     tree = []
#     for i in range(0, n):
#         pstr = []
#         for j in range(0, m):
#             number = random.randrange(1, 10)
#             pstr.append(number)
#             if number == 7:
#                 counter += 1
#         data.append(pstr)
#     print(data)
#     print(counter)
#
# print(generate_matrix(n,m))


# for i, elem in enumerate(['a','b','c','d']):
#    print(f'{i} - {elem}')

#Задача 3.04

# def generate_matrix(n, m):
#     data = []
#     average = 0
#     for i in range(0, n):
#         pstr = []
#         for j in range(0, m):
#             number = random.randrange(1, 100)
#             average += number
#             pstr.append(number)
#         data.append(pstr)
#     average = average / (n * m)
#
#     counter = 0
#     for i in range(0, n):
#         for j in range(0, m):
#             if data[i][j] > average and (i + j) % 2:
#                 counter += 1
#     print(counter)


#
# for key, value in pupils.items():
#     print(key, value)


#Зачада 5.07

# n = int(input("ОТ: "))
# m = int(input("ДО: "))
# counter = input('Количество попыток: ')
#
# number = random.randrange(1, 100)
# print(number)
# used = 0
# correct = False

# while True:
#     used += 1
#     user_number = int(input(''))
#
#     if user_number <= n and user_number >= m:
#         print(f'Number is not in range {n}-{m}')
#     if user_number == number:
#         correct = True
#         print('You are winner!')
#         break
#     if used == counter:
#         break
# if correct is False:
#     print('You are loser!')

# for i in range(counter):
#     user_number = int(input())
#     if user_number <= n and user_number >= m:
#         print(f'Number is not in range {n}-{m}')
#         if user_number == number:
#             correct = True
#             print('You are winner!')
#             break
#
# if correct is False:
#     print('You are loser!')

# Задача 1 из телеграма, но у меня не работает
# data = 'привет привет абракадабра двадцать'
# words = {} #слова и сколько повторений
# longs_word = "" #самое длинное слово
# counter_word = data.split()[i]
#
# for i in data.split():
#     if len(longs_word) < len(i):
#         longs_word = i
#     if i in words:
#         words[i] += 1
#     else:
#         words[i] = 1
#
#     if counter_word not in words:
#         counter_word = i
#     else:
#         if words[counter_word] < words[i]:
#             counter_word += i
#
# print(words)
# print(longs_word)
# print(counter_word)

# 2 задание из телеграмма
# seter = [1, 2, 3, 4, 5, 6, 7, 8, 8, 3, 4, 5]
# pset = set(seter)
#
# if len(seter) == pset:
#     print(True)
# else:
#     print(False)

#Задание 4 из телеграма
a = [1, 2, 3, 4, 5, 6, 7, 8, 8, 3, 4, 5]
b = [1, 2, 10, 4, 12, 6, 7, 8, 8, 3, 4, 5]

def cheker(a, b):
    for i in a:
        if i not in b:
            print(i)

cheker(a, b) #всё также, но не работает. Почему?


