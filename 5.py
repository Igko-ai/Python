'''Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    title = "Использование канцелярских принадлежностей"
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('Используем для отрисовки ручку.')

class Pencil(Stationery):
    def draw(self):
        print('Используем для отрисовки карандаш.')

class Handle(Stationery):
    def draw(self):
        print('Используем для отрисовки маркер.')

headline = Stationery().title
print(headline)

draw = Stationery()
draw.draw()

draw_pen = Pen()
draw_pen.draw()

draw_pencil = Pencil()
draw_pencil.draw()

draw_handle = Handle()
draw_handle.draw()
