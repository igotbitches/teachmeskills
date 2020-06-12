string = 'test1@vitebsk-second.moi.gov.com'
string_list = string.split('@')
ignore = '-_.'
for i in string_list[0]:
    if i.isalpha() or i.isdigit() or i in '-_.':
        print(i)
    else:
        print ('Error')
        break

for j in range(0, len(string_list[1])):
    if j in ignore and j + 1 not in ignore:
        print('Ok')