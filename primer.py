#Дополнительыне функции работы со строками

string = 'Hello,_my_name_is_Alex'
string_list = string.split('_')
result = ' '.join(string_list)
print(result)

string = 'ping pong'
result_string = string.replace('p', 'k')
print(result_string)
--------------------------------

#Задание 3.03
data = 'computer network'
plist = data.split()
new_data = ' '.join(plist[::-1])
print(f'!{new_data}!')
--------------------------------

