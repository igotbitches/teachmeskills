plist = ['Masha', 'Dasha', 'Sasha', 'Valera']
print(plist)
new_plist = list(map(lambda name: f'Hello, {name}', plist))
print(new_plist)