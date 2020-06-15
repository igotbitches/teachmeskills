dict = lambda **key_value: {key*2: value for key, value in key_value.items()}
print(dict(abc = 5, de = 1, ga = 3, same = 4))