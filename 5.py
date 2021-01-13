'''Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.'''

from functools import reduce

def prod(el_1, el_2):
    return el_1 * el_2

print (f'Результат умножения: {reduce(prod, [even_num for even_num in range(100, 1001) if even_num % 2 == 0])}')
