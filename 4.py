'''Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки нужно пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.'''

data = list(input('Введите строку: ').split())
a = []

for i in range (len(data)):
    if len(data[i]) > 10:
        data[i] = data[i][:10]

for ind, el in enumerate(data):
    print(ind, el)