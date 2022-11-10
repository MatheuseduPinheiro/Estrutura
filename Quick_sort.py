def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # Se o valor atual que estamos vendo for maior que o pivô
        # está no lugar certo (lado direito do pivô) e podemos mover para a esquerda,
        # para o próximo elemento.
        # Também precisamos ter certeza de que não ultrapassamos o ponteiro baixo, já que
        # indica que já movemos todos os elementos para o lado correto do pivô
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # Encontramos um valor para alto e baixo que está fora de ordem
        # ou baixo é maior que alto, nesse caso saímos do loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # O laço continua
        else:
            #Saímos do loop
            break

    array[start], array[high] = array[high], array[start]

    return high
def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

quick_sort(array, 0, len(array) - 1)
print(array)
