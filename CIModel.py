""" Module for CI Models
  Data:
    N -> Number of variables of the model
    cards -> List of cardinialities of random variables state spaces
    Statements -> List of CI Statements which are triples.

  Methods:
    All sorts of generation of Macaulay2 code
    -> Ideal
    -> Ring

  The convention for this module is to use variable names pijkl ... with no subscripts.
"""

from multigradedRing import multigradedRing as mR
import numpy

class CIModel(object):

    def __product__ (self, liste):
        """ Multiply over a list """
        re = 1;
        for i in liste: re *= i
        return re

    def __indexGenerator__ (self):
        """ Generate string indices like 1111,1112,1121,... """
        state = [1 for i in range(N)]
        stop = __product__(self, self.cardlist)
        while __product__(self, state) < stop:
            print state
            state[-1] += 1
            # Carry
            for i in range(N):
                if state[-(i+1)] > self.cardlist[-(i+1)]:
                    state[-(i+2)] += 1
                    state[-(i+1)] = 1
            yield "".join(state)

    def __init__ (self, cardlist, statementlist):
        # Todo : Check varlist and statementlist for validity
        self.N = len(cardlist)
        self.cards = cardlist
        self.statements = statementlist
        varlist = [('p' + v) for v in self.__indexGenerator__()]
        
        ## Generate the grading matrix??
        self.ring = mR(varlist)

    def indexToVar (self, index):
        """
        Converts an N-tuple to a variable string
        """
        return (p + ''.join([str (i) for i in index]))

    def varToIndex (self, var):
        """
        Converts a variable name like p1234 to the index string 1234
        """
        return [int (s) for s in var[1:]]

    def M2Ring (self, ringname="R"):
        """
        Returns the ring defining string for this CI-Model
        Name of the ring to be created can be given
        """
        varlist
        varstring = ",".join(varlist)
        return (ringname + "=QQ[" + varstring + "]\n")

    def M2Ideal (self):
        """
        Returns the ideal defining string for this CI-Ideal
        """
        pass
    
    
if __name__ == '__main__':
    # Running tests:
    g = CIModel([4,2,4,2],[])
    
