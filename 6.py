a = float(input('Количество километров пройденных за первый день равно: '))
b = float(input('Минимальное количество километров, которое надо пройти: '))

count = 1
while b >= a:
    a += a * 0.1
    count += 1
print(f'на {count}-й день спортсмен достигнет результата — не менее {b} км')