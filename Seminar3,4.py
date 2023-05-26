# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)


list_1 = []
length = int(input('Enter length of list > '))

for i in  range(length):
    list_1.append(int(input()))

count = 0

for i in range(length - 1):
    if list_1[i]>list_1[i+1]:
        count += 1

print(f'Count = ',count)
