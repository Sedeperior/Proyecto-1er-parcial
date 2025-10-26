edades = []
contador = 0
limite = 5
while True:
    contador += 1
    if contador > limite:
        print("Máximo de entradas, gracias, se cerrará el programa")
        break
    print("Ingrese su edad en: ")
    años = float(input("Años: "))
    meses = float(input("Meses: "))
    días = float(input("Días: "))
    resultado = (años * 365.25) + (meses * 30.5) + días
    n = resultado / 365.25
    parpa = resultado / 10
    if n > 150 or n < 0:
        print("No creo, pon tu edad real")
        continue
    actual = [n]
    if años > 80 and años <= 120:
        print (f"{años}! Eres bastante viejo" )
    elif años <= 3:
        print (f"{años}! Sabes leer?" )
    elif años > 120:
        print (f"{años}!? Eso debe ser un record...")
    actual.append(parpa)
    edades.append(actual)
    print (f"Haz pasado {parpa:.2f} días parpandeando")
    print("Registro de entradas y resultados:")
    for registro in edades:
        print(f"Edad: {registro[0]:.2f} años, con {registro[1]:.2f} días parpadeando")
    continue