import time

# multiplicación clásica por divide y vencerás (4 multiplicaciones)
def tradicional(u, v):
    if u < 10 or v < 10:
        return u * v

    n = max(len(str(u)), len(str(v)))
    m = n // 2
    
    a, b = divmod(u, 10**m)
    c, d = divmod(v, 10**m)
    
    ac = tradicional(a, c)
    bd = tradicional(b, d)
    ad = tradicional(a, d)
    bc = tradicional(b, c)

    return ac * 10**(2*m) + (ad + bc) * 10**m + bd

# multiplicación de karatsuba (3 multiplicaciones)
def karatsuba(u, v):
    if u < 10 or v < 10:
        return u * v

    n = max(len(str(u)), len(str(v)))
    m = n // 2

    a, b = divmod(u, 10**m)
    c, d = divmod(v, 10**m)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    suma1 = a + b
    suma2 = c + d
    suma_prod = karatsuba(suma1, suma2)

    return ac * 10**(2*m) + (suma_prod - ac - bd) * 10**m + bd

"""
u = int(input("Introduce el primer número: "))
v = int(input("Introduce el segundo número: "))  
"""

u = 2**500
v = 2**500

ini = time.time()
res_kar = karatsuba(u, v)
fin = time.time()
tiempo_kar = fin - ini

ini1 = time.time()
res_trad = tradicional(u, v)
fin1 = time.time()
tiempo_trad = fin1 - ini1

print(f"\nMultiplicación clásica: {res_trad}")
print(f"Tiempo: {tiempo_trad:.8f} segundos")

print(f"\nKaratsuba: {res_kar}")
print(f"Tiempo: {tiempo_kar:.8f} segundos")

print("\nEl resultado es correcto: " + str(res_kar == res_trad))

if tiempo_kar < tiempo_trad:
    print(f"\nDiferencia de tiempo: {tiempo_trad - tiempo_kar:.8f} segundos")
    print(f"\nKaratsuba es un {(tiempo_kar/tiempo_trad)*100:.2f}% más rápido")
else:
    print(f"\nDiferencia de tiempo: {tiempo_kar - tiempo_trad:.8f} segundos")
    print(f"\nKaratsuba es un {(tiempo_trad/tiempo_kar)*100:.2f}% más lento")

    