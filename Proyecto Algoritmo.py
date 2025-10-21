#Calcular el tiempo con los ojos cerrados por el parpadeo
edades = []
contador = 0
limite = 5
while True:
    contador += 1
    if contador > limite:
        print("Máximo de entradas, gracias, se cerrará el programa")
        break
    N = float(input("Ingrese su edad en años: "))
    if N > 150 or N < 0:
        print("No creo, pon tu edad real")
        continue
    actual = [N]
    if N > 80 and N <= 120:
        print (f"{N}! Eres bastante viejo" )
    elif N <= 3:
        print (f"{N}! Sabes leer?" )
    elif N > 120:
        print (f"{N}!? Eso debe ser un record...")
    Resultado = N * 365.25 / 10 + 0.23
    actual.append(Resultado)
    edades.append(actual)
    print (f"Haz pasado {Resultado:.2f} días parpandeando")
    print("\nRegistro de entradas y resultados:")
    for registro in edades:
        print(f"Edad: {registro[0]} años, con {registro[1]:.2f} días parpadeando")
    continue