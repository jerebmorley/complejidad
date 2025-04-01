def es_mayoritario(nums):
    n = len(nums)
    candidato, conteo = None, 0
    for i in nums:
        if conteo == 0:
            candidato = i
        conteo += 1 if i == candidato else -1

    if nums.count(candidato) > n // 2:
        return candidato
    return None

example = [3, 3, 4, 2, 3, 3, 3, 1]
print(es_mayoritario(example))
