def principal():
    valido = False
    listaCadenas = []

    while valido is False:
        cadena = input("Introduce una cadena o un punto para terminar de introducir palabras ==> ")
        if cadena == ".":
            valido = True
        else:
            listaCadenas.append(cadena)
            
    for i in range(len(listaCadenas)):
        if len(listaCadenas[i]) > 5:
            print(listaCadenas[i])
            
if __name__=="__main__":
   principal()