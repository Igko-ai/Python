'''Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Итоговый список сохранить в виде json-объекта в соответствующий файл.'''

import json

def average_no_negative(var):
    # вычисляем среднее без отрицательных значений
    try:
        var = [x for x in var if x >= 0]
        return sum(var) / len(var)
    except:
        print('Ошибка! Это не может быть просто число!')

with open('7.txt') as f:
    read = f.readlines()
    profit = []
    firm_list = []
    final_list = []
    for line in read:
        s = line.split()
        for i in range(2, len(s)-1):
            delta = int(s[i]) - int(s[i + 1])
            profit.append(delta) # для вычисления среднего
            firm_list.append(s[0])
            firm_list.append(delta)
    firm_dict = {firm_list[i]: firm_list[i + 1] for i in range(0, len(firm_list), 2)}

    av = average_no_negative(profit)
    av_dict = {"average_profit": round(av, 2)}

    final_list.append(firm_dict)
    final_list.append(av_dict)
    print(final_list)

with open("final_list.json", "w") as j:
    json.dump(final_list, j)


