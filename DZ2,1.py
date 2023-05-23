# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

num = int(input('Enter num of coins > '))
i = 0
# решка - 1, орел - 0 
count_reshka = 0
count_orel = 0
for i in range(num):
    coin = int(input())
    if coin == 1:
        count_reshka += 1
    else:
        count_orel += 1  
print(f'We have {count_reshka} reshka and {count_orel} orel')

if count_reshka > count_orel:
    print(f'We need to turn it over {count_orel} сoins')
elif count_orel > count_reshka:
    print(f'We need to turn it over {count_reshka} сoins')

