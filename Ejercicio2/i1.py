nota = float(input("¿Que nota quieres clasificar?: "))

if nota <= 10 and nota >= 9:
    print("Tienes un sobresaliente.")
elif nota < 9 and nota >= 7:
    print("Tienes un notable.")
elif nota < 7 and nota >= 6:
    print("Tienes un bien.")
elif nota < 6 and nota >= 5:
    print("Tienes un suficiente.")
elif nota < 5 and nota >= 0:
    print("Tienes un suspenso.")
else: 
    print("La nota no se encuentra entr 0 y 10.")