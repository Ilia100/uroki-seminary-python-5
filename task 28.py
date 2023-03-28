# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def sum(count1, count2): 
    if count1 > 0:
        return sum(count1-1,count2)+1
    if count2 > 0:
        return sum(count1,count2-1)+1
    else:
        return 0

Num1 = int(input('Введите первое число: '))
Num2 = int(input('Введите второе число: '))

print(f"{Num1} + {Num2} =", sum(Num1,Num2))