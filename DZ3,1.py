# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 3
# -> 1

list_1 = []
length = int(input('Enter length of list > '))
k = int(input('k = '))

for i in  range(length):
    list_1.append(int(input()))

print(list_1)

count = 0
for i in range(length):
    if list_1[i] == k : count += 1

print(f'count {k} = {count}')    