class Quick():
    def __init__(self) -> None:
        self.__nome = 'Quick'

    # Puxa um pivô aleatório de uma lista e ordena os maiores e menores
    # Pior Caso: Ocorre quando o pivô é sempre o maior ou menor elemento (partições de tamanho desequilibrado)
    # Melhor Caso: Ocorre quando as partições têm sempre o mesmo tamanho (balanceadas)
    # Vantagens:
    # Laço interno simples, pequena memória auxiliar para recursão, complexidade O(n log n)
    # Desvantagens:
    # Não é estável e o pior caso é quadrático

    # Otimizações:
    # Escolher o pivô como a mediana de três elementos
    # Usar inserção para partições pequenas
    # Quick Sort não recursivo e que limita o tamanho da pilha auxiliar ordenando partições pequenas primeiro

    def quick_sort(self, sequence: list):
        # O algoritmo termina somente quando as listas se tornam únicas
        # Tira um pivot para usar como parâmetro para todo o resto
        if len(sequence) <= 1:
            return sequence
        else:
            pivot = sequence.pop()

        items_greater = []
        items_lower = []
        for number in sequence:
            if number > pivot:
                items_greater.append(number)
            else:
                items_lower.append(number)

        # Repete o código
        return self.quick_sort(items_lower) + [pivot] + self.quick_sort(items_greater)


if __name__ == '__main__':
    insertion = Quick()
    ordenada = insertion.quick_sort(
        [2, 1, 4, 2, 1, 5, 2, 6, 3, 12, 2, 325, 235, 12, 2, 1, 56, 3])
    last_value = ordenada[0]
    for value in ordenada:
        if value < last_value:
            print(f'Code not working, {value}, {last_value}')
        last_value = value
    print(ordenada)
