import math

numeros = [1, 34, 56, 72, 85, 97, 1016, 1995, 543, 1, 0, 16, 22]

def estadisticas(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    media = sum(numeros)/len(numeros)
    
    return f"Min: {minimo} \nMax: {maximo} \nMedia:  {media}"

print(estadisticas(numeros))