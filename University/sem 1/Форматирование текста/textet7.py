# Операции над текстом
# Балашов Роман ИУ7-15Б

#input:  Текст задается в коде через массив строк

# (1) Выравнивание по ширине ^ +
# (2) Выравнивание по левому краю ^ +
# (3) Выравнивание по правому краю ^ +
# (4) Замена во всем тексте одного слова другим ^ +
# (5) Удаление заданного слова из текста ^ +
# (6) Замена арифм. выражений на их результат ^
# (7) Предложение с самым коротким словом ^ +

ariphSymbols = ["+", "-"]
splitSymbols = ["+", "-", ","]
splitSentence = [".",","]
num = ["1","2","3","4","5","6","7","8","9","0"]

def CheckIfNumber(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def Denormalize(text):
    for i in range(len(text)):
        splitMinus = text[i].split("-")
        text[i] = " - ".join(splitMinus)
        splitPlus = text[i].split("+")
        text[i] = " + ".join(splitPlus)
        splitDot = text[i].split(",")
        text[i] = " , ".join(splitDot)

def Normalize(text):
    for i in range(len(text)):
        splitMinus = text[i].split(" - ")
        text[i] = "-".join(splitMinus)
        splitPlus = text[i].split(" + ")
        text[i] = "+".join(splitPlus)
        splitDot = text[i].split(" , ")
        text[i] = ", ".join(splitDot)   

def ReplaceAriphmetics(text):
    Denormalize(text)

    textStrings = []   
    for i in range(len(text)):
        textStrings.append(text[i].split())

    for i in range(len(textStrings)):
        for l in range(1, len(textStrings[i])): 
            if textStrings[i][l] in ariphSymbols:
                if CheckIfNumber(textStrings[i][l-1]) and CheckIfNumber(textStrings[i][l+1]):
                    a = float(textStrings[i][l-1])
                    b = float(textStrings[i][l+1])
                    operation = textStrings[i][l]
                    if operation == "+":
                        c = a + b
                    if operation == "-":
                        c = a - b
                    
                    textStrings[i][l] = str(c)
                    textStrings[i][l+1] = ""
                    textStrings[i][l-1] = ""
       
        text[i] = " ".join(textStrings[i])
    Normalize(text)

def GetShortest(text):
    starterFlag = True
    wholePiece = "" # Используется для склейки всего текста в одну строку
    
    for l in range(len(text)):
        wholePiece += text[l] + " "
    textSplit = wholePiece.split(".") # Разбиение на отдельные предложения

    for f in range(len(textSplit)): # Поиск самого короткого слова во всех предложениях
        sentSplit = textSplit[f].split()
        if starterFlag:   
            shortest = len(sentSplit[0])
            shIndex = 0
            word = sentSplit[0]
            starterFlag = False

        for l in range(len(sentSplit)):
            if sentSplit[l].isalpha(): # Проверка на числа
                if len(sentSplit[l]) < shortest:
                    shortest = len(sentSplit[l])
                    word = sentSplit[l]
                    shIndex = f
        
        normalizierSplit = textSplit[shIndex].split()
        answerSentence = " "

        for l in range (len(normalizierSplit)):
            answerSentence += normalizierSplit[l] + " "
        answerSentence = answerSentence.rstrip()
    print("Самое короткое слово: ", word)
    print("Предложение с этим словом: ", answerSentence, ".\n", sep = "")

def DeleteWord(word, text):
    for l in range(len(text)):
        split = text[l].split()
    
        for f in split:
            if f.upper() == word.upper():
               text[l] = text[l].replace(f, "", 1)
            if f.upper() == word.upper() + ".":
                text[l] = text[l].replace(f, ".", 1)
                for i in range(len(text)):
                    splitDot = text[i].split(" . ")
                    text[i] = ". ".join(splitDot)
            if f.upper() == word.upper() + ",":
                text[l] = text[l].replace(f, "", 1)
        #print("changed line: ", text[l].strip(), sep = '')

def ReplaceWord(text):
    A = input("Введите слово: ")
    B = input("Введите замену: ")
        
    for i in range(len(text)):
        splitText = text[i].split()
        for k in splitText: # Для замены слов
            
            if k.upper() == A.upper():
                if k.istitle() and not B.isupper():
                    text[i] = text[i].replace(k, B.capitalize(), 1)
                else:
                    text[i] = text[i].replace(k, B, 1)   
            if k.upper() == A.upper() + ".":
                if k.istitle() and not B.isupper():
                    text[i] = text[i].replace(k, B.capitalize(), 1)
                else:
                    text[i] = text[i].replace(k, B + ".", 1)
            if k.upper() == A.upper() + ",":
                if k.istitle() and not B.isupper():
                    text[i] = text[i].replace(k, B.capitalize(), 1)
                else:
                    text[i] = text[i].replace(k, B + ",", 1)

def Format(side, text): # Выравнивание текста
    maxLen = 0
    splitText = []
    for i in text:
        splitText.append(i.split())
        if len(i) > maxLen:
            maxLen = len(i)

    if side == "left":
        for i in range(len(text)):
            text[i] = " ".join(splitText[i])

    if side == "right":
        for i in range(len(text)): 
            addedSpaces = maxLen - len(" ".join(splitText[i])) # Перед всем предложением
            if len(text[i]) != maxLen:
                text[i] = addedSpaces * " " + " ".join(splitText[i])
            else:
                text[i] = " ".join(splitText[i])

    if side == "width":
        for i in range(len(text)):
            
            difference = maxLen - len(" ".join(splitText[i]))
            wordCount = len(splitText[i])

            addedSpaces = int(difference / wordCount) + 1 # После каждого слова
            addedLeftoff = int(difference % wordCount) + addedSpaces - 1
            
            while addedLeftoff > wordCount and wordCount != 1:
                addedLeftoff -= (wordCount - 1)
                addedSpaces += 1
            if addedLeftoff == wordCount:
                addedLeftoff = 1
                addedSpaces += 1

            text[i] = ""

            for k in range(len(splitText[i])):
                if addedLeftoff > 0:
                    text[i] += splitText[i][k] + " " * addedSpaces + " "
                    addedLeftoff -= 1
                else:
                    text[i] += splitText[i][k] + " " * addedSpaces
            text[i] = text[i].rstrip()

def clearUp(text): # Убирает пустые строки из текста
    for i in range(len(text)-1, -1, -1):
        if text[i].strip() == "":
            text.pop(i)

def mainMenu(a, text):

    if a == '0':
        return a
    elif a == '1':
        Format("width", text)
    elif a == '2':
        Format("left", text)
    elif a == '3':
        Format("right", text)
    elif a == '4':
        ReplaceWord(text)
    elif a == '5':
        wordToDelete = input("Введите слово для удаления: ")
        DeleteWord(wordToDelete, text)
    elif a == '6':
        ReplaceAriphmetics(text)
    elif a == '7':
        GetShortest(text)
    else:
        print("Неверная команда..")
        return True

def printInfo():
    print("--------------------COMMANDS----------------------")
    print(
        " # (0) Выход\n"
        " # (1) Выравнивание по ширине\n",
        "# (2) Выравнивание по левому краю\n",
        "# (3) Выравнивание по правому краю\n",
        "# (4) Замена во всем тексте одного слова другим\n",
        "# (5) Удаление заданного слова из текста\n",
        "# (6) Замена арифм. выражений на их результат\n",
        "# (7) Предложение с самым коротким словом"
        )

    print("----------------------TEXT------------------------")
    for i in text:
        print(i)
    print("--------------------------------------------------")

text = [
    "Интеграл является одним из важнейших понятий математического анализа, которое",
    "возникает при решении многих задач. Упрощенно интеграл",
    "можно представить как аналог суммы для бесконечного числа",
    "бесконечно малых слагаемых. Существуют разные способы определения интеграла -",
    "различают интегралы Римана, Лебега, Стильтеса итд.",
    "ла ла лалала",
    "два два",
    "три три три",
    "четыре четыре четыре четыре",
    "Проверки на числа: 3 + 4.334, 8+3ю 17 + 2323, 6 - 2, 3 - 9, 323+32rr, 5-43, 65+22 123123 123."
    ]

a = 1
counter = 0 # Считает неверные вводы
while a != '0':
    clearUp(text)
    printInfo()
    a =input("Введите команду: ")
    if a in ['1','3']:
        Format("left",text)
    if mainMenu(a, text):
        counter += 1
    if counter > 5:
        print("Превышено максимальное количество неверных вводов...")
        break
print("Выход")