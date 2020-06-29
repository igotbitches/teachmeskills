# Описать класс «домашняя библиотека».
# Предусмотреть возможность работы с произвольным числом книг, поиска книги по какому-либо признаку
# (например, по автору или по году издания), добавления книг в библиотеку,
# удаления книг из нее, сортировки книг по разным полям.

import csv

class Library:

    def __init__(self, author=None, year=None, book_name=None):
        self._book_name = book_name
        self._year = year
        self._author = author
        self._choise = []
        self._write = []


    def search(self):

        with open('library.csv', "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for i in reader:
                if str(self._author) in str(i[0]) or i[1] == self._book_name or i[2] == self._year:
                    self._choise.append(i)


    def add_in_library(self, author, book_name, year):
        self.author = author
        self.book_name = book_name
        self.year = year
        self._write = [self.author, self.book_name, self.year]

        with open('library.csv', "a") as f:
            writer = csv.writer(f)
            writer.writerow(self._write)


    def del_book(self):

        self.data_write = [['author','book name','year']]

        with open('library.csv', "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for i in reader:
                if str(self._author) in str(i[0]) or self._book_name == i[1] or self._year == i[2]:
                    continue
                else:
                    self.data_write.append(i)

        with open('library.csv', 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.data_write)


    def sort(self):
        pass



b = Library('')
b.search()
print(b._choise)

# b.add_in_library("Emile Durkheim","Suicide: A Study in Sociology","1897")

# b = Library('Franz Kafka')
# b.del_book() #работает через Library


