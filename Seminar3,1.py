# first_list = [9, 'fkr', True, [1, 2, 3]]

# for i, elemnt in enumerate(first_list):
#     if elemnt == 9:
#         first_list[i] = 'nine'









# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

list_1 = []
length = int(input('Enter length of list > '))

for i in  range(length):
    list_1.append(int(input()))

print(list_1)

count = 0
for i in range(length):
    if list_1[i] != list_1[i - 1]:
        count += 1 
 
print(count)