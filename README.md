# Programación de Computadores - UNAL

## Tabla de Contenidos
- [Funciones 1](#funciones-1)
- [Utilidad de las funciones](#utilidad-de-las-funciones)
- [Funciones en Python](#funciones-en-python)
- [La función main](#la-función-main)
- [Scope o alcance](#scope-o-alcance)
- [Import](#import)
- [Reto 6](#reto-6)

## Funciones 1

En programación, así como en matemáticas, para las funciones definidas como:

$$f : A \rightarrow B$$ 

Al conjunto A se le denomina dominio y al conjunto B como rango. En programación el conjunto A corresponde al tipo de los argumentos de dicha función y el conjunto B que es el rango corresponderá al valor de retorno de dicha función.

### Utilidad de las funciones
+ Encapsular secuencias de código, *traducción:* reutilizar instrucciones que se repiten.
+ Separar y organizar procesos de manera eficiente, *traducción:* Divide y vencerás.
+ Mejorar la abstracción de un proceso.

### Funciones en Python 
Para declarar una función se utiliza la palabra reservada `def` seguida del nombre de la función, el cual debe ser un identificador válido (revisar [clase 6](https://github.com/fegonzalez7/pdc_unal_clase6)), en paréntesis se listan los argumentos y se sigue con `:`, se indentan las instrucciones y si la función retorna algo se usa la palabra reservada `return`.

```python
def nombre_de_la_funcion(arg1, arg2, ... , argn):
  <instrucciones de la función>
  return <datos que retorna la función>
```
**Ejemplo:** Escribir una función que reciba un real y retorne su cuadrado.
$$f: R \rightarrow R$$
$$f(x) \rightarrow x^2$$

```python
def elevar_al_cuadrado(x:float):
  return x**2
```
El flujo normal de un progama **secuencial** en python luce de esta manera:
```python
<importar librerias>
<declarar constantes>
<funciones>
<funcion_main> # Función principal
<declarar variables>
<ejectar procesos> # Implica llamar a las funciones declaradas
```
### La función main
Es la función principal de cualquier programa escrito en Python que se quiera ejecutar como script, es el denomiando *entry point*. La sintaxis es:

```python
if __name__ == "__main__":
  # codigo aqui
```

Si bien se pueden ejecutar programas sin necesidad de definir la función *main*, no es una buena práctica.

**Pro tip:** En C o C++ el equivalente era declarar:
```C
int main(void){
  // codigo aqui
}
```

**Ejemplo:** Escribir un programa que ingrese un flotante por teclado y usando una funcion retorne el cuadrado del número.

```python
def elevar_al_cuadrado(x:float) -> float:
  return x**2

if __name__ == "__main__":
  x = float(input("Ingrese un numero real:"))
  x_squared = elevar_al_cuadrado(x)
  print("El cuadrado de " + str(x)+ "es " + str(x_squared))
```

**Ejemplo:** Escribir un programa que ingrese la base y la altura de un rectángulo y usando una función retorne su área.

En este caso la función debe recibir dos parámetros y retorna uno.
```python
def calcular_area_rectangulo(base:float, altura:float) -> float:
  area_rectangulo = base*altura
  return area_rectangulo

if __name__ == "__main__":
  base = float(input("Ingrese base del rectangulo:"))
  altura = float(input("Ingrese altura del rectangulo:"))
  area = calcular_area_rectangulo(base, altura)
  print("El area del rectagulo es " + str(area))
```

**Ejecicio:** Realice un programa que ingrese dos masas y la distancia que las separa y calcule la fuerza de gravedad entre ellas. Resuelva usando una función.

$$\text{Ley de la gravitación universal:} \ F=G\frac{m_1 \cdot m_2}{r^2}$$

```python
G : float = 6.67384e-11 # Constante de Cavendish [Nm^2/kg^2]
``` 

### Scope o alcance

**Alcance Local:** Es la posibilidad de modificar una variable unicamente en la función donde es declarada.

**Alcance global:** Es la posiblidad de modificar una variable en cualquier función del programa. Se utiliza la palabra reservada *global* para dar el alcance general.

**Pro tip:** Utilizar variables globales **NO** es una buena práctica, ya que compromete la integridad de la información.

Variable local en la función *saludar*.
```python
def saludar():
  mensaje = "Hola local"
  print("Variable local", mensaje)

if __name__ == "__main__":
  saludar()
  # print("Variable global", mensaje) Quitar comentario y probar
```

Variable global que se utiliza en la función *saludar* y en *main*.
```python
mensaje = "Hola global"
def saludar():
  print("Variable local", mensaje)

if __name__ == "__main__":
  saludar()
  print("Variable global", mensaje)
```

Variable global dentro en la función *saludar* que se puede acceder desde *main*.
```python
def saludar():
  global mensaje
  mensaje = "Hola global"

if __name__ == "__main__":
  saludar()
  print("Variable global", mensaje)
```

### Import
Normalmente las funciones se organizan en librerias (en el caso de Python se llaman paquetes) que se pueden importar para ser usadas, en lo anterior radica la potencia de los lenguages de programación como Python, Java y C, en el desarrollo de potentes librerías que permiten ejecutar una infinidad de tareas.

La palabra reservada para importar paquetes en Python es *import*, puede traer un módulo completo o traer parte de las funciones de un módulo. 

El archivo [operaciones.py](/operaciones.py) contiene dos funciones, una para elevar al cuadrado y otra para sumar dos números.
```python
# operaciones.py
def elevar_al_cuadrado(x:float) -> float:
  return x**2

def sumar_dos_numeros(x:float, y:float) -> float:
  return x+y
```

El archivo [calculadora.py](/calculadora.py) en la línea 1 importa todas la funciones de operaciones usando el simbolo (*). Alternativamente se podría usar `from operaciones import elevarCuadrado` y solo traeria la función elevar al cuadrado.

```python
from operaciones import *

if __name__ == "__main__":
  x = float(input("Ingrese un numero real:"))
  x_squared = elevar_al_cuadrado(x)
  print("El cuadrado de " + str(x) + " es " + str(x_squared))

  y = float(input("Ingrese un numero real:"))
  suma = sumar_dos_numeros(x,y)
  print("La suma de " + str(x) + " y " + str(y) + " es " + str(suma))
```

El archivo [calculadora2.py](/calculadora2.py) en la línea 1 importa todo el módulo `operaciones` por ende cuando se desea usar una función se debe invocar las funciones antecediendolas con `operaciones.` (en el curso de POO lo entenderán en detalle).

```python
import operaciones

if __name__ == "__main__":
  x = float(input("Ingrese un numero real:"))
  x_squared = operaciones.elevar_al_cuadrado(x)
  print("El cuadrado de " + str(x) + " es " + str(xSquared))

  y = float(input("Ingrese un numero real:"))
  suma = operaciones.sumar_dos_numeros(x,y)
  print("La suma de " + str(x) + " y " + str(y) + " es " + str(suma))
```

**Ejercicio:** Uno de los módulos que trae python es *math*, hacer un porgrama en Python importando *math* y usar 5 de las funciones incluidas en este módulo.

----
### Info adicional

- [Python functions](https://learn.microsoft.com/en-us/training/modules/functions-python/)
- [Functions explanation python](https://stackoverflow.com/questions/32409802/basic-explanation-of-python-functions)
- [All You Need to know About Functions in Python](https://medium.com/@datasciencejourney100_83560/all-you-need-to-know-about-functions-in-python-8d39d06ec691)
------

- [Ejercicio de funciones - Hackerrank](https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true)


----

## Reto 5
Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_6 en slack.

1. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/FRvCmpxx/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

2. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

4. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

5. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

6. Consultar qué es y cómo funciona *pip* en python.

7. Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.
