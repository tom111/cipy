#!/usr/bin/python
"""A couple of tests"""

print "Testing CIMatrix"
from CIMatrix import CIMatrix
A = CIMatrix(2,2)
A.printRawList()

print "\n\n Testing BinomialPattern222k"
from BinomialPattern import BinomialPattern222k
M = BinomialPattern222k(4)
M.fromBinomial("1111*2222-2222*1212")
N = BinomialPattern222k(4)
N.fromBinomial("1111*1211-1211*2111")

M.printAsMatrix()
print "\n"
N.printAsMatrix()
print "\n"
M.Spair(N).printAsMatrix()
