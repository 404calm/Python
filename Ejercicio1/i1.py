print ("Conversor de Temperatura")
print ("Dame una temperatura en Celsius?")
tempC = float(input())

tempF = tempC * 9/5 +32
tempK = tempC + 273.15

print ("La temperatura es:")
print(f"Celsius: {tempC:.1f}Cº")
print(f"Fahrenheit: {tempF:.1f}Fº")
print(f"Kelvin: {tempK:.1f}Kº")