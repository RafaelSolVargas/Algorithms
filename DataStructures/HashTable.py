"""
HashTable is a data structure that store values which have keys associated with each of them. It supports lookup efficiently if we know the key associated with the value.
If we use direct addressing, the main problem will be the size of the structure, depending on the size of key value pairs.
To overcome this problem we use hash tables that has a hash function associated. With this approach we calculate the index to the table to witch values are stored. 
The value calculated using the hash functions for a given key is called the hash value which indicates the index of the table to which the value is mapped

In this example the hash function used are calculating the sum of the unicode of each character in the key, then getting the rest of division of this by the max size of dictionary.
The insertion and deletion of values in HashTable is O(1) if we known the key.
The main problem in HashTable is collisions, it's when the hash function return the same value for two different keys
"""

from typing import Any


class HashTable:
    def __init__(self, size: int) -> None:
        self.__size = size
        self.__arr = [None for _ in range(self.__size)]

    def __setitem__(self, key: str, value: Any) -> None:
        hash_key = self.__get_hash(key)
        self.__arr[hash_key] = value

    def __getitem__(self, key) -> Any:
        hash_key = self.__get_hash(key)
        return self.__arr[hash_key]

    def __delitem__(self, key) -> None:
        hash_key = self.__get_hash(key)
        self.__arr[hash_key] = None

    def __get_hash(self, key: str) -> str:
        x = 0
        for char in key:
            code = ord(char)
            x += code
        return x % self.__size


if __name__ == '__main__':
    table = HashTable(10)
    table['Rafael'] = 52
    table['Gabriel'] = 55
    print(table['Rafael'])
    print(table['Gabriel'])
    del table['Gabriel']
    print(table['Gabriel'])
