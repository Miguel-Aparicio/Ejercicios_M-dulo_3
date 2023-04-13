def principal():
    #Algortimo hora24
    from datetime import datetime
    while True:
    # Entrada
        hora,minus = input("Ingrese una hora en formato hh:mm ").split(":")
        hora = int(hora)
        minus = int(minus)
        if int(hora) <= 12:
            am_pm = input("¿Su hora es AM o PM? ").upper()
    # Proceso
            if am_pm == "AM" and hora == 12:
                hora = 00
            elif am_pm == "PM" and hora < 12:
                hora = hora+12
        try:
            horaconv = datetime(1,1,1, hora, minus)
            horafin = datetime.strftime(horaconv,"%H:%M")
            # Salida
            print(f"Su hora en formato 24H es las {horafin}")
            seguir = input("¿Quiere introducir otra hora? y/n: ").lower()
            if seguir == "n":
                print("Fin programa horas.")
                break
        except ValueError:
            print("Hora inválida. Por favor, ingrese una hora válida en formato hh:mm.")
