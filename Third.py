# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input("Введите число: "))
list = []
i = 1
while len(list) != k:
    list.append(round((1+1/i)**i,2))
    i+=1
print(list)
result = 0.0
print(type(list[1]))
k = 0
while len(list) != k:
    result = result + list[k]
    k += 1
print(result)