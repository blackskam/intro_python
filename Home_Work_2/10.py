# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
#  а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
#  чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2
import random

number_coin = int(input('Введите количество монет: '))
eagle = 0
data = []
for i in range(0, number_coin):
    k = random.randrange(0, 2)
    data.append(k)
    eagle += k
print('Распределение монет: ', data)
if (number_coin - eagle) < (number_coin / 2):
    print('нужно перевернуть монет: ', number_coin - eagle)
else:
    print('нужно перевернуть монет:', eagle)
