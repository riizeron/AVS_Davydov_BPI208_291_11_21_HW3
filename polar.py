from number import *


# ----------------------------------------------
class Polar(Number):
    def __init__(self):
        self.a = 0
        self.b = 0

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.a = int(strArray[i])
        self.b = int(strArray[i + 1])
        if self.a <= 0:
            print("Incorrect input values.\nRadial distance must be positive")
            exit(0)
        if self.b >= 360 or self.b < 0:
            print("Incorrect input values.\nAzimuth must be between 0 and 360 degrees")
            exit(0)
        i += 2
        # print("Polar: a = ", self.a, " b = ", self.b)
        return i

    def Print(self):
        print("Polar: a = ", self.a, " b = ", self.b, ", Real = ", self.Real())
        pass

    def Write(self, ostream):
        ostream.write("Fraction: a = {}  b = {}, Real = {}".format \
                          (self.a, self.b, self.Real()))
        pass

    def Real(self):
        return self.a
        pass
