# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
#Для решения данной задачи используйте функцию .split()

a = input('Введите строку через пробел > ').split()

print(a)
#print(list(a))

stringA = ''
for i in range(len(a)):
    if a[0:i].count(a[i]) == 0:
        stringA += f'{a[i]} '
    else: stringA += f'{a[i]}_{a[0:i].count(a[i])} '  

print(stringA)




    