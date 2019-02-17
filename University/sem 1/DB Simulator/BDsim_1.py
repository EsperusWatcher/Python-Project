# Работа с текстовыми файлами
# Балашов Роман ИУ7-15Б

# Требуется написать программу для работы с набором записей одинаковой 
# структуры, хранящимися в текстовом файле. Работу с программой реализовать 
# с помощью следующего меню: 
# 1) Выбор файла 
# 2) Создание нового набора записей 
# 3) Добавление записи 
# 4) Вывод всех записей из файла 
# 5) Поиск по одному полю 
# 6) Поиск по двум полям

# Программа создает в своей папке новые файлы по необходимости

import os
from pathlib import Path


def CreateNewFile(filePath):
	n = int(input("Введите желаемое количество столбцов: "))
	
	listToAdd = ""
	for i in range(n):
		a = input("Введите столбец {}: ".format(i+1))
		listToAdd += a + "|" # Разделитель для всех остальных операций над столбцами
	listToAdd = listToAdd[:len(listToAdd)-1]
	filePath += ".txt"
	file = open(filePath, 'w', encoding = 'utf-8')
	file.write(listToAdd)
	file.close()
	print("Файл успешно создан")

def ChooseFile(): # Выбрать или создать новый файл
	checkPath = input('\nВведите имя файла или путь до него: ').strip()
	if os.path.isfile(checkPath):
	    print('Файл выбран')
	    return checkPath
	print("Ошибка, файл не выбран")

def AddNewNote(file):

	Titles = list(file.readline().rstrip())
	Titles = ''.join(Titles) # Приводят приглашение ко вводу в порядок
	Titles = Titles.split("|")

	addToFile = "\n"
	for i in Titles:
		a = input("Введите значение для поля {:^5}: ".format(i))
		addToFile += a + "|"
	addToFile = addToFile[:len(addToFile)-1]
	file.write(addToFile)
	print()

def PrintEverything(file):
	Lines = [line for line in file]
	print()
	for i in Lines:
		i = i[0:len(i)-1]
		print (i)
	print()

def MakeFilesBeautiful(file): # Выравнивание всех столбцов в файле на одну ширину
	Lines = [line.strip() for line in file]
	maxSize = 0 # Размер максимальной длины слова для выравнивания
	for i in Lines:
		Note = i.split("|")
		for k in range(len(Note)):
			if len(Note[k]) > maxSize:
				maxSize = len(Note[k])

	newLines = []
	for i in range(len(Lines)):
		newLines.append([])
		for k in Lines[i].split("|"):
			k = k.strip()
			addedSpaces = " "*int((maxSize-len(k))/2)
			if int(maxSize-len(k)) % 2 == 0:	
				newLines[i].append((addedSpaces + k + addedSpaces + "|"))
			else:
				newLines[i].append((addedSpaces + k + addedSpaces + " |"))

	returnString = ""
	notTitle = False
	for i in newLines:
		if notTitle:
			returnString += "\n"
		notTitle = True
		for k in i:
			returnString += k
		a = len(returnString)
		returnString = returnString[:a-1]
	
	print(returnString)
	return returnString

def ChangeFile(file, newLines):
	file.write(newLines)

def FindByField(num, file):
	Titles = list(file.readline().rstrip())
	for i in range(len(Titles)):
		Titles[i] = Titles[i].strip(' ')
	Titles = ''.join(Titles) # Приводят приглашение ко вводу в порядок
	Titles = Titles.split("|")



	Lines = [line.strip() for line in file]

	for i in range(len(Lines)):
		Lines[i] = Lines[i].strip(' ')

	for i in range(len(Lines)):
		Lines[i] = Lines[i].split("|")
		for k in range(len(Lines[i])):
			Lines[i][k] = Lines[i][k].strip()

	print(Titles)
	for i in Lines:
		print(i)
	
	print("Доступные поля: ", ' '.join(Titles))

	if num == 1:
		keyfield = input("Введите поле для поиска: ") 
		keyword = input("Введите слово для поиска: ")
		idPos = Titles.index(keyfield)

		for i in range(len(Lines)):
			if Lines[i][idPos] == keyword:
				print(Lines[i])
		
	elif num == 2:
		keyfieldOne = input("Введите первое поле для поиска: ")
		keywordOne = input("Введите ключевое слово для поиска: ")
		keyfieldTwo = input("Введите второе поле для поиска: ")
		keywordTwo = input("Введите ключевое слово для поиска: ")

		idPosOne = Titles.index(keyfieldOne)
		idPosTwo = Titles.index(keyfieldTwo)

		for i in range(len(Lines)):
			if Lines[i][idPosOne] == keywordOne and Lines[i][idPosTwo] == keywordTwo:
				print(Lines[i])

filePath = "Help.txt" # По умолчанию поле пустое

while True:
	
	print("----------------------COMMANDS------------------------\n")
	print(
	" #  1) Выбор файла\n ",
	"#  2) Создание нового набора записей\n ",
	"#  3) Добавление записи\n ",
	"#  4) Вывод всех записей из файла\n ",
	"#  5) Поиск по одному полю\n ",
	"#  6) Поиск по двум полям\n", sep = ""
		)
	print("-------------------------------------------------------")
	print("\nВ данный момент выбран файл: ", filePath)
	
	a = int(input("Введите команду: "))

	if a == 1:
		filePath = ChooseFile() # Выбранный файл становится активным
	elif a == 2:
		filePath = input("Введите название файла без расширения: ")
		CreateNewFile(filePath)
		filePath += ".txt"
	elif filePath == "" or filePath == None:
		print("Для начала необхдимо выбрать файл")
		continue
	elif a == 3:
		file = open(filePath, 'r+', encoding = 'utf-8') # Открытие файла на дозапись значений (без удаления данных)
		AddNewNote(file)
		file.close()
		file = open(filePath, 'r+', encoding = 'utf-8')
		changedFileLines = MakeFilesBeautiful(file)
		file.close()
		file = open(filePath, 'w', encoding = 'utf-8')
		ChangeFile(file, changedFileLines)
		file.close()
	elif a == 4:
		file = open(filePath, 'r', encoding = 'utf-8') # Только для считывания значений
		PrintEverything(file)
		file.close()
	elif a == 5:
		file = open(filePath, 'r', encoding = 'utf-8') # Только для считывания значений
		FindByField(1, file)
		file.close()
	elif a == 6:
		file = open(filePath, 'r', encoding = 'utf-8') # Только для считывания значений
		FindByField(2, file)
		file.close()
	else:
		print("Неверная команда...")