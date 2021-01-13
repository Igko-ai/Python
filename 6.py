'''Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.'''

from itertools import count, cycle

first = int(input('Введите первое число: '))
last = int(input('Введите последнее число: '))

for el in count(first):
    if el > last:
        break
    else:
        print(el)

text = input('Введите слово: ')
num = int(input('Сколько раз повторить это слово в столбик: '))
a = 0
for letter in cycle(text):
    if a > len(text) * num - 1:
        break
    print(letter)
    a += 1
