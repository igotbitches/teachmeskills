# def decorate(func):
#     def results(*args):
#         args = args[::-1]
#         func(*args)
#     return results
#
# @decorate
# def result(*args):
#     print(args)
#
# result(1,2,3,4)

##########################################

# меняет местами ключ, значение

# def decorate(func):
#
#     def results(**kwargs):
#         new_list = {}
#         for key, value in kwargs.items():
#             new_list[str(value)] = key
#         print(new_list)
#         func(**new_list)
#     return results
#
# @decorate
# def result(**kwargs):
#     print(kwargs)
#
#
# result(a=1, b=2, c=3, d=4)

##########################################


# def decorate(func):
#
#     def results(*args, **kwargs):
#         new_list = {}
#         second_list = args
#         for key, value in kwargs.items():
#             if value not in args:
#                 new_list[key] = value
#         func(*second_list, **new_list)
#     return results
#
# @decorate
# def result(*args, **kwargs):
#     print(args, kwargs)
#
# result(1, 2, 3, a=1, b=2, c=3, d=4)

##########################################

def decorate(func):

    def results(details, **kwargs):
        new_list = {}
        for key, value in kwargs.items():
            new_list[key] = value * details
        func(details, **new_list)
    return results

def second_decorator(func):
    def results(details, **kwargs):
        print(kwargs)
        data = {}
        for i, j in kwargs.items():
            data[i] = 0 if j % 3 == 0 else j
        func(details, **data)

    return results


@decorate
@second_decorator
def result(details, **kwargs):
    print(details)
    print(kwargs)

result(details=15, a=1, b=2, c=3, d=4)