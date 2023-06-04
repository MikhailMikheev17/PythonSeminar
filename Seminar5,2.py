# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

list_1 = []
length = int(input('Enter length of list > '))

for i in  range(length):
    list_1.append(int(input()))

print(list_1)


def findmax(list_1):
    max = list_1[0]
    for i in range(length):
      if list_1[i] > max:
        max = list_1[i]
    return max    

def findmin(list_1):
    min = list_1[0]
    for i in range(length):
        if list_1[i] < min:
         min = list_1[i]
    return min    

def zamena(list_1,max,min):
    for i in range(length):
      if list_1[i] == max:
         list_1[i] = min
    return list_1

max = findmax(list_1)
print(max)  

min = findmin(list_1)
print(min)

print(zamena(list_1,max,min)) 