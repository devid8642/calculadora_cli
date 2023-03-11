from typer import Typer
from rich import print

app = Typer()

@app.command()
def add(numeros: list[int]) -> None:
	"""
		Este comando recebe como parâmetros números inteiros 
		(no formato x1 x2 x3 x4...) e retorna a soma deles.
	"""
	soma = 0

	for n in numeros:
		soma += n

	print(f'A soma vale: {soma}')

@app.command()
def addF(numeros: list[float]) -> None:
	"""
		Este comando recebe como parâmetros números reais 
		(no formato x1 x2 x3 x4...) e retorna a soma deles.
	"""
	soma = 0

	for n in numeros:
		soma += n

	print(f'A soma vale: {soma}')

@app.command()
def even(numeros: list[int]) -> None:
	"""
		Este comando recebe como parâmetros números inteiros
		(no formato x1 x2 x3 x4...) e retorna a soma de todos
		os pares.
	"""

	soma = 0

	for n in numeros:
		if (n % 2 == 0):
			soma += n

	print(f'A soma dos pares vale: {soma}')

@app.command()
def odd(numeros: list[int]) -> None:
	"""
		Este comando recebe como parâmetros números inteiros
		(no formato x1 x2 x3 x4...) e retorna a soma de todos
		os ímpares.
	"""

	soma = 0

	for n in numeros:
		if (n % 2 != 0):
			soma += n

	print(f'A soma dos ímpares vale: {soma}')

app()
