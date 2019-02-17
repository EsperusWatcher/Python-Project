# Вычисление суммы бесконечного ряда с точностью eps
# Балашов Роман ИУ7-15Б

while True:
    x, eps = map(float, input("Введите x (-1,1) и eps: ").split())
    h, it_max = map(int, input("Введите шаг вывода и макс. количество итераций: ").split())
                    
    if (h == 0) or not (-1 < x < 1):
        print("Введенные данные неверны..")
        continue
    else:
        break
print("| {:^20} | {:^20} | {:^25} |".format("№ Итерации", "Текущий член", "Текущее значение суммы"))

# Задаем стартовые значения
summ = x
curr = x
n = 1
i = 0
h_counter = h

print("| {:^20} | {:^20.5} | {:^25.5} |".format(i+1, curr, summ * 2))

# Подсчет суммы и вывод таблицы

while (abs(curr) > eps):

    i += 1
    n += 2
    curr = (x ** n)/n
    summ += curr
    
    if (i == h_counter):    
        print("| {:^20} | {:^20.5} | {:^25.5} |".format(i+1, curr, summ * 2))
        h_counter += h

    if (i > it_max):
          print("Превышено максимальное количество итераций")
          break

print("Итоговое количество итераций: ", i+1)
print("Итоговое значение суммы: {:.5}".format(summ * 2))
