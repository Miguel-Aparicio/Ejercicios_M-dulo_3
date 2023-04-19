def principal():
        #Algoritmo formatofecha
        from datetime import datetime
        while True:
                try:
                # Entrada
                        fechaCadena = input("Introduzca fecha (dd/mm/aaaa): ")
                # Proceso
                        fecha = datetime.strptime(fechaCadena,"%d/%m/%Y")
                        fechaconv = fecha.strftime("%Y-%m-%d")
                # Salida
                        print(f"La nueva fecha formateada es: {fechaconv}")
                        break
                except:
                        print("Errores en los valores introducidos. Intentelo de nuevo.")

if __name__=="__main__":
   principal()