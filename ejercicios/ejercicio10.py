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
        if "a" in listaCadenas[i] or "e" in listaCadenas[i] or "i" in listaCadenas[i] or "o" in listaCadenas[i] or "u" in listaCadenas[i]:
            print(listaCadenas[i])
            
if __name__=="__main__":
   principal()