num = int(input("Dame un numero: "))

contador = 0

for divisor in range(1, num):
    if num % divisor == 0:
        contador +=1

if contador <= 2:
    print("El numero es primo")
else: 
    print("El numero no es primo")
    
        
     