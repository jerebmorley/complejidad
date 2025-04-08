"""
    Encuentra el elemento mayoritario en un arreglo si existe.
    Un elemento es mayoritario si aparece más de n/2 veces.
"""

def elemento_mayoritario(arr):
    n = len(arr)
    cont = {}

    for i in arr:
        cont[i] = cont.get(i, 0) + 1
        if cont[i] > n // 2:
            return i
    return None

example = [3, 3, 4, 2, 3, 3, 3, 1]
result = elemento_mayoritario(example)
if result:
    print(f"El elemento mayoritario es: {result}")
else:
    print("No hay elemento mayoritario.")