def calcular_media(notas):
    total = 0
    for nota in notas:
        total = total + nota
    media = total / len(notas)  # <- hay un error en esta linea
    return media

print(calcular_media([7, 8, 9, 6]))