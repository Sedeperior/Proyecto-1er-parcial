#Calcular el tiempo con los ojos cerrados por el parpadeo
while True:
    N = float(input("Ingrese su edad en años: "))
    if N > 150 or N < 3:
        print ("No creo, es demasiado, pon tu edad real:")
        lista = []
        lista.append (N)
        print (f"Realmente pusiste {lista} años?")
        continue
    if N > 80 and N <= 120:
        print (f"{N}! Eres bastante viejo" )
    elif N < 3:
        print (f"{N}! Sabes leer?" )
    elif N > 120:
        print (f"{N}!? Eso debe ser un record...")
    Resultado = N * 365.25 / 10 + 0.23
    print (f"Haz pasado {Resultado} días parpandeando")
    break