# def result(a, b, c, d):
#     """
#     operation with
#     :param a: first number
#     :type a: int
#     :param b: second number
#     :type b: int
#     :param c: operation
#     :type c: str
#     :return:
#     :rtype: int
#     """
#     if d is False:
#         a, b = b, a
#     if c == '+':
#         return a + b
#     elif c == '-':
#         return a - b
#     elif c == '*':
#         return a * b
#     else:
#          if b != 0:
#              return a / b
#
# print(result(4,20,'-', False))

###########################


a = [
    [1, 2, 8],
    [8, 12, 6],
    [8, 0, 2]
]
#поиск наибольшего числа во втором столбце матрицы
# max_element = 0
# for i in a:
#    for j in range(len(i)):
#        if j == 1 and max_element < i[j]:
#            max_element = i[j]
# print(max_element)

#########################################
# поиск наибольшего числа в столбце (position - 1, 2, 3) - разобраться

# def max_element_in_matrix(matrix, position):
#     position -= 1
#     if len(matrix[0]) >= position:
#         max_element = 0
#         for i in matrix:
#             for j in range(len(i)):
#                 if j == position and max_element < i[j]:
#                     max_element = i[j]
#         return max_element
#     return 'Error'
#     print(max_element)
# print(max_element_in_matrix(a,1))
#########################################

#замена заданного числа в матрице на ноль и вывод в виде матрицы

# def change_element_in_matrix(matrix, element):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == element:
#                 matrix[i][j] = 0
#     return matrix

###### cделал тоже самое, что и выше, но попроще для понимания

# def change_element_in_matrix(matrix, element):
#     for i in matrix:
#         for j in range(len(i)):
#             if i[j] == element:
#                 i[j] = 0
#     return matrix
######
# print(change_element_in_matrix(a,8))
# new_matrix = change_element_in_matrix(a,8)
# print(new_matrix)
# for i in new_matrix:
#     for j in i:
#         print(j, end="\t")
#     print('\n')

#########################################

#заменить основную (на 1) и побочную (на 0) диагональ, а в пересечении оставить 1

# def change_matrix(matrix):
#     a = 0
#     b = len(matrix[0]) - 1
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if j == a:
#                 matrix[i][j] = 1
#         if a != b:
#             matrix[i][b] = 0
#         a += 1
#         b -= 1
#     return(matrix)
#
# print(change_matrix(a))

#########################################

# def change_zero(matrix, average, max_element):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] < average:
#                 matrix[i][j] = 0
#     return matrix
#
#
# def change_one(matrix, average, max_element):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] > average and matrix[i][j] != max_element:
#                 matrix[i][j] = 1
#     return matrix
#
# def max_average(matrix):
#     average = 0
#     max_element = 0
#     for i in matrix:
#         for j in i:
#             average += j
#             if max_element < j:
#                 max_element = j
#     average = int(average / 9)
#     matrix = change_zero(matrix, average, max_element)
#     matrix = change_one(matrix, average, max_element)
#     return matrix
#
# print(max_average(a))

#############################

def change_after_diagonal(matrix_a, matrix_b):
    pass
def change_before_diagonal(matrix_a, matrix_b):
    index = 0
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[i])):
            if i > index and j <= index + 1:
                matrix_a[i][j], matrix_b[i][j] = matrix_b[i][j], matrix_a[i][j]
                if i <= index+1 and j >= index + 1:
                    matrix_a[i][j], matrix_b[i][j] = matrix_b[i][j], matrix_a[i][j]

    return matrix_b, matrix_a

a2 = [
    [1, 7, 7],
    [5, 12, 7],
    [5, 5, 2]
]

b = [
    [9, 2, 2],
    [1, 12, 2],
    [1, 1, 4]
]

print(change_before_diagonal(b,a2))