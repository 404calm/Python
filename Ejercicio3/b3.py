import math
import random

cantidad = int(input("Cuantos numeros aleatorios quieres generar junto con su raiz cuadrada?: "))
num = random.randint(1, 100)
contador = 0

for contador in range(0, cantidad):

    num = random.randint(1, 101)
    print(f"Raíz cuadrada de {num}: {math.sqrt(num):.2f}")