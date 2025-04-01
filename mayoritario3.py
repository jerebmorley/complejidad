def mayoritario_rapido(nums):  # No hay forma de verificar que no hay un mayoritario
    candidato, conteo = None, 0

    for num in nums:
        if conteo == 0:
            candidato = num
        conteo += (1 if num == candidato else -1)

    return candidato  # No se verifica, útil si garantizamos un mayoritario

# Ejemplo de uso
nums = [0, 9, 4, 2, 3, 7, 6, 1]
print(mayoritario_rapido(nums))  # Salida: 3
