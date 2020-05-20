x = int(input('Введите число: '))
fact = 1
while x > 1:
    fact *= x
    x -= 1

print(fact)