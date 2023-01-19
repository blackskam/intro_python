# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B,
#  и возводит число А в целую степень B с помощью рекурсии.


def expon(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * expon(a, b-1)


a = int(input('Ведите число А: '))
b = int(input('Ведите число В: '))
print(expon(a, b))