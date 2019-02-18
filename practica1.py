#!/usr/bin/env python3.6

print ("-¿Cuales son los dos valores de tipo de dato booleano?¿Como se escriben?")
print ("Las dos variables de tipo booleano son verdadero y falso, se escriben como True y False.")
print ()

print ("-¿Cuales son los tres operadores booleanos?")
print ("Conjuncion logica (&&), disyuncion logica (||) y negacion logica (!).")
print ()
#Tablas de verdad
print ("CONJUNCION")
bool = [True, False]
print ('t\t f\t Conjuncion\t') 
for t in bool:
    for f in bool:
        print (t,f,'',t and f)
print ()

print ("DISYUNCION")
print ('t\t f\t Disyuncion\t') 
for t in bool:
    for f in bool:
        print (t,f,'',t or f)
print ()

print ("NEGACION")
print ('t\t Negacion\t') 
for t in bool:
    print (t,'', not t)
print ()

print ("-¿Cuales son los seis operadores de comparacion?")
print ("Devuelve verdadero si ambos valores son: Iguales (==), diferentes (!=), mayor (>), menor (<), mayor o igual (>=), menor o igual (<=).")
print ()
print ("-¿Cual es la diferencia entre el operador igual y el operador de asignacion?")
print ("El operador igual devuelve true si los ambos valores de las variables son iguales, mientras que el operador de asignacion asigna a la variable el valor declarado.")
print ()
print ("-Explique que es una condicion y donde la usaria.")
print ("Una condicion es una sentencia que puede ser verdadera o falsa, usualmente la uso para filtrar ciertos datos que cumplan ciertos criterios.")
print ()
print ("-¿Que puede hacer si su programa esta atascado en un bucle infinito?")
print ("Se puede presionar Ctrl+c, ademas hay otra forma que involucra meter un codigo mas complicado de hacer.")
print ()
print ("-¿Cual es la diferencia entre romper y continuar?")
print ("Romper se usa para indicar que una estructura debe terminar una vez que haga la operacion indicada anteriormente, continuar por el contrario hace que el compilador siga leyendo el codigo.")
print ()
print ("-¿Cual es la diferencia entre rango (10), rango (0, 10) y rango (0, 10, 1) en un bucle for?")
print ("rango (10) indica el valor que tomara la variable del for, rango (0, 10) indica que el for inicia desde 0 hasta 10 y rango (0, 10, 1) indica que empezara en 0 hasta 10 y que iria en aumento 1 a 1.")
print ()
#Programa for
print ("Imprimir los primeros n numero y la suma de ellos usando for")
n = int (input ("Inserte el valor de n: "))
print ()
suma = 0

for i in range (1, n + 1):
    print (i)
    suma = suma + i
print ()
print ("La suma es: ") 
print (suma)
print ()
#Programa while
print ("Imprimir los numeros del 1 al 10 con while:")
n = 0

while n < 10:
     n = n + 1
     print (n)
print ()
#Programa impares
print ("Imprimir los m numeros impares")
m = int (input ("Inserte el valor de m: "))
impar = 0
print ("Los numero impares son: ")

for j in range (1, m + 1):
    if j % 2 != 0:
        print (j)
print ()
#Programa serie de Fibonacci
print ("Imprimir los x numeros de la serie de Fibonacci")
x = int (input ("Inserte el valor de x: "))
def fib (x):
    a = 0
    b = 1
    
    for l in range (x):
        c = b + a
        a = b
        b = c
        
    return a
print (fib (x))

#Programa factorial
print ("Imprimir el factorial de un numero z")
z = int (input ("Inserte el valor de z: "))
factorial = 1

for k in range (1, z + 1):
    factorial = factorial * k
print ("El factorial es:")
print (factorial) 
