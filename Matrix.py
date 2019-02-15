from Exceptions import *
from scipy import misc, ndimage, stats
from skimage import data, feature
import skimage as sk
import matplotlib.pyplot as plt

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

    import numpy as np

def convolution_1d(matrix, filter):
    filtered_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]-1):
            sum = 0
            for i in range (filter.shape[0]):
                for j in range (filter.shape[1]):
                    sum += matrix[x][y+j] * filter[i][j]
            filtered_matrix[x][y] = sum
            if y == matrix.shape[1] - 2:
                filtered_matrix[x][y+1] = matrix[x][y+1]
    return filtered_matrix


def convolution(matrix, filter):
    #flip filter
    filter = np.flip(filter, axis=0)
    filter = np.flip(filter, axis=1)
    print filter.shape
    print matrix.shape

    if filter.shape[1] % 2 == 0:
        return convolution_1d(matrix, filter)

    #gather shape/dimensions
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    #first zero pad the matrix, but only if filter is of odd length
    start_index = 0 # by default, non padded matrices will start at 0,0
    col_end_index = cols  # same logic for end index
    row_end_index = rows
    if filter.shape[0] % 2 == 1:
        matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=0)
        start_index = 1 # if zero padded, then start index is going to be 1,1
        col_end_index += 1
        row_end_index += 1
    filtered_matrix = np.zeros((rows, cols))
    for x in range (start_index, col_end_index):
        for y in range (start_index, row_end_index):
            #calculate filter math
            sum = 0
            for i in range(filter.shape[0]):
                for j in range(filter.shape[1]):
                    #print 'Matrix value: ' + str(matrix[x-i+start_index][y+j-1])
                    #print 'filter value: ' + str(filter[i][j])
                    sum += np.multiply(matrix[x-i+start_index][y+j-1],filter[i][j])
            filtered_matrix[x-start_index][y-start_index] = sum
    return filtered_matrix

def convolution_3d(matrix, filter):
    filtered_matrix = np.ones((matrix.shape[0], matrix.shape[1]))
    for i in range(matrix.shape[2]):
        #strip each matrix and filter channel
        channel = matrix[:, :, i]
        channel_filter = filter[:, :, i]
        #perform convolution for each channel
        filtered_channel = convolution(channel, channel_filter)
        filtered_matrix = np.multiply(filtered_matrix, filtered_channel)
    return filtered_matrix
