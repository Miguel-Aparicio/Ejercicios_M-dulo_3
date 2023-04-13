def principal():
    #Algoritmo contarcadenacaracteres
    # Entrada
    cadena = input("Introduzca su cadena de caracteres: ").replace(",","").replace(".",".").split(" ")
    i = 0
    numero = 0
    # Proceso
    while i != len(cadena):
        numero +=1
        i += 1
    # Salida
    print(numero)