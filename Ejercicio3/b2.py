def saludar(nombre, saludo="Hola"):
    print(f"¡{saludo} {nombre}!")

nombre = str(input("Como te llamas? "))

saludar(nombre)
saludar(nombre, saludo = "Hasta luego")