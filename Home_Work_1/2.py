"""
Задача 4
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно,
 что Петя и Сережа сделали одинаковое количество журавликов,
 а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Пример:
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
"""
print("Введите общее количество журавликов кратное 6:")
all = int(input())
if all % 6 == 0:
    print(f'Петя сделал {all/6:.0f}, Катя {all*2/3:.0f}, Серёжа {all/6:.0f} журавликов!')
else:
    print("Вы ыыели число не кратное 6!")