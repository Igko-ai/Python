'''Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.'''

a = [9, 5, 4, 3, 3, 2]
while len(a) != 500:    #пока не надоест в общем
    number = int(input("Введите натуральное число (рейтинг): "))
    a.append(number)
    if a[0] >= a[1]:
        a.sort(reverse=True)
        print(a)
    else:
        a.sort()
        print(a)
