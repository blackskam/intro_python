# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число,
#  которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X,
#  выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random


def bubble_sort(arr):
    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True
    return arr


n = int(input('Ведите количество элементов в массиве: '))
x = int(input('Ведите чилсо для проверки повторяемости: '))
num_array = []
num_array2 = []
for i in range(0, n):
    num_array.append(random.randrange(1, n))
print(num_array)
num_array2 = bubble_sort(num_array)
if x in num_array2:
    print(x)
elif num_array2[0] > x:
    print(num_array[0])
elif num_array2[-1] < x:
    print(num_array2[-1])
else:
    for i in range(0, len(num_array2) - 1):
        if num_array2[i] < x and x < num_array2[i+1]:
            if num_array2[i+1] - x >= x - num_array2[i]:
                print(num_array2[i])
            else:
                print(num_array2[i+1])


