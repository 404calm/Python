print ("Calculadora de IMC")
print ("Cuanto mides en metros?:")
altura = float(input())
print ("Cuanto pesas en kg?:")
peso = float(input())

imc = peso/altura **2

print (f"Tu IMC es: {imc:.2f}")