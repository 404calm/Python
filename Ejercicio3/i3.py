import random

def generar_contrasenha():
   return "" .join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))

    
print(generar_contrasenha())
    