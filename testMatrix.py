from array_m import Array, Array2D
from matrix import Matrix
def main():
    m1 = Matrix(3,2)
    m2 = Matrix(3,2)
        
    m1.clear(2)
    m2.clear(3)
    m3 = m1.__add__(m2)
    m3 = m1.__sub__(m2)
    print(type(m1))
    print(type(m1._theGrid))
    m3._theGrid.printArray2D()
    
    mulTest1 = Matrix(3,2)
    mulTest2 = Matrix(2,3)
    
    mulTest1.__setitem__([0,0], 0)
    mulTest1.__setitem__([0,1], 1)
    mulTest1.__setitem__([1,0], 2)
    mulTest1.__setitem__([1,1], 3)
    mulTest1.__setitem__([2,0], 4)
    mulTest1.__setitem__([2,1], 5)
    mulTest1._theGrid.printArray2D()
    
    mulTest2.__setitem__([0,0], 6)
    mulTest2.__setitem__([0,1], 7)
    mulTest2.__setitem__([0,2], 8)
    mulTest2.__setitem__([1,0], 9)
    mulTest2.__setitem__([1,1], 1)
    mulTest2.__setitem__([1,2], 0)
    mulTest2._theGrid.printArray2D()
    
    mulTestRes = mulTest1.__mul__(mulTest2)
    mulTestRes._theGrid.printArray2D()
    mT = mulTestRes.tranpose()
    mT._theGrid.printArray2D()
    '''
    a1 = Array2D(2,3)
    a1.clear(2)
    a1.__getitem__([1,1])
    print(type(a1))
    print(str(a1.__getitem__([1,1])))
    a1.printArray2D()
    '''
main()