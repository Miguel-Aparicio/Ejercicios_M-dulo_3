def principal():
    valido = False
    listaNumeros = []

    while valido is False:
        numero = input("Introduce un numero entero o un punto para terminar de introducir numeros ==> ")
        if numero == ".":
            valido = True
        else:
            if numero.isdigit():
                listaNumeros.append(int(numero))
            else:
                numero = input("Introduce un numero entero correcto ==> ")
                
    for i in range(len(listaNumeros)):
        if listaNumeros[i] % 3 == 0:
            print(listaNumeros[i])
            
if __name__=="__main__":
   principal()