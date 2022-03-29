class FenwickTree:
    def __init__(self, m, n) -> None:
        self.max_x = m+1
        self.max_y = n+1
        # Plus one to use index start at 1
        self.matriz = [[0 for _ in range(n+1)] for _ in range(m+1)]

    def get_parent(self, index) -> int:
        """Return the parent of index in a Fenwick tree"""
        index -= index & (-index)
        return index

    def get_next(self, index) -> int:
        """Return the next node of a index in a Fenwick tree"""
        index += index & (-index)
        return index

    def update(self, x, y, value) -> None:
        """Update all the fenwick tree with one value"""
        # Add x and y to use index start at 1
        x += 1
        y += 1
        while x < self.max_x:
            y2 = y

            while y2 < self.max_y:
                self.matriz[x][y2] += value
                y2 = self.get_next(y2)

            x = self.get_next(x)

    def getSum(self, x, y) -> int:
        """Get the sum from all values from the 0, 0 to the coordinate x, y"""
        if x <= 0 or y <= 0:
            return 0

        soma = 0

        while x > 0:
            y2 = y
            while y2 > 0:
                soma += self.matriz[x][y2]
                y2 = self.get_parent(y2)

            x = self.get_parent(x)

        return soma

    def getSumRect(self, x1, y1, x2, y2) -> int:
        """Get the sum of all values in the area between the coordinates x1, y1 to x2, y2"""
        # Update all numbers to work with index of 1
        x1 += 1
        x2 += 1
        y1 += 1
        y2 += 1
        sum = self.getSum(x2, y2) + self.getSum(x1-1, y1-1) - \
            self.getSum(x2, y1-1) - self.getSum(x1-1, y2)
        return sum


if __name__ == '__main__':
    while True:
        comprimento, largura, preco = list(map(int, input().split()))

        if comprimento == largura == preco == 0:
            break

        quant_mensagens = int(input())

        fenwick = FenwickTree(comprimento, largura)

        for mensagem in range(quant_mensagens):
            entrada = input().split()

            if entrada[0] == 'A':
                x = int(entrada[2])
                y = int(entrada[3])
                quant = int(entrada[1])

                fenwick.update(x, y, quant)
            else:
                a = int(entrada[1])
                b = int(entrada[2])
                c = int(entrada[3])
                d = int(entrada[4])

                if a > c:
                    a, c = c, a
                if b > d:
                    b, d = d, b

                soma = fenwick.getSumRect(a, b, c, d)

                print(soma * preco)
        print()
