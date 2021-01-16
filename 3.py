'''Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.'''

def create_list(var):
    new_list = []
    for line in var:
        s = line.split()
        new_list += s
    return new_list

with open('3.txt') as f:
    peronal_list = create_list(f.readlines())
    peronal_dict = {peronal_list[i]: float(peronal_list[i + 1]) for i in range(0, len(peronal_list), 2)}

summa = []
for key, value in peronal_dict.items():
    summa.append(value)
    if value < 20000:
        print(f'Сотрудник {key} получает меньше 20000. Его оклад составляет: {value}')
    else:
        print(f'Сотрудник {key} получает больше 20000. Его оклад составляет: {value}')
        # если его не выводить (в задании этого не просили), то вместо print будет continue
print(f'Средняя зарплата сотрудников: {round(sum(summa)/len(summa), 2)}')
