"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица."""

from random import randint
import numpy as np


class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return f"Матрица \n {np.array(self.lst)}"

    def __add__(self, other):
        for i in range(len(self.lst)):
            for j in range(len(other.lst[0])):
                self.lst[i][j] = self.lst[i][j] + other.lst[i][j]
            result = self.lst
        return Matrix(result)


m = int(input("Введите количество столбцов: "))
n = int(input("Введите количество строк: "))
matrix_1 = Matrix([[randint(0, 20) for m in range(m)] for n in range(n)])
matrix_2 = Matrix([[randint(0, 20) for m in range(m)] for n in range(n)])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
