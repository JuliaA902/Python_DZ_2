#Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.


n = int(input("введите число: "))
f = 1
list = []
for i in range(1, n+1):
    f = f * i
    list.append(f)
    print(f)
print(list)

