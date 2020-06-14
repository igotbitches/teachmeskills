names = ['Kate', 'Lena', 'Karina', 'Alex', 'Dima', 'Nick']

new_list = list(filter(lambda x: 'k' in x.lower(), names))
print(new_list)

