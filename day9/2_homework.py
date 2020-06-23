class Car:

    def __init__(self, brand, model, year, speed=0):
        self._brand = brand
        self._model = model
        self._year = year
        self._speed = speed

    def more_speed(self, speed=5):
        self._speed += speed

    def less_speed(self, speed=5):
        self._speed -= speed

    def stop_speed(self, speed=0):
        self._speed = speed


    def yor_speed_now(self):
        return f"Ваша скорость сейчас {self._speed} км/ч"

# не понял про разворот, сделал минимальную скорость для разворота 1, максимальную - 20
# т.е. если скорость машины выше 20 км/ч, то понижаем до 20 и делаем разворот, если скорость в промежутке
# от 1 до 20, то оставляем такую же скорость для разворота

    def turn_speed(self):
        if self._speed > 0 and self._speed <= 20:
            return self._speed
        else:
            self._speed = 20
            return self._speed


car = Car('Mersedes', 'w140 s600', 2010)
car.more_speed()
car.more_speed()
car.more_speed()
car.more_speed()
car.more_speed()

print(car.yor_speed_now())
print(car.turn_speed())