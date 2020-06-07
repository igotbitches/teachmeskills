data = input('Enter: ')

def newgame():
    n = data.split()
    for x in range(len(n)):
        if x <= len(n):
            new_word = []
            n[x] = ''.join(sorted(n[x]))
            new_word = new_word + n
    return ' '.join(new_word)

print(newgame())