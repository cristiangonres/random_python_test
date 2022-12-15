from random import *


num_aleatorio = randint(50, 100)
num_aleatorio_decimal = uniform(50, 100)
num_aleatorio_entre_0_1 = random()

valores = ['azul', 'rojo', 'verde', 'amarillo', 'negro', 'naranja']

print(f'Mi color favorito es el {choice(valores)}')

numeros = list(range(5, 50, 5))
print(numeros)

shuffle(numeros)


print(f'Los numeros ahora están mezclados {numeros}')

print(num_aleatorio)
print(num_aleatorio_decimal)
print(num_aleatorio_entre_0_1)