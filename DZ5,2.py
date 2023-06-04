# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

A = int(input('Enter a number A > '))
B = int(input('Enter a number B > '))

def sum(a, b):
    if a < 0 or b < 0: print('error') 
    if a == 0:
        return b
    else:
        return sum(a - 1, b + 1)


print(sum(A, B))