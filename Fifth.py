# Реализуйте алгоритм перемешивания списка.

import random

k = int(input("Введите число: "))
list = []
while len(list) != k:
    list.append(random.randint(-k,k))
print(list)
random.shuffle(list)
print(list)