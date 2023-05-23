# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

num = int(input('Enter a number > '))

fact = 1
i = 1

# while i <= num:
#     if num == 0 :
#         print(f'{num}! = 1')
#     fact *= i
#     i += 1
# print(f'{num}! = {fact}')

j = 1
factorial = 1
res = 1 

for j in range(num):
    res *= factorial
    factorial += 1

print(f'{num}! = {res}')