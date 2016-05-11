from Exceptions import *
class Matrix:
    def __init__(self, row, col):
        "Initialization of Matrix type."
        self.r = row
        self.c = col
        self.matrix = [];
        
    def validMatrix(self, m):
        return len(m.matrix) == self.r

    def addRow(self, row):
        "Adds a row to currently active matrix."
        if (len(row) == self.c):
            if (len(self.matrix) < self.r):
                self.matrix.append(row);
            else:
                print("Matrix bounds exceeded/not met.");
        else:
            print("Row Bounds exceeded/not met.");
    
    def printMatrix(self):
        print(self.matrix);

    def modMatrix(self, m, var):
        if not (self.validMatrix(self) and self.validMatrix(m)):
            raise IllegalMatrix("Illegal Matrix detected.");
        if (m.r != self.r) and (m.c != self.c):
            raise IllegalDimensionSize("Cannot add different size matrices.");
        for r in range(0, self.r):
            for c in range(0, self.c):
                if var == "add":
                    self.matrix[r][c] += m.matrix[r][c];
                elif var == "sub":
                    self.matrix[r][c] -= m.matrix[r][c];
                else:
                    self.matrix[r][c] = self.matrix[r][c] * var;
    def addMatrix(self, m):
        self.modMatrix(m, "add");
        
    def subMatrix(self, m):
        self.modMatrix(m, "sub");

    def multiplyMatrixScalar(self, n):
        self.modMatrix(self, n);

    def determinantWrapper(self, m):
        "Recursively calculates the determinant of an NxN matrix."
        n = self.c;
        #static base case
        if (n == 2):
            return self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0];
        else:
            total = 0 
            #block off columns
            for i in range(0, self.c):
                #matrix coeffecient
                cf = self.matrix[0][i];
                inner = Matrix(self.r-1, self.c-1)
                #iterate through rows
                R = 0
                r = 0
                for R in range(0, self.r):
                    row = []
                    for r in range(0, self.c):
                        #if the current row element is not in the blocked column
                        if r != i and R != 0:
                            row.append(self.matrix[R][r])
                    if len(row) > 0:
                        inner.addRow(row)
                #recursive call
                temp = cf * inner.determinantWrapper(inner)
                if (i % 2) == 0:
                    total = total + temp
                else:
                    total = total - temp
            return total    
        
    def determinant(self):
        if (self.c != self.r):
            raise IllegalDimensionSize("Cannot get determinant of non NxN matrix.");
        print(self.determinantWrapper(self.matrix));
            
    def isSingular(self):
        if (self.c != self.r):
            raise IllegalDimensionSize("Cannot get determinant of non NxN matrix.");
        print(self.determinantWrapper(self.matrix) == 0);

    
