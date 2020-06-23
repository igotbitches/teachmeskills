import csv
from _datetime import datetime

with open('date_file.csv', 'r', encoding='utf-8') as data:
    reader = csv.reader(data)
    header = next(reader)
    date = []
    for i in list(reader):
        date.append(datetime.strptime(f"{i[0]}-{i[1]}-{i[2]}", "%d-%m-%Y"))
    print(min(date).date())

#вариант через lambda
# date = min(
#     list(map(lambda x: datetime.strptime(f"{x[0]}-{x[1]}-{x[2]}", "%d-%m-%Y"), list(reader)))
# ).date()
# print(date)

# долгий и не совсем понятный для других вариант
# def min_date(data):
#
#     def min_year(data):
#         y_list = []
#         for i in range(len(data)):
#             y_list.append(data[i][2])
#         return min(y_list)
#
#     def min_month(data):
#         m_list = []
#         for i in range(len(data)):
#             m_list.append(data[i][1])
#         return min(m_list)
#
#     def min_day(data):
#         d_list = []
#         for i in range(len(data)):
#             d_list.append(data[i][0])
#         return min(d_list)
#
#     second_list = []
#     third_list = []
#
#     for i in range(len(data)):
#         if int(data[i][2]) == int(min_year(data)):
#             second_list.append(data[i])
#
#     for i in range(len(second_list)):
#         if int(second_list[i][1]) == int(min_month(second_list)):
#             third_list.append(second_list[i])
#
#     for i in range(len(third_list)):
#         if int(third_list[i][0]) == int(min_day(third_list)):
#             return '.'.join(third_list[i])
#
# print(min_date(our_list))
