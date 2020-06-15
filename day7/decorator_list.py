def new_list(data):

    def even_index():
        new_data = []
        for i in data:
            if i % 2 == 0:
                continue
            else:
                new_data.append(i)
        return new_data

    return even_index()

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(new_list(data))