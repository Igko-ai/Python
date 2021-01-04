initial_time = int(input("Введите количество секунд: "))

hours = initial_time // 3600
minutes = initial_time // 60 % 60
seconds = initial_time % 60

print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))