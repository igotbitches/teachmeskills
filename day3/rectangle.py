a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = float(c + b - a)

if a <= 1000 and b <= 1000 and c <= 1000:
    print("%.6f" % d)
else:
    print('Введены неверные данные. Введите целое положительно число, не превосходящее 1000')



