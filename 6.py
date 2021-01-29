"""Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных."""


class WarehouseError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddError(WarehouseError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferError(WarehouseError):
    def __init__(self, text):
        self.text = f"Невозможно отправить товар со склада:\n {text}"


class Warehouse:
    def __init__(self):
        self.dict = {}

    def to_add(self, equipment):
        try:
            if isinstance(equipment, int):
                raise AddError(f"Недопустимый тип данных: '{type(equipment)}'")
        except AddError as a_err:
            print(a_err)
        else:
            self.dict.setdefault(equipment.group_name(), []).append(equipment)

    def transfer_from(self, model):
        try:
            if isinstance(model, int):
                raise TransferError(f"Недопустимый тип данных: '{type(model)}'")
        except TransferError as t_err:
            print(t_err)
        else:
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


warehouse = Warehouse()
xerox = Copy('Canon', '2206', 50)
print(xerox.work())
warehouse.to_add(xerox)
printer = Printer('HP', 'M15', 70)
warehouse.to_add(printer)
xerox = Copy('Canon', '1225', 45)
warehouse.to_add(xerox)
scan = Scanner('HP', 'Pro3500', 25)
warehouse.to_add(scan)
printer = Printer('Epson', 'L132', 60)
warehouse.to_add(printer)
print(warehouse.dict)

warehouse.transfer_from('Printer')
print(warehouse.dict)

