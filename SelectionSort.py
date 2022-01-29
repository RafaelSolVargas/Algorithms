class Selection():
    # Selection Sort faz loops por todo o array e determina o menor valor, colocando ele
    # à esquerda do array, e então refaz o loop no array, ignorando a parte já ordenada à esquerda
    # O Selection Sort é in-place e O(n²), mas não é estável.
    # A propriedade de estabilidade está relacionado ao fato de dois valores iguais não trocarem de posição
    # Se houver duas ocorrências de um 5 no array inicial, ao final, o primeiro que apareceu é o primeiro no
    # array ordenado também, ou seja, eles não trocaram de posição desnecessariamente durante o código

    # O custo do Selection Sort é igual ao custo da soma de termos de uma PA, 1+2+3+(n-1), com
    # a1 = 1 e an = (n-1). Logo o tempo de execução do algoritmo é dado, por (n²)/2. E aplicando as
    # diretrizes de simplificação, o Selection Sort é O(n²)
    def __init__(self) -> None:
        self.__nome = 'Selection'

    def order(self, lista) -> list:
        i = 0
        while i < len(lista):
            menor = None
            menorIndex = None

            for x in range(i, len(lista)):
                if menor == None or lista[x] < menor:
                    menor = lista[x]
                    menorIndex = x

            # print(menor)
            # Inverte o primeiro e o menor
            lista[i], lista[menorIndex] = lista[menorIndex], lista[i]
            i += 1  # Att o index inicial
        return lista


selection = Selection()
ordenada = selection.order(
    [2, 1, 4, 2, 1, 5, 2, 6, 3, 12, 2, 325, 235, 12, 2, 1, 56, 3])
print(ordenada)
