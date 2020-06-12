pupils = [
{
        'firstname': 'Masha',
        'Group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
},
{
        'firstname': 'Dasha',
        'Group': 34,
        'physics': 9,
        'informatics': 10,
        'history': 7,
  },
{
        'firstname': 'Alla',
        'Group': 39,
        'physics': 4,
        'informatics': 3,
        'history': 9,
  },
    {
        'firstname': 'Kate',
        'Group': 40,
        'physics': 2,
        'informatics': 1,
        'history': 4,
  }
]

for i in pupils:
    average = round(((i['physics'] + i['informatics'] + i['history']) / 3), 2)
    if average > 4:
        print(f"Имя: {i['firstname']}, Группа: {i['Group']}, Средний балл: {average}")

