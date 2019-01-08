def right_triangles(a,b,n): # Метод правых прямоугольников
	h = (b-a)/n # Длина каждого из n отрезков
	summ = 0
	for k in range(1,n):
		summ += f(a + k * h)
	summ *= h
	return summ

def left_triangles(a,b,n): # Метод левых прямоугольников
	h = (b-a)/n
	summ = 0
	for k in range(0,n-1):
		summ += f(a + k * h)
	summ *= h
	return summ

def center_triangles(a,b,n): # Метод срединных прямоугольников
	h = (b-a)/n
	summ = 0
	for k in range(0, n-1):
		summ += f(a + (k + 0.5) * h)
	summ *= h
	return summ

def trapeze(a,b,n): # Метод трапеций
	h = (b - a)/n
	summ = 0
	for k in range(1,n):
		one = f(a + h * (k - 1))
		two = f(a + h * k)
		summ += (two + one) / 2 * h
	return summ

def parabola(a,b,n): # Метод парабол(Симпсона)
	h = (b-a)/n
	summ = f(a)
	check = True
	for k in range(0, n):
		if check:
			summ += f(a + k * h) * 4
		else:
			summ += f(a + k * h) * 2
		check = not check
	summ *= h / 3
	return summ

def three_eight(a,b,n): # Метод трех восьмых
	h = (b-a)/n/3
	m = 3 * n - 1
	summ = f(a) + f(b)
	for i in range(1, m):
		if i % 3 == 0:
			summ += 2 * f(a + h * i)
		else:
			summ += 3 * f(a + h * i)
	summ *= 3/8 * h
	return summ

def f(x): # Функция для интегрирования
	return 2 * x + 5

def F(x): # Первообразная функции для точного интеграла
	return x ** 2 + 5 * x + 28

def calculate(Func, n, n2, eps): # Функция рассчета для любого метода
	one = Func(a,b,n)
	two = Func(a,b,n2)
	count = 2

	while abs(one - two) > eps:
		one = Func(a,b,n * count)
		two = Func(a,b,n2 * count)
		count *= 2
	else:
		return two

n = 100; n2 = 200 # Количество участков разбиения
a = 0; b = 20  # Интервал рассчета
eps = 0.01 # Точность рассчета

print("Данная функция: y = 2x + 5")
print("Интервал рассчета: ", a, " -> ", b)
print("Выбранная точность: ", eps)
print("Точное значение интеграла: ", F(b) - F(a), "\n")
	
print("Метод правых прямоугольников: ", calculate(right_triangles, n, n2, eps))	
print("Метод левых прямоугольников: ", calculate(left_triangles, n, n2, eps))
print("Метод средних прямоугольников: ", calculate(center_triangles, n, n2, eps))
print("Метод трапеций: ", calculate(trapeze, n, n2, eps))
print("Метод парабол(Симпсона): ", calculate(parabola, n, n2, eps))
print("Метод 3/8: ", calculate(three_eight,n,n2,eps))

a = input()
