#Calcular el tiempo con los ojos cerrados por el parpadeo
edades = []
while True:
    N = float(input("Ingrese su edad en años: "))
    print("No creo, pon tu edad real")
    if N > 150 or N < 3:
        continue
    actual = [N]
    if N > 80 and N <= 120:
        print (f"{N}! Eres bastante viejo" )
    elif N < 3:
        print (f"{N}! Sabes leer?" )
    elif N > 120:
        print (f"{N}!? Eso debe ser un record...")
    Resultado = N * 365.25 / 10 + 0.23
    actual.append(Resultado)
    edades.append(actual)
    print (f"Haz pasado {Resultado} días parpandeando")
    print("\nRegistro de entradas y resultados:")
    for registro in edades:
        print(f"Edad: {registro[0]} años, con {registro[1]:.2f} días parpadeando")
    break