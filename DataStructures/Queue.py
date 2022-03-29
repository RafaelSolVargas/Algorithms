"""
Queue is a FIFO - First In First Out. It's similar to a real world queue of people
"""

from typing import Any


class Queue:
    def __init__(self) -> None:
        self.__queue = []

    def enqueue(self, value) -> None:
        self.__queue.append(value)

    def dequeue(self) -> Any:
        if len(self.__queue) == 0:
            return None
        else:
            return self.__queue.pop(0)

    def isEmpty(self) -> bool:
        if len(self.__queue) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    queue = Queue()
    print(queue.isEmpty())
    queue.enqueue(5)
    queue.enqueue(2)
    queue.enqueue(7)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
