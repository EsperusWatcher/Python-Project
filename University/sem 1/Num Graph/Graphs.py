# Построение таблицы и графика функции
# Балашов Роман ИУ7-15Б

while True:
    
    x, xn, h = map(float, input("Введите начальный x, конечный и шаг: ").split())
    if (h == 0 or xn == x):
        print ("Из введенных данных невозможно построить график...")
        continue
    else:
        break

xCrossed = False

if (x > xn):
    x, xn = xn, x
    if (h < 0):
        h = -h

# Вывод заголовка для таблицы

print ('| {:^12} | {:^12} |'.format('x','y'))

temp = x

while (temp <= xn):
    y = 1.23 * pow(temp,5) - 2.52 * pow(temp, 4) - 16.1 * pow(temp, 3) + 173.3 * pow(temp, 2)
    print('| {:^12.5} | {:^12.5} |'.format(temp, y))
    temp += h

# Нахождение минимального и максимального значения функции

y_max = int(1.23 * pow(xn,5) - 2.52 * pow(xn,4) - 16.1 * pow(xn,3) + 173.3 * pow(xn,2))
y_min = int(1.23 * pow(x,5) - 2.52 * pow(x,4) - 16.1 * pow(x,3) + 173.3 * pow(x,2))
if (y_max < y_min):
    y_max, y_min = y_min, y_max
temp = x

# Нахождение точки пресечения графиком оси Ox

eps = 1e-7

while (temp <= xn):
    y_now = int(1.23 * pow(temp,5) - 2.52 * pow(temp,4) - 16.1 * pow(temp,3) + 173.3 * pow(temp,2))
    y_next = int(1.23 * pow(temp + h, 5) - 2.52 * pow(temp + h,4) - 16.1 * pow(temp + h, 3) + 173.3 * pow(temp + h, 2))

    if (y_now < y_min):
        y_min = y_now
    if (y_now > y_max):
        y_max = y_now
        
    if (y_now <= 0 and y_next >= 0) or (
        y_next <= 0 and y_now >= 0):
            Ox_pos = int(abs((y_now - y_min) / (y_max - y_min)) * 64)
            xCrossed = True
            if temp == 0:
                break
    temp += h


# Вывод заголовка для колонки значений x и промежутка (y_min, y_max)

print('\n| {:^12.5} | {:^10}'.format('x',y_min), 42 * " ", "{:^10}".format(y_max))

temp = x

while (temp <= xn):

    
    print('| {:^12.5} |'.format(temp),end='')

    y_now = int(1.23 * pow(temp,5) - 2.52 * pow(temp,4) - 16.1 * pow(temp,3) + 173.3 * pow(temp,2)) 
    X_pos = int(((y_now - y_min) / (y_max - y_min)) * 62) + 1   #Определение границ вывода

    
    # График пересекает ось Oy только тогда, когда x = 0
    if (temp < 0 and (temp + h) > 0) or temp == 0:
        print((X_pos - 1) * "-", "X", sep = '', end = '')
        print((63 - X_pos) * "-")
        temp += h
        continue

    # Вывод для случая когда ось пересекает Ox и нет
    
    if xCrossed:
        
        if (X_pos == Ox_pos):
            if (y_now > 0):
                X_pos += 1
            else:
                X_pos -= 1

        if (X_pos == 64):
            print((X_pos - 2) * " ", "o", sep = '')
            temp += h
            continue
            
        if (X_pos < Ox_pos):
            print((X_pos - 1) * " ", "o", (Ox_pos - X_pos - 1) * " ", "|", sep = '')
        else:
            print((Ox_pos - 1) * " ", "|", (X_pos - Ox_pos - 1) * " ", "o", sep = '')
    else:
        print((X_pos - 1) * " ", "o", sep = '')
 
    temp += h
