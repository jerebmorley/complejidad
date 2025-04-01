"""
    Encuentra el elemento mayoritario en un arreglo si existe.
    Un elemento es mayoritario si aparece más de n/2 veces.
"""

def elemento_mayoritario(arr):
    n = len(arr)
    cont = {}

    for num in arr:
        cont[num] = cont.get(num, 0) + 1
        if cont[num] > n // 2:
            return num
    return None

example = [3, 3, 4, 2, 4, 4, 2, 4, 4]
result = elemento_mayoritario(example)
if result:
    print(f"El elemento mayoritario es: {result}")
else:
    print("No hay elemento mayoritario.")