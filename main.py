# ----------------------------------1-----------------------------


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.len1 = len(self.matrix)
        self.len2 = len(self.matrix[0])

    def __str__(self):
        result = ''
        for i in self.matrix:
            string = ''
            for j in i:
                string += str(j) + '\t'
            result += string.strip() + '\n'
        return result.strip()

    def __add__(self, other):
        if self.len1 == other.len1 and self.len2 == other.len2:
            result = []
            tmp = []
            for i in range(self.len1):
                for j in range(self.len2):
                    sum = self.matrix[i][j] + other.matrix[i][j]
                    tmp.append(sum)
                result.append(tmp)
                tmp = []
            return Matrix(result)
        else:
            return 'Разные матрицы'


my_matrix = Matrix([[5, 95, 47],
                    [3, 50, 29],
                    [2, 39, 5]])

print(str(my_matrix))

my_matrix2 = Matrix([[53, 85, 3],
                     [8, 12, 93],
                     [7, 17, 83]])

my_matrix3 = Matrix([[73, 4, 92],
                     [4, 54, 2],
                     [55, 2, 10]])

print(str(my_matrix + my_matrix2 + my_matrix3))


# ----------------------------------------2-----------------------------------------------

class Suit:
    def __init__(self, height):
        self.consumption = 2 * height + 0.3


class Coat:
    def __init__(self, size):
        self.consumption = size / 6.5 + 0.5


class Cloth:
    def __init__(self):
        self.consumption = []

    def add_suit(self, height):
        self.consumption.append(Suit(height))

    def add_coat(self, size):
        self.consumption.append(Coat(size))

    @property
    def cloth_consumption(self):
        result = 0
        for i in self.consumption:
            result += i.consumption
        return round(result)


cloth = Cloth()
cloth.add_coat(5)
cloth.add_suit(30)
print(cloth.cloth_consumption)


# ----------------------------------------3-------------------------------

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity >= other.quantity:
            return Cell(self.quantity - other.quantity)
        else:
            return print('Negative value')

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, row):
        result = ''
        for i in range(self.quantity // row):
            result += f'{"*" * row}\n'
        result += f'{"*" * (self.quantity % row)}'
        return result

    def __str__(self):
        return f'{"*" * self.quantity}'


cells1 = Cell(5)
cells2 = Cell(36)
print(cells1)
print(cells2)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells1 * cells2)
print(cells2.make_order(4))
print(cells1.make_order(11))
print(cells1 / cells2)
