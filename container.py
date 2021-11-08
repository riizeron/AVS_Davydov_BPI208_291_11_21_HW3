# ----------------------------------------------
class Container:
    def __init__(self):
        self.store = []

    # def ReadStrArray(self, strArray):

    def Print(self):
        print("Container is store", len(self.store), "numbers:")
        for number in self.store:
            number.Print()
        print("RealAverage  = ", self.RealAverage())
        pass

    def Write(self, ostream):
        ostream.write("Container is store {} numbers:\n".format(len(self.store)))
        for number in self.store:
            number.Write(ostream)
            ostream.write("\n")
        ostream.write("RealAverage  = {}\n".format(self.RealAverage()))
        pass

    def RealAverage(self):
        summ = 0.0
        for number in self.store:
            summ += number.Real()
        return summ / len(self.store)

    def DeleteLowerThenAverage(self):
        aver = self.RealAverage()
        for number in self.store:
            if number.Real() < aver:
                self.store.remove(number)
