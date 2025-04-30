import time

# criba de eratostenes
def criba(hasta):
    primos = []
    es_primo = [True] * (hasta + 1)
    es_primo[0] = es_primo[1] = False
    for i in range(2, hasta + 1):
        if es_primo[i]:
            primos.append(i)
            for j in range(i * i, hasta + 1, i):
                es_primo[j] = False
    return primos

# factoriza un numero con una lista de primos
def factorizar(n, primos):
    factores = {}
    for p in primos:
        if p * p > n:
            break
        while n % p == 0:
            factores[p] = factores.get(p, 0) + 1
            n //= p
    if n > 1:
        factores[n] = 1
    return factores

# verifica si un numero es de carmichael usando el teorema de korselt
# korselt dice que si n es de Carmichael si: es libre de cuadrados (no tiene ningún factor primo repetido) y para todo primo P que divide a n, se cumple que  P − 1  divide  n − 1 .
def es_korselt(n, primos):
    factores = factorizar(n, primos)

    if len(factores) < 2:  # debe ser compuesto
        return False

    for exponente in factores.values():  # libre de cuadrados
        if exponente > 1:
            return False

    for p in factores:  # p - 1 debe dividir n - 1
        if (n - 1) % (p - 1) != 0:
            return False

    return True

def buscar_carmichael(inicio, fin):
    primos = criba(int(fin ** 0.5) + 1)
    resultado = []
    for n in range(inicio, fin + 1):
        if es_korselt(n, primos):
            resultado.append(n)
    return resultado

inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número de fin: "))

t0 = time.time()  # Tiempo inicial
numeros = buscar_carmichael(inicio, fin)
t1 = time.time()  # Tiempo final

print("\nNúmeros de Carmichael encontrados:")
print(numeros if numeros else "No se encontraron números de Carmichael.")
print(f"\nTiempo de ejecución: {t1 - t0:.4f} segundos")
