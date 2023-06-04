# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

n = int(input("Введите число: "))

def is_prime(n: int, divider: int) -> bool:
    if divider == 1:
        return True
    if n % divider == 0:
        return False
    return is_prime(n, divider - 1)
          

print(is_prime(n,n //2 +1))          