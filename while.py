i = 0
result = 1000
while True:
    if i >result:
        break
    print(i)
    i += 1


x = int(input('Введите число: '))
fact = 1
while x > 1:
    fact *= x
    x -= 1

print(fact)