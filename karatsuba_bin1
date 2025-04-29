import time

def tradicional_base2(u, v):
    if u < 2 or v < 2:
        return u * v

    n = max(u.bit_length(), v.bit_length())
    m = n // 2
    p = 2 ** m

    a = u // p
    b = u % p
    c = v // p
    d = v % p

    ac = tradicional_base2(a, c)
    bd = tradicional_base2(b, d)
    ad = tradicional_base2(a, d)
    bc = tradicional_base2(b, c)

    return ac * (p ** 2) + (ad + bc) * p + bd

def karatsuba_base2(u, v):
    if u < 2 or v < 2:
        return u * v

    n = max(u.bit_length(), v.bit_length())
    m = n // 2
    p = 2 ** m

    a = u // p
    b = u % p
    c = v // p
    d = v % p

    ac = karatsuba_base2(a, c)
    bd = karatsuba_base2(b, d)
    suma_prod = karatsuba_base2(a + b, c + d)

    return ac * (p ** 2) + (suma_prod - ac - bd) * p + bd

u = 2**500
v = 2**500

ini = time.time()
res_kar = karatsuba_base2(u, v)
fin = time.time()
tiempo_kar = fin - ini

ini1 = time.time()
res_trad = tradicional_base2(u, v)
fin1 = time.time()
tiempo_trad = fin1 - ini1

print(f"\nMultiplicación clásica (bin): {res_trad}")
print(f"Tiempo: {tiempo_trad:.8f} segundos")

print(f"\nKaratsuba (bin): {res_kar}")
print(f"Tiempo: {tiempo_kar:.8f} segundos")