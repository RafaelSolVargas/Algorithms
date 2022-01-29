class Bubble():
    """
    Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order
    """

    def __init__(self) -> None:
        self.__nome = 'Bubble'

    # Faz diversos loops pelo array, em cada index do loop ele vai levando o valor para a direita
    # até que o valor à direita seja maior
    # Complexidade: O(n²), pior caso é quando o array is reverse sorted
    # Melhor caso de complexidade: O(n), quando o array já está ordenado
    # Auxiliary Space: O(1). Possui Sorting in place e é estável
    def order(self, lista) -> list:
        sorted = False
        while not sorted:
            sorted = True
            for x in range(0, len(lista) - 1):
             #               print(f'Loop com {x}')
                if lista[x] > lista[x+1]:
                    sorted = False  # Só vai sair do while após estar ordenado
#                    print(f'Trocando {lista[x]} por {lista[x+1]}')
                    lista[x], lista[x+1] = lista[x+1], lista[x]

        return lista


bubble = Bubble()
ordered = bubble.order(
    [2, 1, 4, 2, 5, 7])
print(ordered)
