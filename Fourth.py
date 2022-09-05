# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях. 

import random

size = int(input("Введите число: "))
list = []
while len(list) != size:
    list.append(random.randint(-size,size))
print(list)

x = input("Введите позиции элементов для умножения через пробел: ")

print(f"Проверяем на наличие лишних и ошибочных элементов из указанных выше позиций")

temp_List = []
i=0
count = 0
temp = ""

while i< len(x):
    if x[i] != " ":
        if "0"<=x[i]<="9":
            temp += x[i]
            i +=1
            if i == len(x):
                temp_List.append(int(temp))
                break
        else:
            i +=1
    elif (x[i] == " ") and (temp != ""):
        temp_List.append(int(temp))
        temp = ""
        i+=1
    elif temp == "":
        i+=1
    elif i == len(x):
        temp_List.append(int(temp))

print(f"Отсеиваем от лишних символов : {temp_List}")

index = 0
while index < len(temp_List):
    if temp_List[index] > len(list):
        temp_List.pop(index)
    else:
        index +=1

print(f"Отсеиваем от лишних чисел выходящих за пределы размерности списка : {temp_List}")

j = 1
result = list[temp_List[0]-1]
temp_int = list[temp_List[0]-1]

while j < len(temp_List):
    result = result * (list[temp_List[j]-1])
    print(f"{temp_int} * {list[temp_List[j]-1]} = {result}")
    temp_int = result
    j +=1

print(f"Результат умножения указанных чисел: {result}")