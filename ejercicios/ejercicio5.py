#Algoritmo cadenainvertida
# Entrada
cadena = input("Introduzca su cadena de caracteres para ser invertida: ")
cadena_invertida = []
# Proceso
for i in range((len(cadena)-1),-1,-1):
    cadena_invertida.append(cadena[i])
cadena_invertida = "".join(cadena_invertida)
# Salida
print(cadena_invertida)