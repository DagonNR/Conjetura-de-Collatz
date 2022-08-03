# Conjetura de Collatz, dice que si seguimos los siguientes pasos siempre llegaremos al número 1
# Los números pares se dividen entre 2 (Ejemplo 24/2)
# Los números impares se multiplican por 3 y se les suma 1 (Ejemplo 37*3+1)

numero = int(input("Ingresa un número: "))

def collatz(numero):
    while numero != 1:
        if numero % 2 == 0:
            numero = int(numero / 2)
        elif numero % 2 == 1:
            numero = int(numero * 3 + 1)
        if numero == 1:
            print("Conjetura correcta, el número llego a " + str(numero))
    return numero

numero = collatz(numero)