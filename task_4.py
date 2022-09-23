#Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
#Позиции хранятся в файле в file.txt одной строке одно число.

n = int(input("Введите число N: "))
l = "1, 2, 3, 4, 5" 
s = 0
c = 1
l1 = []
for i in range(-n, n+1):
    l1.append(i)
with open(" ./DZ_2/list.txt", 'r') as f:
    l = f.readline()    
l2 = l.split(',')
print(l)
print(l1)    
print(l2)
for i in l2:
    print(i)
    c = c *l1[int(i.strip())]
print(c)

