data = str(input('Количество рублей: '))
dlist = data.split('.')

total = int(float(data) * 100)
rub = total // 100
cent = total % 100
rub_word = ''
cent_word = ''

if rub == 1 or rub % 10 == 1:
    rub_word = 'рубль'
    if rub%10 == 2 or rub%10 == 3 or rub%10 == 4:
        rub_word = 'рубля'
        if rub == 12 or rub == 13 or rub == 14:
            rub_word = 'рублей'
else:
    rub_word = 'рублей'

if cent == 1 or cent % 10 == 1:
    cent_word = 'копейка'
    if cent%10 == 2 or cent%10 == 3 or cent%10 == 4:
        cent_word = 'копейки'
        if cent == 12 or cent == 13 or cent == 14:
            cent_word = 'копейки'
else:
    cent_word = 'копеек'

print(f'{rub} {rub_word}, {cent} {cent_word}')







# a = int(dlist[0])
# b = int(dlist[1])
# total = (100 * a) + b #количество копеек
# print(total)


# print(dlist[0])
#
# print(f'{dlist[0]} {rub_word}, {dlist[1]} {cent_word}')



# a = int(input())#Стоимость пирожка в рублях
# b = int(input())#Стоимость пирожка в копейках
# n = int(input())#Кол-во пирожков
# price = (100 * a) + b #Все смешиваем в копейки, так как 1р=100к
# total = price * n #Стоимость n пирожков в общем(В копейках)
# rub = total // 100 #На рубли
# kop = total % 100 #На копейки
# print(rub , kop) #Стоимость n пирожков в рублях и копейках.


# rub_word = 'рублей'
# cent_word = 'копеек'

# for i in dlist[0]:
#     if i == 1:
#         print(f'{dlist[0]} рубля')
#
# data.is