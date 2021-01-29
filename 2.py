"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class DivByZeroError(Exception):
    def __init__(self, *args):
        self.first = first
        self.second = second


first = float(input('Введите делимое: '))
second = float(input('Введите делитель: '))

try:
    if second == 0:
        raise DivByZeroError('На ноль делить нельзя!')
    else:
        res = first / second
except DivByZeroError as err:
    print(err)
else:
    print(f'Результат деления: {round(res, 2)}')
finally:
    print('Программа завершена.')
