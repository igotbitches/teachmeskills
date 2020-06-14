def time_import_call(x):
    import time

    def time_count():
        start_count = time.time()
        x()
        end_count = time.time()
        print('Время: {} '.format(end_count - start_count))
    return time_count()


@time_import_call
def new_function():
    import requests
    webpage = requests.get('http://anolink.ru')

print(new_function)

