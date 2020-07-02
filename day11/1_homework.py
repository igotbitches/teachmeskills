
class MyTime:
    """Работа с магическими методами сравнения, сложения, вычитания, умножеиния.
    Перегрузка конструктора"""

    def __init__(self, hours=None, minutes=None, seconds=None):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        if type(hours) == str and minutes == None and seconds == None:
            new_list = hours.split('-')
            self.hours = int(new_list[0])
            self.minutes = int(new_list[1])
            self.seconds = int(new_list[2])

        if type(hours) == type(self) and minutes == None and seconds == None:
            self.hours = hours.hours
            self.minutes = hours.minutes
            self.seconds = hours.seconds

        if self.hours == None and self.minutes == None and self.seconds == None:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

        if self.seconds > 59:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60

        if self.minutes > 59:
            self.hours += self.minutes // 60
            self.minutes %= 60
    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True
        else:
            return False

    def __ne__(self, other):
        return self.hours != other.hours and self.minutes != other.minutes and self.seconds != other.seconds

    def __lt__(self, other):
        return self.hours < other.hours and self.minutes < other.minutes and self.seconds < other.seconds

    def __gt__(self, other):
        return self.hours > other.hours and self.minutes > other.minutes and self.seconds > other.seconds

    def __le__(self, other):
        return self.hours <= other.hours and self.minutes <= other.minutes and self.seconds <= other.seconds

    def __ge__(self, other):
        return self.hours >= other.hours and self.minutes >= other.minutes and self.seconds >= other.seconds

    def __add__(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds

    def __sub__(self, other):
        self.hours -= other.hours
        self.minutes -= other.minutes
        self.seconds -= other.seconds

    def __mul__(self, other):
        self.hours *= other.hours
        self.minutes *= other.minutes
        self.seconds *= other.seconds

    def __str__(self):

        if self.hours > 24:
            return 'В сутках 24 часа'
        if len(str(self.minutes)) == 1:
            self.minutes = f"0{self.minutes}"
        if len(str(self.seconds)) == 1:
            self.seconds = f"0{self.seconds}"
        if len(str(self.hours)) > 2:
            return 'Введите время в формате: 00:00:00'
        elif len(str(self.hours)) == 1:
            self.hours = f"0{self.hours}"
        return f"Time: {self.hours}:{self.minutes}:{self.seconds}"


"""одна строка"""
# m = MyTime("2-2-2")
# print(m)

"""отсутствие входных параметров"""
# m = MyTime()
# print(m)

"""другой объект класса MyTime"""
# m2 = MyTime(12,14,15)
# m = MyTime(m2)
# print(m)

"""нормальное отображение времени"""
# m2 = MyTime(21,123,113)
# print(m2)

"""магические методы сравнения, сложения, вычитания, умножения"""
time = MyTime(2,14,34)
time2 = MyTime(1,14,15)
# print(time == time2)
# print(time != time2)
# print(time < time2)
# print(time > time2)
# print(time <= time2)
# print(time >= time2)

# time.__sub__(time2)
# time.__add__(time2)
time.__mul__(time2)

print(time)
