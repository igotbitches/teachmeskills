#first option using "for"

x = int(input('Введите целое число: '))
factorial = 1
for i in range(x):
    factorial *= (i+1)
print(factorial)


#second option using "while"

x = int(input('Введите целое число: '))
fact = 1
while x > 1:
    fact = fact * x
    x -= 1
print(fact)

