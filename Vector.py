from Exceptions import *

class Vector:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '[{self.x},{self.y},{self.z}]'.format(self=self)
    
    def getMatrix(self):
        return [self.x, self.y, self.z]
        
    #validates 3d vector
    def validatePoint(self, p):
        return (len(p) == 3)

    #creates 3d vector given two points
    def createVector(self, p1, p2):
        if not (self.validatePoint(p1) and self.validatePoint(p2)):
            raise IllegalDimensionSize("One of the two vectors is not 3D!")
        self.x = p2[0] - p1[0]
        self.y = p2[1] - p1[1]
        self.z = p2[2] - p1[2]

    @staticmethod
    def dotProduct(v, w):
        "Computes the dot product of two 3D vectors."
        return (v[0]*w[0] + v[1]*w[1] + v[2]*w[2])

    @staticmethod
    def crossProduct(v, w):
        a = []
        #i   j   k
        #v1  v2  v3
        #w1  w2  w3
        
        #v2*w3 - v3*w2
        a.append(v[1]*w[2] - v[2]*w[1])
        #v1*w3 - v3*w1
        a.append(v[0]*w[2] - v[2]*w[0])
        #v1*w2 - w1*v2
        a.append(v[0]*w[1] - v[1]*w[0])
        return a
