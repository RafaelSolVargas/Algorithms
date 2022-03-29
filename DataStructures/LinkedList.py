"""
Linked Lists is a sequential structure that consists of a sequence of items in linear order which are linked to each other. Each value is known as a Node, where they have their own value and a pointer to the next node.
There are 3 types Insertion Operations:
- At the start: Complexity of O(1)
- At the middle: Complexity of O(1)
- At the end: Complexity of O(n) 
Traversal and Access Elements is also O(n)

You doesn't need to pre allocate space, the linked list could be fully spread in the memory and still works. Insertion is more faster

In Double Linked List the Nodes has also an pointer to the prev Node
"""


class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.__head: Node = None

    def insert_at_start(self, value) -> None:
        node = Node(value, self.__head)
        self.__head = node

    def insert_at_end(self, value) -> None:
        if self.__head is None:
            self.__head = Node(value, None)
            return

        current = self.__head
        while current.next:
            current = current.next

        current.next = Node(value, None)

    def printList(self):
        if self.__head is None:
            print('Linked List is Empty')
            return

        current = self.__head
        list_str = ''
        while current:
            list_str += f'{current.value} -> '
            current = current.next
        list_str += f'None'
        print(list_str)

    def insert_values(self, values_list: list) -> None:
        self.__head = None
        for value in values_list:
            self.insert_at_end(value)

    def __len__(self) -> int:
        count = 0
        current = self.__head
        while current:
            count += 1
            current = current.next
        return count

    def remove_at(self, index: int) -> None:
        if index < 0 or index > len(self):
            print('Invalid Index')
            return

        if index == 0:
            self.__head = self.__head.next
            return

        count = 0
        current = self.__head
        while current:
            if count == index - 1:
                current.next = current.next.next
                break

            count += 1
            current = current.next

    def insert_at(self, value, index: int) -> None:
        if index < 0 or index > len(self):
            print('Invalid Index')
            return

        if index == 0:
            self.insert_at_start(value)
            return

        count = 0
        current = self.__head
        while current:
            if count == index - 1:
                node = Node(value, current.next)
                current.next = node
                break
            count += 1
            current = current.next

    def insert_after_value(self, value, new_value) -> None:
        current = self.__head
        while current:
            if current.value == value:
                node = Node(new_value, current.next)
                current.next = node
                break

            current = current.next


if __name__ == '__main__':
    list = LinkedList()
    list.printList()
    list.insert_at_start(5)
    list.insert_at_start(4)
    list.insert_at_end(8)
    list.insert_at_start(2)
    list.insert_at_start(2)
    list.remove_at(2)
    list.insert_at(15, 0)
    list.insert_at(16, 2)
    list.insert_at(17, 6)
    list.insert_after_value(18, 50)
    list.printList()
    print(len(list))
