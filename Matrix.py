class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix


    #Help function for reference
    def help(self):

        functions = [
            ("add(matrix2)", "Adds two matrices element by element. Both must be same size."),
            ("subtract(matrix2)", "Subtracts matrix2 from current matrix element by element. Both must be same size."),
            ("multiply(matrix2)", "Multiplies two matrices. Columns of first must equal rows of second."),
            ("transpose()", "Flips matrix over its diagonal. Rows become columns."),
            ("determinant()", "Returns the determinant of a square matrix. Works recursively."),
            ("trace()", "Returns sum of diagonal elements of a square matrix."),
            ("char_eqn()", "Prints the characteristic equation: λ² - trace·λ + det = 0"),
        ]

        for name, description in functions:
            print(f"{name} : {description}")


    #Returns the summation of two matrices
    def add(self, matrix2):
        summation = []
        for i in range(len(self.matrix)):
            new_list = []
            for j in range(len(self.matrix[i])):
                element = self.matrix[i][j] + matrix2[i][j]
                new_list.append(element)
            summation.append(new_list)

        return summation

    #Returns the subtraction of two matrices
    def subtract(self, matrix2):
        difference = []
        for i in range(len(self.matrix)):
            new_list = []
            for j in range(len(self.matrix[i])):
                element = self.matrix[i][j] - matrix2[i][j]
                new_list.append(element)
            difference.append(new_list)

        return difference

    #Multiplication of two different matrices
    def multiply(self, matrix2):

        result = []
        for i in range(len(self.matrix)):
            new_list = []
            for j in range(len(matrix2[0])):
                element = 0
                for k in range(len(matrix2)):
                    element += self.matrix[i][k] * matrix2[k][j]
                new_list.append(element)
            result.append(new_list)

        return result

    #Return the transpose of a given matrix
    def transpose(self):

        transposed = []
        for i in range(len(self.matrix[0])):
            new_list = []
            for j in range(len(self.matrix)):
                element = self.matrix[j][i]
                new_list.append(element)
            transposed.append(new_list)

        return transposed

    #Return the determinant of the given matrix
    def determinant(self):

        matrix = self.matrix
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        det = 0
        for j in range(len(matrix[0])):
            sub = []
            for i in range(1, len(matrix)):
                new_list = []
                for k in range(len(matrix[0])):
                    if k != j:
                        new_list.append(matrix[i][k])
                sub.append(new_list)
            element = matrix[0][j] * ((-1) ** j)
            det += element * self.__class__(sub).determinant()
        return det

    #Returns the trace of the matrix, i.e. the summation of diagonal elements
    def trace(self):
        trace = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if i == j:
                    trace += self.matrix[i][j]

        return trace

    #Characteristic Equation of the matrix
    def char_eqn(self):
        t = self.trace()
        d = self.determinant()
        return f'λ² - {t}λ + {d}'