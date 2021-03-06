"Python Classes for CIMatrices"

class NotReducibleError(Exception):
    pass

#####################################

class CIMatrixEntry(object):
    "Abstraction of the 0,+,-,* thing"
    def __init__(self, s):
        "s is a string representation of the entry"
        self.s = s
        if s == "*" : self.star=True
        else: self.star=False

    def __add__ (self, other):
        """addition - corresponds to Spair formation
           This is abuse of notation since it feels more like subtraction !!!
           Example:
           * + * = *
           - + - = *
           + + + = 0
           0 + x = x
           """
        if self.star:
            if other.star:
                return CIMatrixEntry("*")
            j = int(other.s)
            if abs(j) > 1: raise NotImplementedError # Is 'higher star arithmetic' necessary?
            if j == 0: return CIMatrixEntry("*")
            else: return CIMatrixEntry (str(-j))
        else:
            if other.star:
                i = int(self.s)
                if abs(i) > 1: raise NotImplementedError
                if i == 0: return CIMatrixEntry("*")
                else: return CIMatrixEntry(str(-i))
            else:
                # Regular Integers
                i = int(self.s)
                j = int(other.s)
                k = i - j
                if (k==0 and i<0):
                    return CIMatrixEntry("*")
                else:
                    return CIMatrixEntry(str(k))
                
    def __sub__ (self, other):
        """ subtraction - corresponds to reduction of moves
        Raises NotReducibleError if not reducible
        """
        if self.star: # Self is a star
            if other.star: return CIMatrixEntry("*")
            else :
                j = int(other.s)
                if j == 0 : return CIMatrixEntry("*")
                else : return CIMatrixEntry(str(-j))
        else: # self.s is an integer
            i = int(self.s)
            if other.star:
                if i == 0: return CIMatrixEntry("*")
                else : return CIMatrixEntry(str(i))
            else: # Both are integer
                j = int(other.s)
                k = i-j
                if k < 0:
                    if j <= 0 : return CIMatrixEntry(str(k))
                    else :
                        raise NotReducibleError
                if k == 0:
                    if i >= 0 : return CIMatrixEntry("0")
                    else :
                        return CIMatrixEntry("*")
                if k > 0 :
                    return CIMatrixEntry(str(k))

    def __neg__ (self):
        """ Inversion, + -> -, - > +, everything else stays the same """
        if self.star: return self
        return CIMatrixEntry(str(-int(self.s)))

    def __eq__ (self, other):
        if self.s == other.s : return True
        else: return False

    def __neq__(self, other):
        if self==other: return False
        else: return True
    
    def __repr__(self):
        if self.s=="0": return "0"
        if self.star: return "*"
        i = int(self.s)
        if abs (i) >= 2: return str(i)
        if i > 0: return "+"
        else : return "-"
        

####### END CIMATRIXENTRY ################


##########################################

class CIMatrix(object):
    "A Conditional Independence Matrix, for easy adressing. Entries are strings"

    def __init__(self, d1=2, d2=2):
        self.rawlist = [ [CIMatrixEntry("0") for i in range(d2)] for i in range(d1) ]
        self.dim2 = d2
        self.dim1 = d1

    def clear(self):
        rawlist = [ [CIMatrixEntry("0") for i in range(self.dim2)] for i in range(self.dim1) ]

    def printRawList(self): print self.rawlist

    def printMatrix(self):
        for l in self.rawlist:
            print " ".join([str(ll) for ll in l])

    def getRawList(self): return self.rawlist

    def getval(self, m,n): return self.rawlist[m][n]

    def setval(self, m,n, newval): self.rawlist[m][n]=newval
    
####### END CIMATRIX ############
