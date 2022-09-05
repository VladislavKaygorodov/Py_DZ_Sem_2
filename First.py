# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

def Sum_Numbers(num):
    i=0
    result = 0
    while i < len(num):
        result = result + int(num[i])
        i +=1
    return result

select_Num =input('Введите вещественное число: ')
list = select_Num.split('.')
if len(list) == 2:
    first_Num = Sum_Numbers(list[0])
    second_Num = Sum_Numbers(list[1])
    print(first_Num + second_Num)
else:
    print("Введите корректное значение")