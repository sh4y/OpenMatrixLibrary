# OpenMatrixLibrary
A (mostly!) self-contained open-source Python library of matrix, vector, and plane functions for a beginner's Linear Algebra course.

Example usage of Matrix functions:

#Creation of Matrix

Initialize Matrix of mxn dimensions:
>>> x = Matrix(2,2)
Add Rows Manually
>>> x.addRow([1,1])
>>> x.addRow([4,3])
>>> x.printMatrix()
>>> [[1,1], [4,3]]

#Modification of Matrix
>>> x = Matrix(2,2)
>>> y = Matrix(2,2)

>>> x.addRow([1,2])
>>> x.addRow([2,1])
>>> y.addRow([4,2])
>>> y.addRow([1,2])

Addition/Subtraction:

>>> x.addMatrix(y)
>>> x.printMatrix()
>>> [[5,4], [3,3]]

>>> x.subMatrix(x)
>>> x.printMatrix()
>>> [[0,0], [0,0]]

Scalar Multiplication:
>>> y.multiplyMatrixScalar(3)
>>> y.printMatrix()
>>> [[12,6], [3,6]]
