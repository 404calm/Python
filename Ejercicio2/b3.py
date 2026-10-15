contrasena = str(input("Introduce la contraseña: "))

while contrasena != str("python123"):
    print("La contraseña es incorrecta")
    contrasena = str(input("Introduce la contraseña: "))
    
print("La contraseña es correcta")