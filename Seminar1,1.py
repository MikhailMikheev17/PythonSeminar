# print('a', 'c', 'b', sep ='-', end = '\n') #\n - перенос строки , \t - табуляция
# print(1, 2, 3, sep = '+')

# name = input('Enter your name :\n') 
# print(f'Hello,{name}!')

num = int(input('Enter a number :\n'))

if num < 0:
    print('Меньше нуля ')
elif num % 2 == 0:
    print('Четное')
    if num % 3 == 0:
        print('Делиться на 3 ')         
else :
    print('Нечетное')       