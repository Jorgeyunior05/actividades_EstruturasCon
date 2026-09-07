longitud1= float(input ("Ingrese lonjitud 1: "))
longitud2= float(input("Ingrese longitud 2: "))
longitud3= float(input("Ingrese logitud 3: "))

if longitud1 == longitud2 == longitud3:
  print("El triangulo es: equilatero")

elif longitud1 == longitud2 or longitud1 == longitud3 or longitud2 == longitud3:
  print("El triangulo es: Isoceles")
else:
  print("El triangulo es: Escaleno")