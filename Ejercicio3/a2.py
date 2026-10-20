def contar_llamadas(funcion):
    contador = 0

    def envoltura():
        nonlocal contador
        contador += 1
        resultado = funcion()
        print("Se ha llamado:", contador)
        return resultado

    return envoltura


@contar_llamadas
def preguntar():
    respuesta = input("¿Quieres seguir? (s/n): ").strip().lower()
    return respuesta == "s"


while preguntar():
    print("¡Seguimos!")

print("Fin del programa")