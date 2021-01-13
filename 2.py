'''Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.'''

from random import randint

my_list = [randint(0, 100) for el in range(0, 15)]

new_list = []
for i in range(0, len(my_list)-1):
    if my_list[i] < my_list[i + 1]:
        new_list.append(my_list[i + 1])

print(my_list)
print(new_list)
