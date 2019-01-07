
import math as m

def reset():
    return [14,18,19,37,23,40,29,30,11]

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

A = [14,18,19,37,23,40,29,30,11]
print(A)
print("\n---------------BUBBLE---------------\n")
bubble_sort(A)
A = reset()
print("\n---------------INSERT---------------\n")
insert_sort(A)
A = reset()
print("\n---------------SHELL----------------\n")
shell(A)
A = reset()
print("\n---------------QUICK----------------\n")
print(quick_sort(A))
A = reset()
print("\n---------------CHOICES--------------\n")
choice_sort(A)