# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 6
# -> 5

list_1 = []
length = int(input('Enter length of list > '))

for i in  range(length):
    list_1.append(int(input()))

print(list_1)

k = int(input('k = '))

min = abs(k - list_1[0])
index = 0
for i in range(1, length):
      count = abs(k - list_1[i])
      if count < min:
            min = count
            index = i
print(f'Число {list_1[index]} в списке  наиболее близко по величине к числу {k}, их разница {abs(k - list_1[index])}')5
