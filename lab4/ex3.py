class Matrix:
    def __init__(self, rows, collumns):
        self.rows = rows
        self.collumns = collumns
        self.matrix = [[0 for _ in range(collumns)] for _ in range(rows)]

    def get(self, row, collumn):
        if 0 <= row < self.rows and 0 <= collumn < self.collums:
            return self.matrix[row][collumn]
        else:
            print("This cell does not exist")
            return None

    def set(self, row, collumn, value):
        if 0 <= row < self.rows and 0 <= collumn < self.collumns:
            self.matrix[row][collumn] = value
        else:
            print("This cell does not exist")

    def transpose(self):
        transposed_matrix = Matrix(self.collumns, self.rows)
        for i in range(self.collumns):
            for j in range(self.rows):
                transposed_matrix.set(i, j, self.matrix[j][i])
        return transposed_matrix

    def multiply(self, other_matrix):
        if self.collumns != other_matrix.rows:
            print("Multiplication not possible")
            return None
        else:
            result = Matrix(self.rows, other_matrix.collumns)
            for i in range(self.rows):
                for j in range(other_matrix.collumns):
                    cell = 0
                    for k in range(self.collumns):
                        cell += self.matrix[i][k] * other_matrix.matrix[k][j]
                    result.set(i, j, cell)
            return result

    def apply_transform(self, function):
        for i in range(self.rows):
            for j in range(self.collumns):
                self.matrix[i][j] = function(self.matrix[i][j])

    def display(self):
        for row in self.matrix:
            print(row)

def main():

    matrix = Matrix(2, 3)

    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(0, 2, 3)
    matrix.set(1, 0, 4)
    matrix.set(1, 1, 5)
    matrix.set(1, 2, 6)

    print("Original Matrix:")
    matrix.display()

    transposed_matrix = matrix.transpose()

    print("\nTransposed Matrix:")
    transposed_matrix.display()

    other_matrix = Matrix(3, 2)
    other_matrix.set(0, 0, 7)
    other_matrix.set(0, 1, 8)
    other_matrix.set(1, 0, 9)
    other_matrix.set(1, 1, 10)
    other_matrix.set(2, 0, 11)
    other_matrix.set(2, 1, 12)

    result = matrix.multiply(other_matrix)
    if result:
        print("\nMatrix Multiplication Result:")
    result.display()

    matrix.apply_transform(lambda x: x * 2)
    print("\nMatrix after applying transformation:")
    matrix.display()

if __name__ == '__main__':
    main()

