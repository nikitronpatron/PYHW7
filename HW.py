
import codecs

def Import():
    print("Введите имя, фамилию, телефон и описание через enter: ")
    name = input()
    surname = input()
    number = int(input())
    description = input()
    dataList = codecs.open("Data.txt", "a+", "utf-8")
    dataList.write(f"*{name} {surname}: {number}. {description}*\n")
    dataList.close()

def Export():
    dataList = codecs.open("Data.txt", "r", "utf-8")
    export = dataList.read()
    print(export)
    dataList.close()

def Main():
    start = int(input("Введите номер операции, которую необходимо выполнить:\n1. Добавить нового абонента.\n2. Вывести список всех абонентов.\n"))
    if start == 1:
        inPut = Import()
    elif start == 2:
        outPut = Export()
    else:
        print("Ошибка!")
Main()