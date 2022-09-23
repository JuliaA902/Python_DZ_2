# Задать список из n чисел последовательности  (1 + 1/n)^n 
# и вывести на экран их сумму.

n = int(input("Введите число N: "))
s = 0
b = {}
sum = 0
for i in range(1, n+1):
    s = (1+1/i)**i
    b[i] = s
    sum += s
    print(s)
print(b)
print(sum)
    