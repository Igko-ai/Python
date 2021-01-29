"""Реализовать проект «Операции с комплексными числами».Создайте класс «Комплексное число», реализуйте
перегрузку методов сложения и умножения комплексных чисел.Проверьте работу проекта, создав экземпляры
класса(комплексные числа) и выполнив сложение и умножение созданных экземпляров.Проверьте корректность
полученного результата."""


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма комплексных чисел: {self.a + other.a}+{self.b + other.b}j'

    def __mul__(self, other):
        return f'Произведение комплексных чисел: {self.a * self.b - other.a * other.b}+' \
               f'{self.a * other.b + self.b * other.a}j'


a = Complex(1, 2)
b = Complex(2, 2)
print(a + b)
print(a * b)


# проверка
class ComplexCheck:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return complex(self.first) + complex(self.second)

    def mul(self):
        return complex(self.first) * complex(self.second)


a = ComplexCheck(1 + 2j, 2 + 2j)
print("Проверка")
print(f'Сумма комплексных чисел: {a.add()}')
print(f'Произведение комплексных чисел: {a.mul()}')
