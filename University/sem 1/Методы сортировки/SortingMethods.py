import math as m

def reset():
    return [9,8,7,6,5,4,3,2,0]
# -------------------------------------------------------------------------
# Сортировка пузырьком
# В ходе нескольких проходов по массиву последовательно сравниваются пары элементов
# В случае когда порядок элементов нарушен, они меняются местами
# Иначе все остается как есть. В результате первого прохода в конце оказывается 
# Максимальный элемент, и так до тех пор, пока массив не будет отсортирован
def bubble_sort(array):
    for i in range(len(array),0,-1):
        for j in range(1, i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                print(array)
# -------------------------------------------------------------------------
# Сортировка шейкером (двусторонний пузырек)
def bubble_shaker_sort(array):
    leftMark = 1
    rightMark = len(array) - 1
    while leftMark <= rightMark:
        for i in range(rightMark, leftMark - 1, -1):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                print(array)
        leftMark += 1
        for i in range(leftMark, rightMark + 1):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                print(array)
        rightMark -= 1
# -------------------------------------------------------------------------
# Сортировка пузырьком с флагом
# Возможность выйти из цикла раньше, если полный проход будет без перестановок
def flagged_bubble_sort(array):
    toExit = False
    while not toExit:
        toExit = True
        for k in range(1, len(array)):
            if array[k] < array[k-1]:
                array[k], array[k-1] = array[k-1], array[k]
                print(array)
                toExit = False
# -------------------------------------------------------------------------
# Сортировка вставками
# Из массива последовательно берется каждый элемент и вставляется в соотв. место отсортированной части,
# начинающейся с первого элемента
def insert_sort(array):
    for i in range(len(array)):
        v = array[i]
        j = i
        while (array[j-1] > v) and (j > 0):
            array[j] = array[j-1]
            j = j - 1
        array[j] = v
        print(array)
# -------------------------------------------------------------------------
# Сортировка вставками + бинарный поиск
# Используется для ускорения нахождения позиции вставки сорт. элемента
# т.е. заменяется перебор элементов
def binary_search(array, key, low, high):
    if low == high:
        if array[low] > key:
            return low
        else:
            return low + 1
    if low > high:
        return low
    mid = (low + high) // 2
    if array[mid] < key:
        return binary_search(array, key, mid+1, high)
    elif array[mid] > key:
        return binary_search(array, key, low, mid-1)
    else:
        return mid

def insert_binary_sort(array):
    for i in range(len(array)):
        j = i - 1
        toInsert = binary_search(array,array[i], 0, j)
        while j >= toInsert:
            array[j+1], array[j] = array[j], array[j+1]
            j -= 1
        print(array)
# -------------------------------------------------------------------------
# Сортировка вставками с барьером
def insert_barrier_sort(initial):
    array = [0] + initial
    for i in range(2, len(array)):
        if array[i - 1] > array[i]:
            array[0] = array[i]
            j = i - 1
            while array[j] > array[0]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = array[0]
            print(array[1:])
    initial = array[1:]
    print(initial)
# -------------------------------------------------------------------------
# Сортировка Шелла
# Улучшенная версия сортировки вставками
# Перед применением оригиналього метода в данной последовательности с шагом gap
# Сортируются отдельные подгруппы элементов
def shell(array):
    gap = len(array) // 2
    while gap >= 1:
        i = gap
        while i < len(array):
            value = array[i]
            j = i
            while j - gap >= 0 and value < array[j - gap]:
                array[j] = array[j - gap]
                j -= gap
            array[j] = value
            i += 1
            print(array)
        gap //= 2
    print(array)
# -------------------------------------------------------------------------
# Быстрая сортировка
# Выбирается один из элементов массива
# Все остальные элементы сравниваются с ним и распределяются на:
# -o- меньшие слева, большие справа
# затем для каждой из групп применяется рекурсивный алгоритм,
# продолжающийся до тех пор, пока лина переданной последовательности не будет 1
def quick_sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        print(less + equal + greater)
        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return array
# -------------------------------------------------------------------------
# Сортировка выбором
# Находится номер минимального значения в последовательности
# Затем зачение переставляется на первую неотсортированную позицию
def choice_sort(array):
    lastSorted = 0
    while lastSorted < len(array):
        minimum = array[lastSorted]
        minPos = lastSorted
        for l in range(lastSorted, len(array)):
            if array[l] < minimum:
                minimum = array[l]
                minPos = l
        array[lastSorted], array[minPos] = array[minPos], array[lastSorted]
        print(array)
        lastSorted += 1
# -------------------------------------------------------------------------
A = [9,8,7,6,5,4,3,2,1]
print(A)
print("\n---------------BUBBLE---------------\n")
bubble_sort(A)
A = reset()
print("\n---------------SHAKER---------------\n")
bubble_shaker_sort(A)
A = reset()
print("\n---------------FLAGGED--------------\n")
flagged_bubble_sort(A)
A = reset()
print("\n---------------QUICK----------------\n")
print(quick_sort(A))
A = reset()
print("\n---------------CHOICES--------------\n")
choice_sort(A)
A = reset()
print("\n---------------INSERT---------------\n")
insert_sort(A)
A = reset()
print("\n--------------INSERTBIN-------------\n")
insert_binary_sort(A)
A = reset()
print("\n--------------INSERTBAR-------------\n")
insert_barrier_sort(A)
A = reset()
print("\n---------------SHELL----------------\n")
shell(A)
A = reset()

