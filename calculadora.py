from operaciones import *

if __name__ == "__main__":
  x = float(input("Ingrese un numero real:"))
  x_squared = elevar_al_cuadrado(x)
  print("El cuadrado de " + str(x) + " es " + str(x_squared))

  y = float(input("Ingrese un numero real:"))
  suma = sumar_dos_numeros(x,y)
  print("La suma de " + str(x) + " y " + str(y) + " es " + str(suma))