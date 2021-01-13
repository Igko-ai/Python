'''Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.'''

from random import randint

my_list = [randint(1, 10) for el in range(0, 15)]
print(my_list)

print([new_el for new_el in my_list if my_list.count(new_el) == 1])
