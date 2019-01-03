def Roulette(n, k, i):
    if k == 1 and n != 1:
        return 2
    people = [l+1 for l in range(n)] # Массив, симулирующий пронумерованных людей

    position = i # Стартовое значение для позиции
    counter = 1

    while people.count(0) != len(people)-1:
        position += 1
        counter += 1

        if position > len(people)-1: # Если счетчик позиции выходит за пределы массива, перемещаем его в начало
            position = 0 
        
        if people[position] == 0: # Игнорируем "мертвых"
            counter -= 1
            continue
            
        if counter == k:
            print(people)
            print("{} is killed".format(people[position]))
            people[position] = 0 # Мертвые люди помечаются как 0 и далее игнорируются
            counter = 0

    else:
        if 1 in people: # Если в живых остался человек с номером 1, то возвращаем стартовую позицию
            return i+1
        else:
            f = i+1
            if f > len(people)-1: # Если начало позиции уходит за границы массива, перемещаем его на 1 элемент
                f = 0
            print()
            return Roulette(n, k, f) # Рекурсия функции с увеличенной стартовой позицией


n, k = map(int, input("Количество и счет: ").split()) # Начальный ввод для входа в основной цикл

while n != 0 and k != 0:
    
    print(Roulette(n, k, 0))
    
    n, k = map(int, input("Количество и счет: ").split())