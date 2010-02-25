"""
Class representing a multigraded polynomial ring in Macaulay2
"""

from numpy import *

class multigradedRing(object):

    def __init__ (self, variables, grading_matrix):
        # Todo: Check that the dimensions match
        if not grading_matrix.ndim == 2:
            print "Grading should be given by a matrix"
            exit(1)
        self.variables = variables
        self.matrix = grading_matrix

    def M2Ring (self, ringname):
        """ Outputs the M2 string representing the ring """
        # Print M2 Matrix:
        matstr = "matrix{"
        dims = self.matrix.shape
        rows = [self.matrix[i] for i in range (dims[0])]
        matstr += ",".join([('{'+",".join([str(i) for i in row])+"}") for row in rows])
        matstr += '}'
        ringstr = ringname + " = QQ["
        ringstr += ",".join(self.variables)
        ringstr += ", Degrees => (entries " + matstr + " )]"
        return ringstr
