'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

eng_voc = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('4.txt') as f:
    read = f.readlines()
    for line in read:
        s = line.split()
        new =  open('translate.txt', 'a')
        new.write(' '.join(eng_voc.get(x, x) for x in s) + '\n')
