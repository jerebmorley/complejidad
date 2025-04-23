import time

def tradicional(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2
    n = max(len(str(num1)), len(str(num2)))
    m = n // 2
    h1, l1 = divmod(num1, 10**m)
    h2, l2 = divmod(num2, 10**m)
    return (tradicional(h1, h2) * 10**(2*m) +
            (tradicional(h1, l2) + tradicional(l1, h2)) * 10**m + tradicional(l1, l2))


def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2

    n = max(len(str(num1)), len(str(num2)))
    m = n // 2

    h1, l1 = divmod(num1, 10**m)
    h2, l2 = divmod(num2, 10**m)

    m0 = karatsuba(l1, l2)
    m1 = karatsuba((l1 + h1), (l2 + h2))
    m2 = karatsuba(h1, h2)

    return (m2 * 10**(2 * m)) + ((m1 - m2 - m0) * 10**m) + m0

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
a = 2**500
b = 2**500

ini = time.time()
res_kar = karatsuba(a, b)
fin = time.time()
tiempo = fin - ini

ini1 = time.time()
res_com = tradicional(a, b)
fin1 = time.time()
tiempo1 = fin1 - ini1


print(f"\nMultiplicación común: {res_com}")
print(f"Tiempo: {tiempo1:.8f} segundos")

print(f"\nKaratsuba: {res_kar}")
print(f"Tiempo: {tiempo:.8f} segundos")