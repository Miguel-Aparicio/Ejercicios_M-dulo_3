def principal():
    cadena = input("Introduce una frase: ").lower()
    palabra = input("Introduce una palabra que se encuentre en la frase 1 o más veces: ").lower()
    palabraReemplazo = input("Introduce una palabra que se cambiará por la anterior palabra: ").lower()

    print(f"La frase que escribiste es '{cadena}'. Después de cambiar las palabras que escogiste modificar, pasa a ser '{cadena.replace(palabra, palabraReemplazo)}'")


if __name__=="__main__":
   principal()