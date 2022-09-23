#Реализовать алгоритм перемешивания списка.

import random
list_1 = [1, 3, 5, 7, 9]
print("Введен список: ", (list_1))
for i in range(len(list_1) -1, 0, -1):
    f = random.randint(0, i +1)
    list_1[i], list_1[f] = list_1[f], list_1[i]
print("Список перемещан: ", (list_1))
    