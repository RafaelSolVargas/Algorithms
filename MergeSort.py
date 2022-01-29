class Merge():
    def __init__(self) -> None:
        self.__nome = 'Merge'

    # Merge sort quebra toda a entrada em listas de valores únicos, e então vai remontando
    # as listas ordenadamente comparando os valores das listas
    # Complexidade: O(n log n)
    def mergesort(self, sequence) -> list:
        if len(sequence) == 1:
            return sequence

        half = len(sequence) // 2

        arrayOne = sequence[:half]
        arrayTwo = sequence[half:]

        arrayOne = self.mergesort(arrayOne)
        arrayTwo = self.mergesort(arrayTwo)

        return self.merge(arrayOne, arrayTwo)

    def merge(self, arrayOne: list, arrayTwo: list):
        arrayThree = []

        while (len(arrayOne) > 0 and len(arrayTwo) > 0):
            if arrayOne[0] < arrayTwo[0]:
                arrayThree.append(arrayOne[0])
                arrayOne.pop(0)
            else:
                arrayThree.append(arrayTwo[0])
                arrayTwo.pop(0)

        # Agora, ou arrayOne ou arrayTwo estão vazios
        while len(arrayOne) > 0:
            arrayThree.append(arrayOne.pop(0))

        while len(arrayTwo) > 0:
            arrayThree.append(arrayTwo.pop(0))

        return arrayThree


insertion = Merge()
ordenada = insertion.mergesort(
    [2, 5, 4, 6, 8, 5, 3, 1, 2, 5, 3, 6, 34, 235, 345, 124, 3476, 1235, 12, 3, 2, 5, 2])
print(ordenada)
