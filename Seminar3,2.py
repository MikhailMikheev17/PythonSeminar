# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

list_1 = []
length = int(input('Enter length of list > '))
k = int(input('k = '))
for i in  range(length):
    list_1.append(int(input()))

print(list_1)

for i in range(k):
    tmp = list_1[-1]
    list_1.insert(0, tmp)
    list_1.pop()

print(list_1)

# list = [1, 2, 3, 4, 5]
# k = int(input('k = '))

# for i in range(k - 1):
#     list.insert(0, list.pop())
# print(list)





# for i in range(k-1):
#     list_1.insert(0, list_1.pop()) # list.pop - извлекает последний элемент, 
# print(list_1)  