print("=========BIENVENIDOS AL BOSQUE DEL ITA========")
print("para ingresar y adquerir tu entrada al bosque debes deirme tu edad")

edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("El costo de tu entrada es de $50.00 pesos ")
elif edad <=17:
    print("El costo de tu entrada es de $80.00 pesos ")
else:
    print("El costo de tu entrada es de $120.00 pesos ") 