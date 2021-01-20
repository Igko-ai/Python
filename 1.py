'''Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
import time

class TrafficLight:
    __color = ['r', 'y', 'g']

    def running(self, color):
        if color == self.__color[0]:
            print('\033[41m')
            time.sleep(1)
        elif  color == self.__color[1]:
            print('\033[43m')
            time.sleep(1)
        elif  color == self.__color[2]:
            print('\033[42m')
            time.sleep(1)
        else:
            print('Нет такого цвета!')

traffic_light = TrafficLight()
# переключатель с защитой от неверной последовательности ввода
a = [' ']
count = 0
while True:
    col = input('Введите цвет светофора (r/y/g)')
    traffic_light.running(col)
    print('\033[0m')
    a.append(str(col))
    if a[count] == 'r' and a[count + 1] != 'y':
        break
    elif a[count] == 'y' and a[count + 1] != 'g':
        break
    elif a[count] == 'g' and a[count + 1] != 'r':
        break
    count += 1
print('Неверная последовательность цветов!')

'''ещё можно просто без ручных переключений запустить cо счётчиком, чтобы задать количество циклов переключений
но тогда получается __color не нужен, т.е. выходит не совсем корректный вариант исходя из условия,'''
#     def running(self):
#         print('\033[41m')
#         time.sleep(7)
#         print('\033[43m')
#         time.sleep(2)
#         print('\033[42m')
#         time.sleep(5)
# try:
#     count = int(input('Введите число повторений: '))
# except ValueError:
#     print('Это не целое число. Светофор сломался.')
# else:
#     n = 0
#     while count > n:
#         traffic_light.running()
#         print('\033[0m')
#         n += 1


