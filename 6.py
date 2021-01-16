'''Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.'''

with open('6.txt') as f:
    read = f.readlines()
    res = []
    for line in read:
        s = line.split()
        #далее извлекаем из строк количество часов по каждому виду занятий для каждой дисциплины
        num = ''
        num_list = []
        for char in line:
            if char.isdigit():
                num = num + char
            else:
                if num != '':
                    num_list.append(int(num))
                    num = ''
        if num != '':
            num_list.append(int(num))

        res.append(s[0])
        res.append(sum(num_list))
    res_dict = {res[i]: float(res[i + 1]) for i in range(0, len(res), 2)}
    print(res_dict)
