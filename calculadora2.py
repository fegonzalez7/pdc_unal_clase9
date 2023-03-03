import operaciones

if __name__ == "__main__":
  x = float(input("Ingrese un numero real:"))
  xSquared = operaciones.elevarCuadrado(x)
  print("El cuadrado de " + str(x) + " es " + str(xSquared))

  y = float(input("Ingrese un numero real:"))
  suma = operaciones.sumarDosNumeros(x,y)
  print("La suma de " + str(x) + " y " + str(y) + " es " + str(suma))