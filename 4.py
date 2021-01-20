'''Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала со скоростью {self.speed} км/ч')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, turn):
        if turn == chr(108): # 'l'
            print('Машина повернула налево.')
        elif turn == chr(114): # 'r'
            print('Машина повернула направо.')
        else:
            print('Машины так не ездят.')

    def show_speed(self):
        print(f'Скорость {self.name} равна {self.speed} км/ч')

class TownCar(Car):
    MAXSPEED = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def overspeed(self):
        if self.speed > self.MAXSPEED:
            print(f'Текущая скорость {self.speed} км/ч. Превышение скорости для городского автомобиля!')

class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

class WorkCar(Car):
    MAXSPEED = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
        print(f'Это полицейская машина? {self.is_police}')

    def overspeed(self):
        if self.speed > self.MAXSPEED:
            print(f'Текущая скорость {self.speed} км/ч. Превышение скорости для спецтехники!')

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)
        print(f'Это полицейская машина? {self.is_police}')

c = Car(50, 'white', 'Mazda', False)
c.turn(input('Введите направление поворота (l/r): '))
c.show_speed()

t = TownCar(80, 'black', 'BMW')
t.go()
t.overspeed()
t.stop()

p = PoliceCar(60, 'blue', 'Lada')
p.show_speed()

w = WorkCar(50, 'orange', "MAN")
w.go()
w.overspeed()
w.stop()
