while True:
    try:
        numero = int(input("Introduce un número entero: "))
        break
    except ValueError:
        print("Error: debes escribir un número entero. Inténtalo de nuevo.")

print(f"Has introducido el número {numero}")