import math

from number import *


# ----------------------------------------------
class Complex(Number):
    def __init__(self):
        self.x = 0
        self.y = 0

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.x = int(strArray[i])
        self.y = int(strArray[i + 1])
        i += 2
        # print("Complex: x = ", self.x, " y = ", self.y)
        return i

    def Print(self):
        print("Complex: x = ", self.x, " y = ", self.y, ", Real = ", self.Real())
        pass

    def Write(self, ostream):
        ostream.write("Complex: x = {}  y = {}, Real = {}".format(self.x, self.y, self.Real()))
        pass

    def Real(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
        pass
