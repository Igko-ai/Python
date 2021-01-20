'''Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.'''

class Road:
    DENSITY = 25 # плотность - константа

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self, thickness):
        self.thickness = thickness
        return self._length * self._width * self.thickness * self.DENSITY

asfalt = Road(float(input('Введите длину дороги, м: ')), float(input('Введите длину дороги, м: ')))
res = asfalt.massa(float(input('Введите толщину покрытия, м: ')))
print(f'Необходимая масса асфальта {round(res, 2)} кг')
