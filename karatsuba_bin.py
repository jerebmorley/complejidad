import time

def multiplicacion_clasica_bin(u, v):
    if u < 2 or v < 2:
        return u * v

    n = max(u.bit_length(), v.bit_length())
    m = n // 2

    a = u >> m 
    b = u & ((1 << m) - 1) 
    c = v >> m 
    d = v & ((1 << m) - 1) 

    ac = multiplicacion_clasica_bin(a, c)
    bd = multiplicacion_clasica_bin(b, d)
    ad = multiplicacion_clasica_bin(a, d)
    bc = multiplicacion_clasica_bin(b, c)

    return (ac << (2 * m)) + ((ad + bc) << m) + bd

def karatsuba_bin(u, v):
    if u < 2 or v < 2:
        return u * v

    n = max(u.bit_length(), v.bit_length())
    m = n // 2

    a = u >> m
    b = u & ((1 << m) - 1)
    c = v >> m
    d = v & ((1 << m) - 1)

    ac = karatsuba_bin(a, c)
    bd = karatsuba_bin(b, d)
    suma_prod = karatsuba_bin(a + b, c + d)

    return (ac << (2 * m)) + ((suma_prod - ac - bd) << m) + bd

u = 2**500
v = 2**500

ini = time.time()
res_kar = karatsuba_bin(u, v)
fin = time.time()
tiempo_kar = fin - ini

ini1 = time.time()
res_clasica = multiplicacion_clasica_bin(u, v)
fin1 = time.time()
tiempo_clasica = fin1 - ini1

print(f"\nMultiplicación clásica (bin): {res_clasica}")
print(f"Tiempo: {tiempo_clasica:.8f} segundos")

print(f"\nKaratsuba (bin): {res_kar}")
print(f"Tiempo: {tiempo_kar:.8f} segundos")
