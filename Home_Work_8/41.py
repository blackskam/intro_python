# Вычислить значение выражения. Уровень 1, 2, 3, 4.


def calc(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b


def calcPriority(list):
    list2 = []
    for i in range(1, len(list), 2):
        if list[i] == '*' or list[i] == '/':
            if i > 1 and (list[i-2] == '*' or list[i-2] == '/'):
                list2[-1] = calc(int(list2[-1]), int(list[i+1]), list[i])
            else:
                rezult = calc(int(list[i-1]), int(list[i+1]), list[i])
                list2.append(rezult)
        else:
            if list[i-2] == '*' or list[i-2] == '/':
                list2.append(list[i])
                if i == (len(list) - 2):
                    list2.append(list[i+1])
            else:
                list2.append(list[i-1])
                list2.append(list[i])
                if i == (len(list) - 2):
                    list2.append(list[i+1])
    return list2


def calcBrackets(list):
    list2 = []
    k = 0
    for i in range(len(list)):
        if list[i] == '(':
            rezult = calc(int(list[i+1]), int(list[i+3]), list[i+2])
            list2.append(rezult)
            k += 5
        elif i == k:
            list2.append(list[i])
            k += 1
    return list2


def calcList(list):
    rezult = list[0]
    for i in range (1, len(list) - 1, 2):
        rezult = calc(int(rezult), int(list[i+1]), list[i])
    return rezult


def menu():
    while True:
        list_expr = input('Введите выражение: ').split()
#       list_expr = '( 1 + 3 ) * 2 * 4 - 6 / 2 + ( 7 - 2 ) * 3 + 1'   # 45
        print(calcList(calcPriority(calcBrackets(list_expr))))
        choice = input('Введите "0" для выхода или "1" для повтора: ')
        if choice == "0":
            break


menu()
