# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12
import random


def random_array(n, k):
    num_array = []
    for i in range(0, n):
        num_array.append(random.randrange(1, k))
    return num_array


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


n = int(input('Ведите количество элементов первого набора: '))
m = int(input('Ведите количество элементов второго набора: '))
k = 100
num_array1 = random_array(n, k)
num_array2 = random_array(m, k)
print(num_array1)
print(num_array2)
num_set = set(num_array1) & set(num_array2)
print(bubble_sort(list(num_set)))
