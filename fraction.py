from number import *


# ----------------------------------------------
class Fraction(Number):
    def __init__(self):
        self.a = 0
        self.b = 0

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.a = int(strArray[i])
        self.b = int(strArray[i + 1])
        if self.b == 0:
            print("Incorrect input values.\nDenominator must not be zero")
            exit(0)
        i += 2
        # print("Fraction: a = ", self.a, " b = ", self.b)
        return i

    def Print(self):
        print("Fraction: a = ", self.a, " b = ", self.b, ", Real = ", self.Real())
        pass

    def Write(self, ostream):
        ostream.write("Fraction: a = {}  b = {}, Real = {}".format \
                          (self.a, self.b, self.Real()))
        pass

    def Real(self):
        return self.a / self.b
        pass
