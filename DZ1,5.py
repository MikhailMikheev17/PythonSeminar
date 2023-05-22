# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

q = int(input('Entet the first side > '))
w = int(input('Entet the second side > '))
e = int(input('Entet a number of slices > '))

if q % e or w % e :
    print('YES')
else:
    print('NO')    

