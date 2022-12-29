# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику.
#  Она растет на круглой грядке, причем кусты высажены только по окружности.
#  Таким образом, у каждого куста есть ровно два соседних.
#  Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
#  поэтому ко времени сбора на них выросло различное число ягод – 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод,
#  которое может собрать за один заход собирающий модуль,
#  находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )

# Output: 9

import random


def random_array(n, k):
    num_array = []
    for i in range(0, n):
        num_array.append(random.randrange(1, k))
    return num_array



n = int(input('Ведите количество кустов, не менее 3-х: '))
k = 10
cluster = random_array(n, k)
print(cluster)
big_cluster = cluster[n-2] + cluster[n-1] + cluster[0]
for i in range(0, n-1):
    tmp = cluster[i-1] + cluster[i] + cluster[i+1]
    if tmp > big_cluster:
        big_cluster = tmp
print(big_cluster)
