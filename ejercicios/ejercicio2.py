def principal():
    from datetime import datetime
    from pytz import timezone
    import pytz
    while True:
        continente = input("Escriba su continente: ")
        ciudad = input("escriba su ciudad: ")
        try:
            fecha = datetime.now(timezone(f"{continente}/{ciudad}"))
            res = fecha.strftime("%H:%M")
            print(f"La hora actual de {ciudad} es: {res}")
            break
        except:
            print("Error con los valores introducidos. Intentelo nuevamente.")