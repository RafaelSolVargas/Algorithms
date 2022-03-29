class Connection():
    """
    Deal with the connection that between two nodes.
    It  stores index of the origin and destiny nodes and value of the connection
    """

    def __init__(self, origin: int, destiny: int, value: int) -> None:
        self.origin = origin
        self.destiny = destiny
        self.value = value


class Node:
    """
    The Node himself, it store the smaller distance known to him and the previous Node that lead to him.
    It stores too if he get visited already and the connection objects that leave from the node
    """

    def __init__(self, index: int, connections: list) -> None:
        self.distance = None
        self.prevNode = None
        self.visited = False
        self.index = index
        self.connections = []

        for index, value in enumerate(connections):
            if value > 0:
                connection = Connection(origin=self.index, destiny=index, value=value)
                self.connections.append(connection)


class Dijkstra:
    """
    Dijkstra class, it receives a matrix informing the connections between all nodes of the system
    """

    def __init__(self, graph: list) -> None:
        self.node_quant = len(graph)
        self.nodes = []

        for index, connections in enumerate(graph):
            self.nodes.append(Node(index, connections))

    def searchAll(self, source: int) -> None:
        if source >= self.node_quant:
            return None

        firstNode = self.nodes[source]
        firstNode.distance = 0

        # Loop to visit all nodes
        for _ in range(self.node_quant):
            node = self.__getClosestNode()
            # If there is no more reachable node
            if node == None:
                break

            node.visited = True
            # For each connection of the node, update the distance for the other node
            for connection in node.connections:
                otherNode = self.nodes[connection.destiny]
                newDistance = node.distance + connection.value

                if otherNode.visited == False:
                    if otherNode.distance == None or newDistance < otherNode.distance:
                        otherNode.distance = newDistance
                        otherNode.prevNode = node

        self.__printResult(source)
        self.__reset()

    def searchPath(self, source: int, destiny: int) -> list:
        if source >= self.node_quant or destiny >= self.node_quant:
            return None

        firstNode = self.nodes[source]
        firstNode.distance = 0
        path = []

        # Loop to visit all nodes
        for _ in range(self.node_quant):
            node = self.__getClosestNode()
            # If there is no more reachable node
            if node == None:
                break

            node.visited = True
            # If the closest node is the destiny, the search is complete
            if node.index == destiny:
                path = self.__getRevertPath(firstNode, node)
                break

            # For each connection of the node, update the distance for the other node
            for connection in node.connections:
                otherNode = self.nodes[connection.destiny]
                newDistance = node.distance + connection.value

                if otherNode.visited == False:
                    if otherNode.distance == None or newDistance < otherNode.distance:
                        # print(
                        #    f'Atualizando Prev do Node {otherNode.index} para o Node {node.index}')

                        otherNode.distance = newDistance
                        otherNode.prevNode = node

        self.__reset()  # Reset the nodes of the graph
        return path  # Return the node paths to get to destiny

    def __reset(self):
        # Reset the nodes
        for node in self.nodes:
            node.visited = False
            node.distance = None
            node.prevNode = None

    def __getClosestNode(self):
        closestNode = None
        smallerDistance = None

        for node in self.nodes:
            # If the distance is known and node is not visited yet
            if node.distance != None and node.visited == False:
                # Att the closestNode
                if smallerDistance == None or node.distance < smallerDistance:
                    smallerDistance = node.distance
                    closestNode = node

        return closestNode

    def __printResult(self, source):
        print(f'Distance from node {source} to:')
        for node in self.nodes:
            print(f'{node.index} - distance: {node.distance}')

    def __getRevertPath(self, originNode: Node, destinyNode: Node) -> list:
        """Return the path to get from originNode to destinyNode"""
        path = []
        node = destinyNode
        # Return the prev node until gets to the first, the only that doesn't has prev
        while node != originNode:
            path.insert(-1, node.index)
            node = node.prevNode

        return path


if __name__ == '__main__':
    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]

    djk2 = Dijkstra(graph)
    for x in range(len(graph)):
        djk2.searchAll(x)

    for x in range(len(graph)):
        for y in range(len(graph)):
            djk2.searchPath(x, y)
