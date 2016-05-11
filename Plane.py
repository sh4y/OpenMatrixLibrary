from Exceptions import *
from Vector import *
from Matrix import *

class Plane:
    def __init__(self, x=None, y=None, z=None, d=None):
        self.x = x
        self.y = y
        self.z = z
        self.d = d
        self.normal = [x, y, z]
        
    def __str__(self):
        return '({self.x}x) + ({self.y}y) + ({self.z}z) = {self.d}'.format(self=self)

    def getNormal(self):
        if len(self.normal) > 0:
            return self.normal
        else:
            raise IllegalPlane("Plane is empty!")
    
    #creates planes given three points
    def createPlaneWithPoints(self, p1, p2, p3):
        v = Vector()
        w = Vector()

        #create vectors given points
        v.createVector(p1,p2)
        w.createVector(p1,p3)

        #retrieve matrices from vectors and call xproduct method
        self.normal = Vector.crossProduct(v.getMatrix(), w.getMatrix())

        #store normal coords into vars
        self.x = self.normal[0]
        self.y = self.normal[1]
        self.z = self.normal[2]

        #calculate d value given normal and one point
        self.d = self.x*p1[0] + self.y*p1[1] + self.z*p1[2]

        print(self)

    def createPlaneWithNormal(self, n, p):
        #store normal coords into vars
        self.x = n[0]
        self.y = n[1]
        self.z = n[2]

        self.normal = n
        
        #calculate d value given normal and one point
        self.d = self.x*p[0] + self.y*p[1] + self.z*p[2]

        print(self)

    def isParallel(self, p):
        a = p.getNormal()
        b = self.getNormal()

        if (b[0] >= a[0]):
            c = b[0] % a[0]
            for x in range(0, 2):
                if (b[x] % a[x] != c):
                    return False
        else:
            c = a[0] % b[0]
            for x in range(0, 2):
                if (a[x] % b[x] != c):
                    return False

        return True

    def isOrthogonal(self, p):
        "Returns true if p is orthogonal to active plane."
        return Vector.dotProduct(self.normal, p.getNormal()) == 0

