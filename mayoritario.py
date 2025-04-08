# Algoritmo mayoritario

def elemento_mayoritario(lista):
    diccionario = {}
    n = len(lista)
    for i in lista:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
        if diccionario[i] > n // 2:
            return i
    return None

x = elemento_mayoritario([3, 2, 2, 2, 1, 2, 3, 2, 2, 1])
print(x)