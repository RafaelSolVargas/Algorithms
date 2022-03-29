"""
Fixed-Size Structure which can hold items of the same data type. They are indexed, meaning that random access is possible. To operate insertions and deletions from an Array it's necessary to use another array and copy the elements.
Insertion and Deletion operations is O(n), since you have to move all the array 
Access Elements is O(1), since you have the index
"""

from typing import Any


class Array:
    def __init__(self, size: int, type) -> None:
        self.__type = type
        self.__size = size
        self.__array = [None for _ in range(size)]

    def update(self, index: int, value) -> None:
        if index < 0 or index > self.__size - 1:
            print('Invalid Index')
            return None
        if type(value) != self.__type:
            print('Invalid Type')
            return None

        self.__array[index] = value

    def search(self, value) -> bool:
        if value in self.__array:
            return True
        else:
            return False

    def get(self, index: int) -> Any:
        if index < 0 or index > self.__size - 1:
            print('Invalid Index')
            return

        return self.__array[index]

    def __len__(self) -> int:
        return len(self.__array)

    def get_elements(self) -> list:
        return self.__array


if __name__ == '__main__':
    array = Array(5, int)
    array.update(4, True)
    array.update(-1, 2)
    array.update(5, 2)
    array.update(0, 2)
    array.update(2, 3)
    print(array.search(5))
    print(array.search(2))
    print(array.get_elements())
