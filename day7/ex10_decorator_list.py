def decorate(func):

    def wrapper(datas):
        new_data = {}
        for i, j in enumerate(datas+1):
            new_data[j] = i
        func(datas)
        return wrapper

@decorate
def result(datas):
    print(datas)

result(["a", "b", "c"])

########################
# def new_list(func):
#
#     def even_index(datas):
#         new_data = []
#         for i in datas:
#             if i % 2 == 0:
#                 continue
#             else:
#                 new_data.append(i)
#         func(new_data)
#     return even_index
#
# @new_list
# def result(datas):
#     print(datas)
#
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# result(data)