data = 'sasha 4zkjh3, masha 23'
list1 = data.replace(',','').split()
age = ""
alpha = ""

for i in data:
    if i.isdigit():
        age += i

sasha_age = int(age[0:2])
masha_age = int(age[2:4])

for i in list1:
    if i.isalpha():
        alpha += i

sasha_name = str(alpha[0:5].title())
masha_name = str(alpha[5:10].title())

print(sasha_age+masha_age)
print(f'{sasha_name}: {sasha_age}, {masha_name}: {masha_age}')