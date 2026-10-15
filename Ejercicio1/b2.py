print("Calculadora de Area y permitero de un cuadrado o rectangulo")
print("Cual es la medida cm/m/km?")
medida = input()
print ("Cual es la base?")
base = int(input())
print("Cual es la altura?")
altura = int(input())

area = base * altura
perimetro = 2*(base +altura)
info = "Area: " + str(area) + medida + "2" + "\nPermitero: " + str(perimetro) + medida
if base == altura:
    print("Es un cuadrado")
else: 
    print("Es un rectangulo")
print(info)

