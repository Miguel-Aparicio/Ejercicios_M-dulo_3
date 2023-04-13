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

    print("1-Modificar fecha")
    print("2-Comprobar hora actual de una zona horaria")
    print("3-Comprobar cuantas palabras hay en una cadena de caracteres")
    print("4-Mostrar hora introducida en formato 24h")
    print("5-Mostrar cadena invertida")
    print("6-Mostrar suma de todos los numeros desde el 1 hasta el numero ingresado")
    print("7-Imprimir cada caracter en una linea separada")
    print("8-Determinar que palabras tienen mas de 5 caracteres")
    print("9-Reemplazar palabras de una frase")
    print("10-Determinar que palabras tienen al menos una vocal de una frase")
    print("11-Determinar que numeros introducidos son multiplos de 3")

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
