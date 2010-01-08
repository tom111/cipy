"Python Classes for CIMatrices"
class CIMatrix(object):
    "A Conditional Independence Matrix, for easy adressing. Entries are strings"

    def __init__(self, d1=2, d2=2):
        self.rawlist = [ ["0" for i in range(d2)] for i in range(d1) ]
        self.dim2 = d2
        self.dim1 = d1


    def clear(self):
        rawlist = [ ["0" for i in range(self.dim2)] for i in range(self.dim1) ]

    def printRawList(self): print self.rawlist

    def printMatrix(self):
        for l in self.rawlist:
            print " ".join(l)

    def getRawList(self): return self.rawlist

    def getval(self, m,n): return self.rawlist[m][n]

    def setval(self, m,n, newval): self.rawlist[m][n]=newval
    
