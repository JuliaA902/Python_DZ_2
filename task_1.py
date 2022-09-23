# Подсчитать сумму цифр в вещественном числе.

from curses.ascii import isdigit


s = input("Введите число: ")
suma = 0
for i in s:
    if i.isdigit():
        suma = suma + int(i)
print(f'Сумма цифр числа {suma}')

    







