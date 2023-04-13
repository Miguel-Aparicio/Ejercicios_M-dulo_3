import os
#from Varios import principal

from ejercicios import ejercicio1
from ejercicios import ejercicio2
from ejercicios import ejercicio3
from ejercicios import ejercicio4
from ejercicios import ejercicio5
from ejercicios import ejercicio6
from ejercicios import ejercicio7
from ejercicios import ejercicio8
from ejercicios import ejercicio9
from ejercicios import ejercicio10
from ejercicios import ejercicio11

while True:
    os.system("cls") #Limpia la pantalla en la consola

    print("Bienvenidos")
    print("Menu principal")

    print("1-Calcular letra DNI español")
    print("2-Calcular Salario Neto Español")
    print("3-Determinar ruta para llegar por avion")
    print("4-Calcular çarea y perímetro de un círculo dado su radio")
    print("5-Calcular numero mayor y menor")
    print("6-Convertir grados Celsius a Fahrenheit")
    print("7-Determinar numero par o impar")
    print("8-Determinar si un año es bisiesto")
    print("9-Determinar si una cadena de texto es un palíndromo")
    print("10-Ordenar lista de nombres")
    print("11-Calcular Salario Neto Español")

    print("0-Salir")

    opcion = input("Seleccione una opción:")

    if opcion == "1":
        ejercicio1.principal()
    elif opcion == "2":
        ejercicio2.principal()
    elif opcion == "3":
        ejercicio3.principal()
    elif opcion == "4":
        ejercicio4.principal() 
    elif opcion == "5":
        ejercicio5.principal() 
    elif opcion == "6":
        ejercicio6.principal() 
    elif opcion == "7":
        ejercicio7.principal()
    elif opcion == "8":
        ejercicio8.principal()     
    elif opcion == "9":
        ejercicio9.principal() 
    elif opcion == "10":
        ejercicio10.principal() 
    elif opcion == "11":
        ejercicio11.principal() 
   

    elif opcion == "0":
        print("Un placer . Nos vemos!")
        break

    continuar=input("Presione enter para continuar...")
