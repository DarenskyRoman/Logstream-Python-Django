try:
	a = float(input("a: ")) #Произвольное число
	borderline = float(input("borderline: ")) #Пограничное число

except ValueError:
	print('Введено нечисловое значение.')

try:
	if (a > borderline * 3):
		print("1-ое число больше пограничного более, чем в 3 раза.")
	elif (a > borderline):
		print("1-ое число больше пограничного.")
	elif (a < borderline):
		print("1-ое число меньше пограничного.")
	else:
		print("Числа равны.")
		
except NameError:
	print('Переменные не были определены.')
