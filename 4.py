number = int(input('Введите целое положительное число: '))
if number <= 0:
    print('Это не положительное число!')
else:
    a = 0
    while number > 0:
        b = number % 10
        number //= 10
        if b > a:
            a = b
    print('Самая большая цифра в выбранном числе:', a)
print('Конец!')