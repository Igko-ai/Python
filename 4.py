"""Начните работу над проектом «Склад оргтехники».Создайте класс, описывающий склад.А также
класс «Оргтехника», который будет базовым для классов - наследников.Эти классы — конкретные
типы оргтехники(принтер, сканер, ксерокс).В базовом классе определить параметры, общие
для приведенных типов.В классах - наследниках реализовать параметры, уникальные для каждого
типа оргтехники."""


class Warehouse:
    pass


class Equipment:
    def __init__(self, model, series):
        self.model = model
        self.series = series
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.model} {self.series}'


class Printer(Equipment):
    def __init__(self, model, series, print_in_minute):
        super().__init__(model, series)
        self.print_in_minute = print_in_minute

    def work(self):
        return f'Модель {self.model} серии {self.series} печатает {self.print_in_minute} станиц в минуту'


class Scanner(Equipment):
    def __init__(self, model, series, scan_in_minute):
        super().__init__(model, series)
        self.scan_in_minute = scan_in_minute

    def work(self):
        return f'Модель {self.model} серии {self.series} сканирует{self.scan_in_minute} станиц в минуту'


class Copy(Equipment):
    def __init__(self, model, series, copy_in_minute):
        super().__init__(model, series)
        self.copy_in_minute = copy_in_minute

    def work(self):
        return f'Модель {self.model} серии {self.series} копирует {self.copy_in_minute} станиц в минуту'
