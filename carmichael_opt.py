# Criba de Eratóstenes para primos hasta n
def criba_primos(hasta):
    primos = [True] * (hasta + 1)
    primos[0] = primos[1] = False
    for i in range(2, int(hasta ** 0.5) + 1):
        if primos[i]:
            for j in range(i * i, hasta + 1, i):
                primos[j] = False
    return primos

# Máximo común divisor (Euclides)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Exponenciación modular rápida
def potencia_mod(a, b, mod):
    resultado = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            resultado = (resultado * a) % mod
        a = (a * a) % mod
        b //= 2
    return resultado

# Verifica si n es de Carmichael
def es_carmichael(n):
    for a in range(2, n):
        if gcd(a, n) == 1:
            if potencia_mod(a, n - 1, n) != 1:
                return False
    return True

# Algoritmo principal optimizado
def buscar_carmichael(inicio, fin):
    primos = criba_primos(fin)
    resultado = []

    for n in range(inicio, fin + 1):
        if not primos[n]:  # solo compuestos
            if es_carmichael(n):
                resultado.append(n)

    return resultado

# -----------------------------
# Uso del algoritmo
# -----------------------------

inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número de fin: "))

numeros = buscar_carmichael(inicio, fin)

print("\nNúmeros de Carmichael en el rango:")
print(numeros if numeros else "No se encontraron números de Carmichael.")
