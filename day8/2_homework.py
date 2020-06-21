import csv
import datetime


with open('minsk_weather.csv', 'r', encoding='utf-8') as weather_file:
    reader = csv.DictReader(weather_file)
    now_time = datetime.datetime.today().date()
    end_time = (datetime.date.today() - datetime.timedelta(days=7))
    gradus = 0
    air = 0

    for line in reader:
        it = datetime.datetime.strptime(line['Дата'], "%d.%m.%Y").date()
        if it <= now_time and now_time >= end_time:
            gradus += int(line['Градусы'])
            air += int(line['Скорость ветра(м/с)'])

    average_g = round((gradus / 7), 2)
    average_v = round((air / 7), 2)
    print(f'Средняя температура: {average_g}')
    print(f'Средняя скорость ветра (м/с): {average_v}')

