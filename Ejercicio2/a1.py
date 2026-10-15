codigoHttp = int(input("¿Cual es el codigo http?: "))
match codigoHttp:
    case 200:
        print("Exito' (200)")
    case 301:
        print("Redireccion' (301)")
    case 404: 
        print("No encontrado' (404)")
    case 500: 
        print("Error del servidor' (500)")
    case _: 
        print("Desconocido' para cualquier otro")