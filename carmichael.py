# Numeros de carmichael

# Función para calcular el máximo común divisor (Euclides)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Exponenciación modular rápida: (a^b) % mod
def potencia_mod(a, b, mod):
    resultado = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            resultado = (resultado * a) % mod
        a = (a * a) % mod
        b //= 2
    return resultado

# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Verifica si un número es de Carmichael
def es_carmichael(n):
    if n < 2 or es_primo(n):
        return False
    for a in range(2, n):
        if gcd(a, n) == 1:
            if potencia_mod(a, n - 1, n) != 1:
                return False
    return True

# Busca todos los números de Carmichael en el rango dado
def buscar_carmichael(inicio, fin):
    resultado = []
    for n in range(inicio, fin + 1):
        if es_carmichael(n):
            resultado.append(n)
    return resultado


inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número de fin: "))

numeros = buscar_carmichael(inicio, fin)

print("\nNúmeros de Carmichael en el rango:")
print(numeros if numeros else "No se encontraron números de Carmichael.")


