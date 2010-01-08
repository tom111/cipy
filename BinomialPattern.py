"Module for binomial Patterns"

import CIMatrix
from CIutil import *

class BinomialPattern222k(object):
    "Store and work with Binomial Patterns in CI analysis"
    # Defining the data :
    def __init__ (self, d2):
        self.matrix = CIMatrix.CIMatrix(4,2*d2)
        self.dim2 = d2

    def __getIndex__ (self, s):
        """Turns a string like 2222 into an a row col index, correcting the off by one
        Input: s the string, kk the format invariant
        1 and 2 index the rows, 1 the big jump
        3 and 4 index the cols, 3 the big jump
        
        Format: 
        1111 1112  1121 1122   
        1211 1212  1221 1222
        
        2111 2112  2121 2122
        2211 2212  2221 2222
        """
        i = int(s[0])
        j = int(s[1])
        k = int(s[2])
        l = int(s[3])
        m = 2*(i-1) + (j-1) # Rowindex
        n = self.dim2*(k-1) + (l-1)# Colindex
        return (m,n)

    def printRaw (self): self.matrix.printRawList()

    def printAsMatrix (self): self.matrix.printMatrix()

    def fromBinomial (self, s):
        "Init from Binomial string in 1,2,... notation"
        ## Init zero
        self.matrix.clear()
    ## Find and remove divisors of the two binomials
        t = s.split("-")
        g = [m.split("*") for m in t]
        divisors = removeDup(g[0],g[1])
        for d in divisors:
            (m,n) = self.__getIndex__ (d)
            self.matrix.setval(m,n,"*")
        for l in g[0]:
            # for each positive term
            (m,n) = self.__getIndex__ (l)
            self.matrix.setval(m,n,"+")
        for l in g[1]:
            (m,n) = self.__getIndex__ (l)
            self.matrix.setval(m,n,"-")

    def invertPattern (self):
        "Inverts the saved pattern"
        for i in range(4):
            for j in range(2*self.dim2):
                if self.matrix.getval(i,j) == "-": self.matrix.setval(i,j,"+")
                else:
                    if self.matrix.getval(i,j) == "+": self.matrix.setval(i,j,"-")

    def fixTermOrder (self):
        "Fixes the pattern such that the last entry is a -"
        l = flatten(self.matrix.getRawList())
        l.reverse()
        if l.index("+") < l.index("-"):
            ### Pattern is wrong
            self.invertPattern()

    def getString (self):
        """return string representing the pattern.
        Warning: * will not have powers !
        """
        pass
            
    def Spair (self, p2):
        def combi(e1,e2):
            # TODO: We need to handle -2 and alike
            if e1=="0":
                if e2=="-": return "+"
                if e2=="+": return "-"
                if e2=="*": return "*"
            if e2=="0": return e1;
            if e1=="+" and e2=="+": return "0";
            if e1=="+" and e2=="-": return "2";
            if e1=="-" and e2=="+": return "-2";
            if e1=="-" and e2=="-": return "*";

        spair = BinomialPattern222k(self.dim2)
            
        "Forms an S-pair of the current pattern and p2"
        for i in range(4):
            for j in range(2*self.dim2):
                spair.matrix.setval(i,j,combi(self.matrix.getval(i,j), p2.matrix.getval(i,j)))
                
        return spair
