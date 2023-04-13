def principal():
    #Algoritmo sumanumeros
    # Entrada
    numero = input("introduzca su número para sumar todos los números del 1 al introducido: ")
    listanum = []
    suma = 0
    # Proceso
    try:
        numero = int(numero)
        if numero == 1:
            res = ("Si el número es 1, el resultado también es 1.")
        for i in range(1,(numero+1)):
            listanum.append(i)
        for i in range(len(listanum)):
            suma += listanum[i]
        suma = str(suma)
        res = (f"La suma desde 1 hasta {numero} es: {suma}")
    except:
        res = ("Solo se admiten números exclusivamente.")
    # Salida
    finally:
        print(res)