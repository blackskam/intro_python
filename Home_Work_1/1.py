"""
Задача 2
Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
print('Ведите трехзначное число:')
number = input()
if 99 < int(number) < 1000:
    print(int(number[0]) + int(number[1]) + int(number[2]))
else:
    print('Вы ввели не трехзначное число!')
