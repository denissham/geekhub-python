# Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
# -  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), 
# 	пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
# -  Повиннi опрацювати такi умови:
# -  x > y;       вiдповiдь - х бiльше нiж у на z
# -  x < y;       вiдповiдь - у бiльше нiж х на z
# -  x == y.      вiдповiдь - х дорiвнює z

def numbers(x,y):
	if x > y:
		z = x - y
		print(x, " бiльше нiж " , y, "на", z)
	elif x < y:
		z = y - x
		print(y, " бiльше нiж " , x, "на", z)
	else:
		print(x, "дорівнює ", y)

x = int(input("Введіть x: "))
y = int(input("Введіть y: "))

numbers(x, y)
