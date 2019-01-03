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

ariphSymbols = ["+", "-", "*", "/", "^"]
splitSymbols = ["+", "-", "*", "/", "^", ".", ","]
splitSentence = [".",","]
num = ["1","2","3","4","5","6","7","8","9","0"]

def CheckIfNumber(num): # Позволяет заменять выражения с действительными числами
    
    try:
        float(num)
        return True
    
    except ValueError:
        return False

def ReplaceAriphmetics(text):

    Denormalize(text)
   # print("\n\n-----------------DENORMALIZED------------\n\n")
   # for i in text:
   #     print(i)
   # print("\n\n\n\n-------------------------------\n\n\n\n")
    textStrings = []
    insertComasIndex = []
    
    for i in range(len(text)):
        textStrings.append(text[i].split())
    #print(textStrings)

    for i in range(len(textStrings)):

        for l in range(1, len(textStrings[i]) - 1): # Приводит выражения к формату a_b
            if textStrings[i][l] in ariphSymbols:
                #textStrings[i][l] = textStrings[i][l-1] + textStrings[i][l] + textStrings[i][l+1]
    
                if CheckIfNumber(textStrings[i][l-1]) and CheckIfNumber(textStrings[i][l+1]):
                    a = float(textStrings[i][l-1])
                    b = float(textStrings[i][l+1])
                    operation = textStrings[i][l]
                    if operation == "+":
                        c = a + b
                    if operation == "-":
                        c = a - b
                    if operation == "*":
                        c = a * b
                    if operation == "/":
                        c = a/b
                    if operation == "^":
                        c = pow(a,b)
                        
                    textStrings[i][l] = str(c)
                    textStrings[i][l+1] = ""
                    textStrings[i][l-1] = ""

     
                    
    for i in range(len(text)):
        text[i] = ""
        for k in range(len(textStrings[i])):
            text[i] += textStrings[i][k] + " "
    Normalize(text)

def GetShortest(text):
    
    starterFlag = True
    wholePiece = "" # Используется для склейки текста в одну строку
    
    for l in range(len(text)):
        wholePiece += text[l]
    textSplit = wholePiece.split(".") # Разбиение на отдельные предложения

    for f in range(len(textSplit)): # Поиск самого короткого слова во всех предложениях
        sentSplit = textSplit[f].split()
        if starterFlag:
            shortest = len(sentSplit[0])
            shIndex = 0
            starterFlag = False

        for l in range(len(sentSplit)):
            if sentSplit[l].isalpha(): # Проверка на числа
                if len(sentSplit[l]) < shortest:
                    shortest = len(sentSplit[l])
                    word = sentSplit[l]
                    shIndex = f
        
        normalizierSplit = textSplit[shIndex].split()
        answerSentence = ""

        for l in range (len(normalizierSplit)):
            answerSentence += normalizierSplit[l] + " "

    #print(normalizierSplit)
    print("Самое короткое слово: ", word)
    print("Предложение с этим словом: ", answerSentence, ".", sep = "")

def Denormalize(text):
 
    toInsert = []
  
    for i in range(len(text)):
        toInsert = []
       
        for k in range(len(text[i])):
            if text[i][k] in splitSymbols:
                toInsert.append(k)
                if text[i][k] == "." and (text[i][k-1] in num) and (text[i][k+1] in num):
                    toInsert.pop()

        counter = 0
       
        for k in range(len(toInsert)):
            a = toInsert[k]

            text[i] = text[i][:a+counter] + " " + text[i][a + counter] + " " + text[i][a+counter+1:]
            counter+=2

def Normalize(text):
    for i in range(len(text)):
        toPop = [] # Индексы символов разделения, вокруг которых нужно убрать пробелы
        onlyLeft = [] # Символы разделения в конце предложения(слова) должны оставлять пробел справа
        for k in range(len(text[i])):
            if text[i][k] in splitSentence:
                toPop.append(k)
                if text[i][k] == "." and (text[i][k-1] in num) and (text[i][k+1] in num):
                    toPop.pop()
                #elif text[i][k] == "." or text[i][k] == "," and text[i][k+1] == " " and text[i][k-1].isalpha():
                  #  toPop.pop()
                   # onlyLeft.append(k)

        for k in range(len(toPop) - 1, -1, -1):
            a = toPop[k]
            text[i] = text[i][:a-1] + text[i][a] + " " + text[i][a+2:]

        #for k in range(len(onlyLeft) - 1, -1, -1):
           # a = onlyLeft[k]
          #  text[i] = text[i][:a-1] +  text[i][a] + text[i][a+1:]

def DeleteWord(word, text):
    for l in range(len(text)):
        split = text[l].split()
    
        for f in split:
            if f.upper() == word.upper():
               text[l] = text[l].replace(f, "", 1)
            if f.upper() == word.upper() + ".":
                text[l] = text[l].replace(f, "", 1)
            if f.upper() == word.upper() + ",":
                text[l] = text[l].replace(f, ".", 1)
    
    return text

def Format(side, text): # Выравнивание текста по образу и подобию

    maxLen = len(text[0]) # Максимальная длина строки в тексте
    wordCount = [] # Массив из отдельных слов кждого предложения в тексте
    maxIndex = [0]
   
    for i in range(len(text)):
        wordCount.append(text[i].split())
        if len(text[i]) >= maxLen:
            maxLen = len(text[i])
            maxIndex = i

    if side == "width":
   
        for i in range(0, len(text)):
            text[i] = "" 
    
            for k in range(len(wordCount[i])):
                text[i] += wordCount[i][k] + " "

            counter = 1
   
            while(len(text[i]) != maxLen):
                k = text[i].index(wordCount[i][counter]) # Равномерная вставка пробелов после каждого слова до макс. длины
                text[i] = text[i][:k] + " " + text[i][k:]
                counter += 1
                if counter == len(wordCount[i]):
                    counter = 1

    if side == "left" or side == "right":
     
        for i in range(len(text)):
            text[i] = ""
     
            for k in range(len(wordCount[i])):
                text[i] += wordCount[i][k] + " "

    if side == "right":
    
        for i in range(0, len(text)):
            wholeSpace = int(abs(len(text[i]) - maxLen))
            text[i] = wholeSpace * " " + text[i]

def ReplaceWord(text):
    
    A, B = map(str, input("Введите слово и замену: ").split())
    
    for i in range(len(text)):
        splitText = text[i].split()
      
        for k in splitText: # Для замены слов
            if k.upper() == A.upper():
                text[i] = text[i].replace(k, B, 1)
            if k.upper() == A.upper() + ".":
                text[i] = text[i].replace(k, B + ".", 1)
            if k.upper() == A.upper() + ",":
                text[i] = text[i].replace(k, B + ",", 1)
                
def PrintText(text):
    
    for i in text:
            print(i)

def GetInput(a, text): # Считать команду для преобразования текста
    print()
    
    if a == 1:
        Format("width", text)
        PrintText(text)
    elif a==2:
        Format("left", text)
        PrintText(text)
    elif a==3:
        Format("right", text)
        PrintText(text)
    elif a==4:
        ReplaceWord(text)
        PrintText(text)
    elif a==5:
        wordToDelete = input("Введите слово для удаления: ")
        text = DeleteWord(wordToDelete, text)
        PrintText(text)
    elif a==6:
        ReplaceAriphmetics(text)
        PrintText(text)
    elif a==7:
        GetShortest(text)
        PrintText(text)
    elif a==8:
        Denormalize(text)
        PrintText(text)
    elif a==9:
        Normalize(text)
        PrintText(text)
    else:
        print("Неверная команда..")

text = [
    "Интеграл является одним из важнейших понятий математического анализа, которое",
    "возникает при решении многих задач. Упрощенно интеграл",
    "можно представить как аналог суммы для бесконечного числа",
    "бесконечно малых слагаемых. Существуют разные способы определения интеграла -",
    "различают интегралы Римана, Лебега, Стильтеса  итд.",
    "Проверки на числа: 3 + 4.334, 17 + 2323, 6 - 2, 3 - 9,  323 + - 32rr, -5+43, 65+22"
    ]

print("\n# (1) Выравнивание по ширине\n"
        "# (2) Выравнивание по левому краю\n"
        "# (3) Выравнивание по правому краю\n"
        "# (4) Замена во всем тексте одного слова другим\n"
        "# (5) Удаление заданного слова из текста\n"
        "# (6) Замена арифм. выражений на их результат\n"
        "# (7) Предложение с самым коротким словом\n"
        )
PrintText(text)
while True:
    
    choice = int(input("\nВыберите опцию: "))
    GetInput(choice, text)
    
