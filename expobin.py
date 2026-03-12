import sys

def potencia_binaria(base, exponente, modulo=None):
    resultado = 1

    if modulo is not None:
        base %= modulo

    while exponente > 0:
        if exponente % 2 == 1:
            resultado *= base
            if modulo is not None:
                resultado %= modulo

        base *= base
        if modulo is not None:
            base %= modulo

        exponente //= 2

    return resultado


# Leer entrada
datos = list(map(int, sys.stdin.read().split()))

base = datos[0]
exponente = datos[1]

if len(datos) == 3:
    modulo = datos[2]
else:
    modulo = None

resultado = potencia_binaria(base, exponente, modulo)

print(resultado)