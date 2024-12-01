import operaciones

if __name__ == "__main__":
  x = float(input("Ingrese un numero real:"))
  x_squared = operaciones.elevaral_cuadrado(x)
  print("El cuadrado de " + str(x) + " es " + str(x_squared))

  y = float(input("Ingrese un numero real:"))
  suma = operaciones.sumar_dos_numeros(x,y)
  print("La suma de " + str(x) + " y " + str(y) + " es " + str(suma))