"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""

import time


class Data(object):

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def converting(cls, date):
        day, month, year = map(int, date.split('-'))
        return day, month, year

    @staticmethod
    def validation(date):
        day, month, year = map(int, date.split('-'))
        try:
            load_date = time.strptime(date, "%d-%m-%Y")
        except ValueError:
            print('Неверная дата')
        else:
            print('С датой всё хорошо!')


your_date = input('Введите дату в формате «день-месяц-год»: ')
print(Data.converting(your_date))
print(Data.validation(your_date))
