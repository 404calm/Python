def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 120:
        raise ValueError("La edad no es realista")
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero")
    return True

edad = int(input("Introduce tu edad: "))

try:
    validar_edad(edad)
except ValueError as e:
    print(f"Error de valor: {e}")