import math as m

# Методы для нахождения корней уравнения с точностью eps на заданном промежутке

def f(x):
	return x ** 3 + x - 2

def f_prime(x):
	return 3 * x ** 2 + 1
# ------------------------------------------------------
# Метод Ньютона(касательных)
# Для получения сжимающего отображения применяется метод простых итераций
# Затем для приближенных рассчетов используется производная данной функции
def newtone(a,b,eps):
	c = a
	result = c
	x = c - f(c) / f_prime(c)
	while abs(result - x) > eps:
		result = x
		x = x - f(x) / f_prime(x)
	return x
# ------------------------------------------------------
# Упрощенный метод Ньютона
# Производная вычисляется только для первого элемента x0
def easy_newtone(a,b,eps):
	c = (a + b) / 2
	result = c
	x = c - f(c) / f_prime(c) # x0
	prime = f_prime(x)
	while abs(result - x) > eps:
		result = x
		x = x - f(x) / prime
	return x
# ------------------------------------------------------
# Метод Стеффенсена
def steffensen(a,b,eps):
	c = (a + b) / 2
	result = c
	x = c - f(c) / (f(c + f(c)) / f(c) - 1)
	while abs(result - x) > eps:
		result = x
		x = x - f(x) / (f(x + f(x)) / f(x) - 1)
	return x
# ------------------------------------------------------
# Метод секущих
def sek(a,b,eps):
	c0 = a
	c = (a+b)/2
	result = c
	x0 = c 
	x0 = c - (c - c0) / (f(c) - f(c0)) * f(c)
	x = x0 - ((x0 - c) / (f(x0) - f(c))) * f(x0)

	while abs(result - x) > eps:
		result = x
		x = x - ((x - x0) / (f(x) - f(x0))) * f(x)
		x0 = result
	return x
# ------------------------------------------------------
# Комбинированный метод
def f_pp(x): # сторая производная от функции
	return 6 * x

def combo(a,b,eps):
	while abs(a-b)>2 * eps:
		if f(a) * f_pp(a) < 0:
			a = a - f(a) * (a-b) / (f(a) - f(b))
		elif f(a) * f_pp(a) > 0:
			a = a - f(a)/f_prime(a)
		if f(b) * f_pp(b) < 0:
			b = b - f(b) * (b-a) / (f(b) - f(a))
		elif f(b) * f_pp(b) > 0:
			b = b - f(b)/f_prime(b)
	x = (a + b) / 2
	return x
# ------------------------------------------------------
# Метод дихотомии(бисекции)
# Рассматриваемый интервал должен пересеекать 0
# Вычисляется средняя позиция в интервале и значение ф-ции в ней
# Если значение удовлетворяет условию |f(mid)| < eps, то return
# Иначе вычисляется знак f(mid) и передается в рекурсию так, чтобы в новой последовательности
# Было пересечение с 0
def dihotomy(a,b,eps):
	c = (a + b) / 2
	if abs(f(c)) < eps:
		return c
	if f(c) * f(a) < 0:
		return dihotomy(a,c,eps)
	else:
		return dihotomy(c,b,eps)
# ------------------------------------------------------
# Метод Хорд
# Начальная хорда проходит через точки
# С(a,f(a)) : D(b,f(b))
def chord(a, b, eps):
	xn = (a * f(b) - b * f(a)) / (f(b) - f(a)) # Уравнение хорды через 2 точки в точке пересечения с осью
	if abs(f(xn)) < eps:
		return xn
	if f(a) * f(xn) < 0:
		return chord(a,xn,eps)
	else:
		return chord(xn,a,eps)
# ------------------------------------------------------
# Метод Итераций
# !!! требуется подобрать сходящуюся эквивалентную функцию, выраженную через х
# x = f(x)
# Затем значение постепенно уточняется, приближаясь к нужному корню
def iterations(a,b, eps):
	result = a # В качестве начальных данных берется значение ф-ции в начале интервала
	x = 2 / (a ** 2 + 1)
	while abs(result - x) > eps:
		result = x
		x = 2 / (x ** 2 + 1)
	return x
# ------------------------------------------------------
a = -10 # Начало и конец интервала уточнения
b = 10
eps = 0.0001
print("Уравнение: y = x^3 + x - 2")
print("Рассматриваемый интервал: [{},{}]".format(a,b) )
print("Выбранная точность: ", eps)
print()
print("Метод дихотомии: ", dihotomy(a,b,eps))
print("Метод хорд: ", chord(a,b,eps))
print("Метод Ньютона: ", newtone(a, b, eps))
print("Упрощенный метод Ньютона: ", easy_newtone(a, b, eps))
print("Метод Стеффенсена: ", steffensen(a, b, eps))
print("Метод секущих: ", sek(a, b, eps))
print("Комбинированный метод: ", combo(a, b, eps))
print("Метод итераций: ", iterations(a, b, eps))



a = input()