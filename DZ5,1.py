# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
A = int(input('Enter a number A > '))
B = int(input('Enter a number B > '))

def Degree(a,b):
    if b == 0:
     return 1
    return a *Degree(a,b-1)
    
print(Degree(A,B))    
