"""
O binary search é um algoritimo de divisão e conquista que encontra um elemento num vetor ordenado

"""

def binarySearch(vet, n):
    ini = 0
    fim = len(vet) -1

    while ini <= fim:
        m = (ini + fim) // 2
        if n == vet[m]:
            return m
        elif n > vet[m]:
            ini = m + 1
        elif n < vet[m]:
            fim = m - 1
    return -1

print(binarySearch([1, 2, 3, 4, 5], 2))