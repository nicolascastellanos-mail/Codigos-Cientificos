# 6:16 p.m. en el 8 de agosto de 2022.
# Con el objetivo de realizar combinaciones recursivas sucesivas

def factorial(x):
	resultado = 0

	if x == 0 or x == 1:
		resultado = 1
	elif x < 0:
		return "Bad calculation"
	else:
		resultado = x * factorial(x - 1)

	return resultado

combinacion = lambda n, r: (factorial(n)) / (factorial(r) * factorial(n - r))

n = 13
resultado = 0

for r in range(1, n + 1):
	resultado += combinacion(n, r)

print(resultado)

# Terminado tal y como está a las 6:33 p.m.
