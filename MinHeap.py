from random import randint
from typing import Any, List, Union


class Node:
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


class MinHeap:
    def __init__(self) -> None:
        self.__heap: List[Node] = []

    def insert(self, value) -> None:
        new_index = len(self.__heap)
        new_node = Node(new_index, value)

        self.__heap.append(new_node)
        self.__increase_value(new_node)

    def minimun(self) -> Union[Any, None]:
        if len(self.__heap) > 0:
            return self.__heap[0].value
        else:
            return None

    def popMinimum(self) -> Union[Any, None]:
        if len(self.__heap) == 0:
            return None

        min_node = self.__heap.pop(0)  # Extract the minimun node

        if len(self.__heap) > 0:
            last = self.__heap.pop()  # Extract the last node
            last.index = 0  # Update the index of node object
            self.__heap.insert(0, last)

            self.__decrease_value(last)  # Heapify the node object

        return min_node.value

    def update(self, index: int, new_value: Any) -> None:
        if index >= len(self.__heap):
            return None

        node = self.__heap[index]  # Get the updated node
        prev_value = node.value  # Get the prev value
        node.value = new_value  # Update the value

        if new_value < prev_value:
            self.__increase_value(node)
        else:
            self.__decrease_value(node)

    def __increase_value(self, node: Node) -> None:
        # While node is not the first and his parent is smaller than him
        while node.index >= 1 and self.__heap[node.parent].value > node.value:
            self.__swap(self.__heap, node.index, node.parent)

    def __decrease_value(self, node: Node) -> None:
        while True:
            # None child
            if not self.__node_has_left_child(node):
                break

            # Only left child
            if not self.__node_has_right_child(node):
                child_left = self.__heap[node.left]
                if self.__node_is_greater_than_other(node, child_left):
                    self.__swap(self.__heap, node.index, node.left)
                else:
                    break

            # Both children
            else:
                if self.__node_is_smaller_than_children(node):
                    break

                minimum_child = self.__get_smaller_child(node)
                self.__swap(self.__heap, node.index, minimum_child.index)

    def __swap(self, array: list, i: int, j: int) -> None:
        nodeI = self.__heap[i]
        nodeJ = self.__heap[j]

        # Swap the position in array
        array[i], array[j] = array[j], array[i]
        # Update the position in the node objects in heap
        nodeJ.index, nodeI.index = nodeI.index, nodeJ.index

    def __len__(self) -> int:
        return len(self.__heap)

    def __node_has_left_child(self, node: Node) -> bool:
        if node.left >= len(self.__heap):
            return False
        else:
            return True

    def __node_has_right_child(self, node: Node) -> bool:
        if node.right >= len(self.__heap):
            return False
        else:
            return True

    def __node_is_greater_than_other(self, node1: Node, node2: Node) -> bool:
        return node1.value > node2.value

    def __node_is_smaller_than_children(self, node: Node) -> bool:
        left_child = self.__heap[node.left]
        right_child = self.__heap[node.right]

        return node.value < min(left_child.value, right_child.value)

    def __get_smaller_child(self, node: Node) -> Node:
        child_left = self.__heap[node.left]
        child_right = self.__heap[node.right]

        if child_left.value > child_right.value:
            return child_right
        else:
            return child_left


if __name__ == '__main__':
    def test_heap():
        heap = MinHeap()

        for _ in range(1000):
            x = randint(0, 8)
            heap.insert(x)

        for _ in range(950):
            x = randint(0, 5)
            y = randint(0, 5)
            heap.update(y, x)

        last_value = None
        while True:
            value = heap.popMinimum()
            if value is None:
                break
            if last_value is not None:
                if value < last_value:
                    print(f'Code not working, heap returned {last_value} and then returned {value}')

            last_value = value

    test_heap()
