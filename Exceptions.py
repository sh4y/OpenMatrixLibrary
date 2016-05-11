class IllegalDimensionSize(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class IllegalMatrix(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class IllegalPlane(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

