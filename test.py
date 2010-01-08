#!/usr/bin/python
"""A couple of tests"""

#print "Testing CIMatrix"
#from CIMatrix import CIMatrix
#A = CIMatrix(2,2)
#A.printRawList()

from CIMatrix import CIMatrixEntry
a = CIMatrixEntry("0")
b = CIMatrixEntry("-1")

print a-b

