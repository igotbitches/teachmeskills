import random

def calculate(func):
    import time

    def results():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд'.format(end - start))

    return results

def ll(func):
    def wrapper():
        func()
        print('Второй декоратор')

    return wrapper

@ll
@calculate
def result():
    data = [random.randrange(0, 2 ** 100) for x in range(0, 2 ** 20)]
    sorted(data)

print(result())

#################################################
# def time_import_call(x):
#     import time
#
#     def time_count():
#         start_count = time.time()
#         x()
#         end_count = time.time()
#         print('Время: {} '.format(end_count - start_count))
#     return time_count()
#
#
# @time_import_call
# def new_function():
#     import requests
#     webpage = requests.get('http://anolink.ru')
#
# print(new_function)


