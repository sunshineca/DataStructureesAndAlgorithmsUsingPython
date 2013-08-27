from array_m import Array2D
class Matrix:
    # create a matrix of size numRows * sumCols initialized to 0
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)
        #print(type(self._theGrid))
        # print the matrix
        # self._theGrid.printArray2D()

    def numRows(self):
        return self._theGrid.numRows()

    def numCols(self):
        return self._theGrid.numCols()

    def __getitem__(self, ndxTuple):
        return self._theGrid.__getitem__(ndxTuple)

    def __setitem__(self, ndxTuple, scalar):
        return self._theGrid.__setitem__(ndxTuple, scalar)

    def clear(self, value):
        self._theGrid.clear(value)

    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= scalar

    def tranpose(self):
        newMatrix = Matrix(self.numCols(), self.numRows())
        for r in range(self.numCols()):
            for c in range(self.numRows()):
                newMatrix[r,c] = self[c,r]
        return newMatrix
                
                
    def __add__(self, rhsMatrix):
        numRows = self.numRows()
        numCols = self.numCols()
        assert rhsMatrix.numRows() == numRows and \
                rhsMatrix.numCols() == numCols, \
                "Matrix sizes not compatible for the add operation"
        newMatrix = Matrix(numRows, numCols)
        for r in range(numRows):
            for c in range(numCols):
                newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]
        return newMatrix

    def __sub__(self, rhsMatrix):
        numRows = self.numRows()
        numCols = self.numCols()
        assert rhsMatrix.numRows() == numRows and \
                rhsMatrix.numCols() == numCols, \
                "Matrix sizes not compatible for the add operation"
        newMatrix = Matrix(numRows, numCols)
        for r in range(numRows):
            for c in range(numCols):
                newMatrix[r, c] = self[r, c] - rhsMatrix[r, c]
        return newMatrix

    def __mul__(self, rhsMatrix):
        #print(str(self.numRows()))
        #print(str(self.numCols()))
        assert self.numCols() ==  rhsMatrix.numRows(), \
                "Matrix sizes not compatible for the add operation"
        newMatrix = Matrix(self.numRows(),rhsMatrix.numCols())
        for r in range(self.numRows()):
            for c in range(rhsMatrix.numCols()):
                i = 0
                newMatrix[r,c]=0
                while i < self.numCols():
                    newMatrix[r,c] += self[r,i]*rhsMatrix[i,c]
                    i = i+1
        return newMatrix
