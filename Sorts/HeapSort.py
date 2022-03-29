class HeapSort:
    # Heap: Ordered Binary Tree
    # Max Heap: Parent > Child
    # array[(k-1)/2] -> Parent None of k
    # array[(2*k) + 1] -> Left Child of k
    # array[(2*k) + 2] -> Right Child of k
    def order(self, array):
        lastParentIndex = len(array)-2//2

        for x in range(lastParentIndex, -1, -1):
            self.siftDown(array, x, len(array))

        for end in range(len(array)-1, 0, -1):
            self.swap(array, 0, end)
            self.siftDown(array, 0, end)

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]

    def siftDown(self, array, i, upper):
        while True:
            left = 2*i + 1
            right = 2*i + 2

            if max(left, right) < upper:
                if array[i] >= max(array[left], array[right]):
                    break

                elif array[left] > array[right]:  # If left greater
                    self.swap(array, i, left)  # Swap parent and node
                    i = left  # Att the new parent to positionate in heap
                else:  # If right greater
                    self.swap(array, i, right)  # Swap parent and node
                    i = right  # Att the new parent to positionate in heap

            elif left < upper:  # The left node exists and it's not ordered yet
                if array[left] > array[i]:
                    self.swap(array, i, left)
                    i = left
                else:
                    break

            elif right < upper:  # The right node exists and it's not ordered yet
                if array[right] > array[i]:
                    self.swap(array, i, right)
                    i = right
                else:
                    break

            # If there is no child
            else:
                break

    # Continuamente vai criar max heap, uma tree na qual todos os parent são maiores que os filhos
    # Após criar um max heap, remove o maior valor e manda para o final do array

    # Após remover o maior valor do array ou do heap, e mandar ele para o final do array
    # (trocando com o numero naquela posição) o heap se torna somente uma tree normal,
    # e precisamos fazer a função heapify, que é colocar esse numero que foi trocado com o maior
    # em seu lugar correto, visto que todos os outros já estão corretamente posicionados
    # Então essa função recebe uma tree e transforma ela em um max heap


if __name__ == '__main__':
    insertion = HeapSort()
    lista = [2, 1, 4, 2, 1, 5, 2, 6, 3, 12, 2, 325, 235, 12, 2, 1, 56, 3]
    insertion.order(lista)
    last_value = lista[0]
    for value in lista:
        if value < last_value:
            print(f'Code not working, {value}, {last_value}')
        last_value = value
    print(lista)
