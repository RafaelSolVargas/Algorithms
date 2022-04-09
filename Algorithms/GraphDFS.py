# Graph Traversal é um algoritmo que visita todos os vértices de um gráfico, a intuição aqui é ir explorando os vértices conforme vão aparecendo,
# e quando chegarmos em um deadend, um vértice que não possua nenhum outro vértice não explorado, começamos a retornar o caminho feito até chegar em algum
# vértice que possa outros vértices exploráveis

from typing import List
from DataStructures.Stack import Stack


class Connection:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end


class Node:
    def __init__(self, value, index, connections: list) -> None:
        self.value = value
        self.index = index
        self.marked = False

        self.connections: List[Connection] = self.__build_connections(connections)

    def __build_connections(self, connections: list) -> list:
        newList = []
        for end_index, end_status in enumerate(connections):
            if end_status == 1:
                newList.append(Connection(self.index, end_index))

        return newList


class GraphDFS:
    def __init__(self, nodes_conn: list) -> None:
        self.__graph: List[Node] = self.__build_nodes(nodes_conn)

    def __build_nodes(self, nodes_conn: list) -> list:
        nodes = []
        index = 0
        for value, connections in nodes_conn:
            nodes.append(Node(value, index, connections))
            index += 1
        return nodes

    def search_dfs(self, start: int) -> list:
        self.__stack_dfs(start)

    def __simple_dfs(self, node_index: int) -> None:
        node = self.__graph[node_index]
        node.marked = True
        print(node.value) # For preorder

        for connection in node.connections:
            neighbor_node = self.__graph[connection.end]
            if not neighbor_node.marked:
                self.__dfs(connection.end)
        # print(node.value) # For PostOrder
        print(f'Ending {node.value} Call')

    def __stack_dfs(self, node_index: int) -> None:
        stack = Stack()
        start_node = self.__graph[node_index]
        stack.push(start_node)

        while len(stack) > 0:
            node: Node = stack.pop()
            if not node.marked:
                print(node.value) # Preorder
                node.marked = True
                for connection in node.connections:
                    neighbor_node = self.__graph[connection.end]
                    if not neighbor_node.marked:
                        stack.push(neighbor_node)
                # print(node.value) # PostOrder


if __name__ == '__main__':
    connections = [
        ('A', [1, 0, 1, 1, 0, 0, 0, 0, 1, 0]),
        ('B', [1, 0, 0, 1, 1, 0, 0, 0, 1, 0]),
        ('C', [1, 0, 0, 1, 0, 1, 0, 1, 1, 0]),
        ('D', [1, 1, 0, 1, 0, 0, 0, 0, 1, 0]),
        ('E', [1, 0, 0, 1, 0, 0, 1, 0, 1, 0]),
        ('F', [1, 0, 1, 1, 0, 0, 0, 1, 1, 1]),
        ('G', [1, 0, 0, 1, 0, 0, 1, 0, 1, 0]),
        ('H', [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]),
        ('I', [1, 0, 0, 1, 1, 0, 0, 0, 1, 0]),
        ('J', [1, 0, 0, 1, 0, 0, 0, 0, 1, 0]),
    ]

    dfs = GraphDFS(connections)
    dfs.search_dfs(8)
