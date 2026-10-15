from datetime import date
print ("Calculadora de edad y en el año que viene")
print ("Como te llamas?")
nombre = input()
print ("Que dia naciste?")
diaNacimiento = input()
print("Que mes (numero) naciste?")
mesNacimiento = input()
print("En que año naciste?")
anoNacimiento = input()

edad = date.today().year - int(anoNacimiento)

if int(mesNacimiento) > date.today().month:
    edad -=1
if int(mesNacimiento) == date.today().month and int(diaNacimiento) < date.today().day:
    edad +=1
if int(mesNacimiento) == date.today().month and int(diaNacimiento) == date.today().day:
    edad +=1
    print("Felicidades, hoy es tu cumpleaños")

edadElProximoAno = edad +1
print("Hola " + nombre)
print("Tienes " + str(edad) + " años")
print("El año que viene en estas fechas tendras " + str(edadElProximoAno) + " años")