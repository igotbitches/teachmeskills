import random

def generate_two_matrix():
    data = [] # первая матрица
    data2 = [] # вторая матрица

    for i in range(3):
        pstr = []
        for j in range(3):
            number = random.randrange(1, 10)
            pstr.append(number)
        data.append(pstr)

    for i in range(3):
        pstr2 = []
        for j in range(3):
            number = random.randrange(3)
            pstr2.append(number)
        data2.append(pstr2)

    data3 = [] # сумма матриц
    for i in range(len(data)):
        cx = []
        for j in range(len(data[i])):
            cx.append(data[i][j] + data2[i][j])
        data3.append(cx)

    print(data)
    print(data2)
    print(data3)

print(generate_two_matrix())



