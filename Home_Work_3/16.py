# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число,
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2


import random


n = int(input('Ведите количество элементов в массиве: '))
x = int(input('Ведите чилсо для проверки повторяемости: '))
num_array = []
k = 0
for i in range(0, n):
    num_array.append(random.randrange(1, n/2 + 1))
    if num_array[i] == x:
        k += 1
print(num_array)
print(k)
