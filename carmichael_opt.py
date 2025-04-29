# criba
def criba_primos(hasta):
    primos = [True] * (hasta + 1)
    primos[0] = primos[1] = False
    for i in range(2, int(hasta ** 0.5) + 1):
        if primos[i]:
            for j in range(i * i, hasta + 1, i):
                primos[j] = False
    return primos

# euclides
def euclides(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# exponenciación modular rápida????
def fermat(a, b, mod):
    resultado = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            resultado = (resultado * a) % mod
        a = (a * a) % mod
        b = b // 2
    return resultado

def es_carmichael(n):
    for a in range(2, n):
        if euclides(a, n) == 1: # solo coprimos
            if fermat(a, n - 1, n) != 1: # solo fermat
                return False
    return True

# algoritmo principal
def buscar_carmichael(inicio, fin):
    primos = criba_primos(fin)
    resultado = []
    for n in range(inicio, fin + 1):
        if not primos[n]:  # solo compuestos
            if es_carmichael(n) and n != 1: 
                resultado.append(n)
    return resultado

import time

inicio_rango = int(input("Ingrese el número de inicio: "))
fin_rango = int(input("Ingrese el número de fin: "))

inicio = time.time()

numeros = buscar_carmichael(inicio_rango, fin_rango)

fin = time.time()

print("Números de Carmichael en el rango:")
print(numeros if numeros else "No se encontraron números de Carmichael.")

print(f"{fin - inicio:.2f}")


