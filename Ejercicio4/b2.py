def operacion_completa(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("ERROR: División por cero")
        resultado = None
    except TypeError:
        print("ERROR: Tipos de datos incorrectos")
        resultado = None
    else:
        print(f"Operación exitosa: resultado = {resultado}")
    finally:
        print("Operación finalizada")
    return resultado

a = int(input("Introduce un número: "))
b = int(input("Introduce un número: "))

operacion_completa(a,b)