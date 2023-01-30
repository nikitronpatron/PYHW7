
import codecs

def Import():
    print("Введите имя, фамилию, класс ученика через enter: ")
    name = input()
    surname = input()
    number = input()
    dataList = codecs.open("Data.txt", "a+", "utf-8")
    dataList.write(f"*{name} {surname}, {number}.*\n")
    dataList.close()

def Export():
    dataList = codecs.open("Data.txt", "r", "utf-8")
    export = dataList.read()
    print(export)
    dataList.close()

def Class():
    clas = input("Введите номер класса: ")
    dataList = codecs.open("Data.txt", "r", "utf-8")
    lst = dataList.readlines()
    for i in lst:
        if clas in i:
            print(i)

def StudentName():
    clas = input("Введите имя ученика: ")
    dataList = codecs.open("Data.txt", "r", "utf-8")
    lst = dataList.readlines()
    for i in lst:
        if clas in i:
            print(i)

def StudentSurname():
    clas = input("Введите фамилию ученика: ")
    dataList = codecs.open("Data.txt", "r", "utf-8")
    lst = dataList.readlines()
    for i in lst:
        if clas in i:
            print(i)


def Main():
    start = int(input("Введите номер операции, которую необходимо выполнить:\n1. Добавить нового ученика.\n2. Вывести список всех учеников.\n3. Вывести учеников класса.\n4. Вывести учеников по имени.\n5. Вывести учеников по фамилии.\n"))
    if start == 1:
        inPut = Import()
    elif start == 2:
        outPut = Export()
    elif start == 3:
        cl = Class()
    elif start == 4:
        sName = StudentName()
    elif start == 5:
        sSurname = StudentSurname()
    else:
        print("Ошибка!")
Main()