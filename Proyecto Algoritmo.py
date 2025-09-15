#Calcular el tiempo con los ojos cerrados por el parpadeo
N = float (input("Ingrese su edad en años: "))
if N > 80 and N <= 120:
    print (f"{N}! Eres bastante viejo" )
elif N < 3:
    print (f"{N}! Sabes leer?" )
elif N > 120:
    print (f"{N}!? Eso debe ser un record...")
Resultado = N * 9.13125 + 1 - 1
print (f"Haz pasado {Resultado} días parpandeando")