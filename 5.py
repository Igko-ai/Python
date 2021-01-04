proceeds = int(input('Введите выручку предприятия: '))
costs = int(input('Введите издержки предприятия: '))

if proceeds - costs > 0:
    print("Выручка предприятия больше издержек. Работаем с прибылью.")
    print(f'Рентабельность предприятия равна {(proceeds - costs) / proceeds:.2f}')
    number_of_employees = int(input('Введите количество сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника равна {(proceeds - costs) / number_of_employees:.2f}')
elif proceeds == costs:
    print("Выручка предприятия равна издержкам.\nРентабельность предприятия равна нулю")
else:
    print("Издержки предприятия больше выручки. Работаем в убыток.")