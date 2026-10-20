try:
    numero = int(input("Introduce un número: "))
    print(f"Has introducido el número {numero}")
except ValueError:
    print("Error: lo que has escrito no es un número válido.")