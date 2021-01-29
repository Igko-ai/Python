"""Продолжить работу над первым заданием.Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании.Для хранения данных о наименовании и количестве единиц оргтехники, а
также других данных, можно использовать любую подходящую структуру, например словарь."""


class Warehouse:
    def __init__(self):
        self.dict = {}

    def to_add(self, equipment):
        self.dict.setdefault(equipment.group_name(), []).append(equipment)

    def transfer_from(self, model):
        if self.dict[model]:
            self.dict.setdefault(model).pop(1)


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
