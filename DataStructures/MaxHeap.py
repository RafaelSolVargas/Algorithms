class Node():
    def __init__(self, index, value) -> None:
        self.value = value
        self.index = index

    @property
    def parent(self):
        return (self.index-1) // 2

    @property
    def left(self):
        return self.index * 2 + 1

    @property
    def right(self):
        return self.index * 2 + 2


class MaxHeap():
    def __init__(self, array: list) -> None:
        self.heap = array

    def printHeap(self) -> None:
        print([node.value for node in self.heap])

    def insert(self, value) -> None:
        newIndex = len(self.heap)
        newNode = Node(newIndex, value)
        self.heap.append(newNode)

        self.__increase_value(newNode)

    def maximum(self) -> int:
        if len(self.heap) > 0:
            return self.heap[0].value

    def popMaximum(self) -> int:
        if len(self.heap) == 0:
            return None

        max = self.heap.pop(0)  # Extract the max element

        # If there is more itens in heap to ordenate
        if len(self.heap) > 0:
            last = self.heap.pop()  # Extract the last element

            last.index = 0  # Update the index of node object
            self.heap.insert(0, last)

            self.__decrease_value(last)  # Heapify the node object
        return max.value

    def update(self, index, new_value) -> None:
        if index >= len(self.heap):
            return None

        node = self.heap[index]  # Get the updated node
        prev_value = node.value  # Get the prev value
        node.value = new_value  # Update the value

        if new_value > prev_value:
            self.__increase_value(node)
        else:
            self.__decrease_value(node)

    def __increase_value(self, node: Node) -> None:
        # While node not the first and his parent is minor
        while node.index >= 1 and self.heap[node.parent].value < node.value:
            self.__swap(self.heap, node.index, node.parent)

    def __decrease_value(self, node: Node) -> None:
        while True:
            # If left child runs out
            if node.left >= len(self.heap):
                break

            # Only left child
            if node.right >= len(self.heap):
                nodeLeft = self.heap[node.left]
                if nodeLeft.value > node.value:
                    self.__swap(self.heap, node.index, node.left)
                else:
                    # If current node is bigger
                    break

            # Both children
            else:
                nodeLeft = self.heap[node.left]
                nodeRight = self.heap[node.right]

                # If the current node is bigger, finish the decrease
                if node.value > max(nodeLeft.value, nodeRight.value):
                    break

                # if left child is bigger, swap them
                if nodeLeft.value > nodeRight.value:
                    self.__swap(self.heap, node.index, node.left)
                # if right child is bigget, swap them
                else:
                    self.__swap(self.heap, node.index, node.right)

    def __swap(self, array, i, j):
        nodeI = self.heap[i]
        nodeJ = self.heap[j]

        # Inverte a posição do nodeI e nodeJ no array
        array[i], array[j] = array[j], array[i]
        # Atualiza a posição dos node dentro do objeto
        nodeJ.index, nodeI.index = nodeI.index, nodeJ.index
