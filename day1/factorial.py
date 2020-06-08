#first option using "for"

x = int(input('Введите целое число: '))
if x == 0:
    print(1)
else:
    factorial = 1
    for i in range(x):
        factorial *= (i+1)
    print(factorial)


#second option using "while"

x = int(input('Введите целое число: '))
if x == 0:
    print(1)
else:
    fact = 1
    while x > 1:
        fact = fact * x
        x -= 1
    print(fact)

