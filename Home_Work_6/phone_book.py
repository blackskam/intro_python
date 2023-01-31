# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# .
# Структура данных:
# Фамилия, имя, отчество, номер телефона.
# .
# Пример данных:
# Ivanov, Ivan, Ivanovich, +79111234567
# Petrov, Petr, Petrovich, +79119876543
# .
# Функции справочника:
# - Показать все записи
# - Найти запись по вхождению частей имени
# - Найти запись по телефону
# - Добавить новый контакт
# - Удалить контакт
# - Изменить номер телефона у контакта
# .
# Пример работы программы:
# .
# При запуске программы пользователю выдается меню:

# Введите номер действия:
# 1 - Показать все записи
# 2 - Найти запись по вхождению частей имени
# 3 - Найти запись по телефону
# 4 - Добавить новый контакт
# 5 - Удалить контакт
# 6 - Изменить номер телефона у контакта
# 7 - Выход

# .
# После выбора действия выполняется функция, реализующая это действие.
# После завершения работы функции пользователь возвращается в меню.

import os
import re


def writeFile(file_name, listTelbook):
    with open(file_name, 'a') as book:
        book.write('\n' + listTelbook[0] + ',' + listTelbook[1] +
                   ',' + listTelbook[2] + ',' + listTelbook[3])


def lineDelete(file_name, numLine):
    with open(file_name, 'r') as book:
        lines = book.readlines()
    del lines[numLine]
    with open(file_name, 'w') as book:
        book.writelines(lines)


def telChange(file_name, line_change, tel_change):
    listbook = readFile(file_name)
    listbook[line_change-1][3] = str(tel_change)
    with open(file_name, 'w') as book:
        for line in listbook:
            book.writelines(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + '\n')


def readFile(file_name):
    listTelbook = []
    try:
        with open(file_name, 'r+') as data:
            for line in data:
                if line != '\n':
                    listTelbook.append(re.split(',|\n', line))
    except FileNotFoundError:
        print('Телефонная книга не найдена, добавтье контакты!')
    return listTelbook


def printFile(listbook):
    count = 1
    for line in listbook:
        print(str(count) + ". " + line[0] + " " + line[1] + " " + line[2] + ", " + line[3])
        count += 1


def findUsers(listTelbook, surname, name, patronymic):
    rezult = []
    for entry in listTelbook:
        if entry[0].lower() == surname and entry[1].lower() == name and entry[2].lower() == patronymic:
            rezult = entry
    return rezult


def findNumber(userList, telephone):
    rezult = []
    for user in userList:
        if user[3] == telephone:
            rezult = user
    return rezult


def printMenu():
    clear()
    print('1 - Показать все записи')
    print('2 - Найти запись по вхождению частей имени')
    print('3 - Найти запись по телефону')
    print('4 - Добавить новый контакт')
    print('5 - Удалить контакт')
    print('6 - Изменить номер телефона у контакта')
    print('7 - Выход')


def clear():
    return os.system('cls')


fileName = 'phone_book.txt'
while True:
    printMenu()
    inMenu = input('Введите команду: ')
    match inMenu:
        case '1':
            printFile(readFile(fileName))
            print()
            input()
        case '2':
            surname = input('Введите фамилию: ').lower()
            name = input('Введите имя: ').lower()
            patronymic = input('Введите отчество: ').lower()
            rezult = findUsers(readFile(fileName), surname, name, patronymic)
            if len(rezult) == 0:
                print('По данным ФИО записей телефона нет!')
            else:
                print(rezult[3])
            input()
        case '3':
            telephone = input('Введите номер телефона: ')
            rezult = findNumber(readFile(fileName), telephone)
            if len(rezult) == 0:
                print('По данному телефону записей нет!')
            else:
                print(rezult[0] + ' ' + rezult[1] + ' ' + rezult[2])
            input()
        case '4':
            listWrite = []
            listWrite.append(input('Введите фамилию: '))
            listWrite.append(input('Введите имя: '))
            listWrite.append(input('Введите отчество: '))
            listWrite.append(input('Введите телефон: '))
            writeFile(fileName, listWrite)
        case '5':
            printFile(readFile(fileName))
            print()
            numDel = int(input('Введите номер записи для удаления: '))
            lineDelete(fileName, numDel)
        case '6':
            printFile(readFile(fileName))
            print()
            line_change = int(
                input('Введите номер записи для изменения номера телефона: '))
            tel_change = int(input('Введите новый номер телефона: '))
            telChange(fileName,line_change,tel_change)
        case '7':
            break
