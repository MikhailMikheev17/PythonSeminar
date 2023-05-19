# print('a', 'c', 'b', sep ='-', end = '\n') #\n - перенос строки , \t - табуляция
# print(1, 2, 3, sep = '+')

# name = input('Enter your name :\n') 
# print(f'Hello,{name}!')

# num = int(input('Enter a number :\n'))

# if num < 0:
#     print('Меньше нуля ')
# elif num % 2 == 0:
#     print('Четное')
#     if num % 3 == 0:
#         print('Делиться на 3 ')         
# else :
#     print('Нечетное')       

# a = [1,2,3,4]

# for element in a :
#     print(element)

# for i in range(len(a)):
#     if a[i] > 2:
#         print(f'{i}-th elem > 2')

# for i, el in enumerate(a): # важно для собесов 
#     if el > 2:
#         print(f'{i}-th element > 2 ')
# ['a' , 'b', 'c']
# (0,'a')
# (1,'b')
# (2,'c')

# for i in range(0,10,2):
#     print(i)

# n = 10
# while n > 1:
#     print(n)
#     n -= 1

# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

import math 
# from math import ceil 
n = int(input('Enter km per day :'))
m = int(input('Enter km way :'))

print(math.ceil(m/n))# округление вверх

