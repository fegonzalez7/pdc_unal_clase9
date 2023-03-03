from operaciones import *

if __name__ == "__main__":
  x = float(input("Ingrese un numero real:"))
  xSquared = elevarCuadrado(x)
  print("El cuadrado de " + str(x) + " es " + str(xSquared))

  y = float(input("Ingrese un numero real:"))
  suma = sumarDosNumeros(x,y)
  print("La suma de " + str(x) + " y " + str(y) + " es " + str(suma))