import csv

with open('homework.csv', encoding='utf-8') as f_file:
    reader = csv.DictReader(f_file)
    first_group = 0
    second_group = 0
    third_group = 0
    fourth_group = 0
    fifth_group = 0
    for row in reader:
        if int(row['Age']) > 0 and int(row['Age']) <= 12:
            first_group += 1
        elif int(row['Age']) >= 13 and int(row['Age']) <= 18:
            second_group += 1
        elif int(row['Age']) and int(row['Age']) <= 25:
            third_group += 1
        elif int(row['Age']) >= 26 and int(row['Age']) <= 40:
            fourth_group += 1
        else:
            fifth_group += 1

data = [['группа', 'количество людей'],
        ['1-12', first_group],
        ['13-18', second_group],
        ['19-25', third_group],
        ['26-40', fourth_group],
        ['40+', first_group]
        ]

with open('homework2.csv', 'w', encoding='utf-8') as new_file:
    writer = csv.writer(new_file)
    for line in data:
        writer.writerow(line)

with open('homework2.csv', encoding='utf-8') as new_file:
    print(new_file.read())

#спросить, почему получаются такие отступы в файле .csv при его создании

