class Insertion():
    def __init__(self) -> None:
        self.__nome = 'Insertion'

    # Sempre possui uma lista ordenada, iniciando à esquerda, vai avançando um index de cada vez
    # e posicionando o novo número na posição exatamente
    # Faz um único loop por todo o array, em cada index n pode fazer n interações para determinar a posição correta
    # Complexidade: in-place O(n²)
    # O Insertion Sort é estável, essa propriedade está relacionada à ordem relativa de valores iguais no array original
    # Ele também é estável por que mantém a ordem relativa dos valores iguais, isso ocorre pq as trocas
    # são feitas com vizinhos. Os valores vão sendo afastados um a um e não dando saltos. Por isso, um elemento qualquer nunca
    # trocará de posição com elementos de mesmo valor.
    def order(self, lista: list) -> list:
        for x in range(1, len(lista)):
            while x > 0 and lista[x] < lista[x-1]:
                # Está trocando, mas talvez só descobrir o index e depois fazer o insert
                lista[x], lista[x-1] = lista[x-1], lista[x]
                x -= 1

        return lista


if __name__ == '__main__':
    insertion = Insertion()
    ordenada = insertion.order(
        [2, 1, 4, 2, 1, 5, 2, 6, 3, 12, 2, 325, 235, 12, 2, 1, 56, 3])
    last_value = ordenada[0]
    for value in ordenada:
        if value < last_value:
            print(f'Code not working, {value}, {last_value}')
        last_value = value
    print(ordenada)
