"""
Stack is a LIFO - Last In First Out. It's similar to a stack of plates, the ones in top are the one to be removed first
"""

from typing import Any


class Stack:
    def __init__(self) -> None:
        self.__stack = []

    def push(self, value) -> None:
        self.__stack.insert(0, value)

    def pop(self) -> Any:
        if len(self.__stack) == 0:
            return None
        else:
            return self.__stack.pop(0)

    def peek(self) -> Any:
        if len(self.__stack) == 0:
            return None
        else:
            return self.__stack[0]

    def isEmpty(self) -> bool:
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def __len__(self) -> int:
        return len(self.__stack)


if __name__ == '__main__':
    stack = Stack()
    print(stack.isEmpty())
    stack.push(5)
    stack.push(2)
    stack.push(7)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
