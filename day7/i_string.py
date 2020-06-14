list_str = ['game', 'other', 'fine', 'other', 'something']
plist = [i for i in range(1,6)]
new_list = list(map(lambda x, y: f'{x} - {y}', plist, list_str))
print(new_list)