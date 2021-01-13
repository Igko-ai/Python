'''Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.'''

from math import factorial
from itertools import count

def fact(n):
    for el in count(1):
        if el > n:
            break
        else:
            yield factorial(el)

n = int(input('Введите число n: '))
for el in fact(n):
    print (el)
