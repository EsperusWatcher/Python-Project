from tkinter import *
from matplotlib import *
import math
import tkinter.messagebox
import matplotlib.pyplot as plt

def f(x):
	#return math.cos(x) 
	return 3*(x**2 - 4*x + 3)**2 - 2

def f_prime(x): # производная
	#return -math.sin(x)
	return (2*x - 4) * 6 * (x**2 - 4*x + 3)

def drawGraph(x_points, y_points, roots, extrem): # Построение графика
	plt.plot(x_points, y_points, color="black") # график функции 
	plt.plot(roots, [0 for i in roots], 'ro') # Корни на графике
	plt.plot(extrem, [f(i) for i in extrem], 'co') # точки экстремума
	plt.axis([x_points[0], 
			x_points[len(x_points) - 1], 
			x_points[0], x_points[len(x_points) - 1]]) # шаг сетки
	plt.legend(('f(x)', 'Корни', 'Экстремумы'), loc=(0.01, 0.48)) # легенда

	plt.grid(True)
	plt.show()

def buildGraph(en_a, en_b, en_h, en_eps, en_maxIt):
	a = en_a.get()
	b = en_b.get()
	h = en_h.get()
	eps = en_eps.get()
	maxIt = en_maxIt.get()

	if not transferEntries(a, b, h, eps, maxIt): # проверка перевода строк в числа
		tkinter.messagebox.showerror("Ошибка", "Введены недопустимые символы!")
		return
		
	a = float(a)
	b = float(b)
	h = float(h)
	eps = float(eps)
	maxIt = abs(int(maxIt))

	table = Toplevel(root) # Внешнее окно для построения таблицы

	# Заголовок для таблицы и легенда ошибок
	Label(table, text="#").grid(row=0, column=0, padx=5, pady=5)
	Label(table, text="(a, b)").grid(row=0, column=1, padx=5, pady=5)
	Label(table, text="x").grid(row=0, column=2, padx=5, pady=5)
	Label(table, text="f(x)").grid(row=0, column=3, padx=5, pady=5)
	Label(table, text="Итерация").grid(row=0, column=4, padx=5, pady=5)
	Label(table, text="Ошибка").grid(row=0, column=5, padx=5, pady=5)
	Label(table, text="", width = 10).grid(row=0, column=6, padx=5, pady=5)
	Label(table, text="Код ошибки: ").grid(row=0, column=6, padx=5, pady=5)
	Label(table, text="0 - Все в порядке ").grid(row=1, column=6, padx=5, pady=5, sticky=W)
	Label(table, 
		text="1 - На всем промежутке не найдено корней").grid(row=2,
															  column=6,
															  padx=5,
															  pady=5,
															  sticky=W)
	Label(table, text="2 - Превышен лимит итераций").grid(row=3, column=6, padx=5, pady=5, sticky=W)

	yCoords = [] # Массивы для координат точек
	xCoords = []
	rootCoords = []
	extrem = []

	constructGraph(a, b, xCoords, yCoords, extrem, 0.001) # Заполнение массивов координатами

	counter_it = 0 # счетчики
	counter = 1
	root_found = 0
	mover = a

	while mover < b: # Переменная для перемещения по элем. отрезкам
		error_code = 0
		counter_it += 1

		if ((f(mover) < 0 and f(mover+h) >= 0) or (f(mover) >= 0 and f(mover+h) < 0)):
			f_root = steffensen(mover, mover+h, eps)
			addRow(table, mover, mover+h, counter_it,
			error_code, counter, f_root, f(f_root)) # Добавление строки в таблицу
			print(f_root)
			rootCoords.append(f_root)
			root_found = 1
			counter += 1
		
		if counter_it >= maxIt:
			break
		
		mover += h

	if root_found == 0 and counter_it < maxIt: # Если возникла ошибка
		error_code = 1
		addRow(table, a, b, maxIt, error_code, counter) # Если на всем промежутке не найдено ни одного корня
	elif counter_it >= maxIt:
		error_code = 2
		addRow(table, mover, mover+h, maxIt, error_code, counter) # Если один из корней был найден, но превышено кол-во итераций
	else:
		button_drawGraph = Button(table, text="Показать график",
										command=lambda: drawGraph(xCoords, yCoords, rootCoords, extrem))
		button_drawGraph.grid(row=counter+4, column=6, padx=5, pady=5, sticky=E)

def constructGraph(a, b, xCoords, yCoords, extrem, h):
	mover = a
	while mover < b: # Переменная для перемещения по элем. отрезка

		xCoords.append(mover) # Массив x для значений на графике
		yCoords.append(f(mover)) # Массив y для значений на графике
		
		if ((f_prime(mover) < 0 and f_prime(mover+h) > 0) or (f_prime(mover) > 0 and f_prime(mover+h) < 0)): # проверка экстремумов
			extrem.append(mover)	
		
		mover += h

def addRow(table, a, b, Iter, error_code, counter,  root = "-", froot = "-"): # Добавление новой строки в таблицу
	Label(table, text=str(counter)).grid(row=counter, column=0, padx=5, pady=5)
	Label(table, text=" ({:.3}, {:.3}) ".format(a, b)).grid(row=counter, column=1, padx=5, pady=5)
	Label(table, text=" {:.3} ".format(root)).grid(row=counter, column=2, padx=5, pady=5)
	Label(table, text=" {:.1} ".format(froot)).grid(row=counter, column=3, padx=5, pady=5)
	Label(table, text=" {} ".format(Iter)).grid(row=counter, column=4, padx=5, pady=5)
	Label(table, text=" {} ".format(error_code)).grid(row=counter, column=5, padx=5, pady=5)

def transferEntries(a, b, h, eps, maxIt): # Проверка значений в полях ввода на тип данных
	try:
		float(a)
		float(b)
		float(h)
		float(eps)
		int(maxIt)
	except ValueError:
		return False
	else:
		return True

def steffensen(start, end, eps, maxiter=10000): # Метод Стеффенсона
	x = (start + end) / 2.0
	a = 2 * eps / (f(x - eps) - f(x + eps))

	x1 = x + 8.0 * eps
	x0 = x + 4.0 * eps

	k = 0

	while k <= maxiter and abs( x - x0 ) >= eps:
	    x2, x1, x0 = ( x1, x0, x )
	    p1 = x  + a * f( x )
	    p2 = p1 + a * f( p1 )
	    x = x - ( ( p1 - x )**2 ) / ( p2 - 2 * p1 + x )
	    k = k + 1
	return x

root = Tk()

entry_a = Entry(root, width=10) # Ввод данных
entry_a.insert(0, -3)
entry_b = Entry(root, width=10)
entry_b.insert(0, 5)
entry_h = Entry(root, width=10)
entry_h.insert(0, 0.01)
entry_eps = Entry(root, width=10)
entry_eps.insert(0, 0.001)
entry_maxIt = Entry(root, width=10)
entry_maxIt.insert(0, 1000)

Label(root, text="a: ").grid(row=0, column=0, padx=5, pady=5, sticky=W) 
Label(root, text="b: ").grid(row=0, column=2, padx=5, pady=5, sticky=W)
Label(root, text="h: ").grid(row=0, column=4, padx=5, pady=5, sticky=W)
Label(root, text="eps: ").grid(row=1, column=0, padx=5, pady=5, sticky=W)
Label(root, text="Iter: ").grid(row=1, column=2, padx=5, pady=5, sticky=W)

entry_a.grid(row=0, column=1, padx=5, pady=5, sticky=W)
entry_b.grid(row=0, column=3, padx=5, pady=5, sticky=W)
entry_h.grid(row=0, column=5, padx=5, pady=5, sticky=W)
entry_eps.grid(row=1, column=1, padx=5, pady=5, sticky=W)
entry_maxIt.grid(row=1, column=3, padx=5, pady=5, sticky=W)

button_buildGraph = Button(root, text="Построить", width=8,
							 command=lambda: buildGraph(entry_a, entry_b, entry_h, entry_eps, entry_maxIt)) 
button_buildGraph.grid(row=1, column=5, pady=5, padx=5)

root.mainloop()