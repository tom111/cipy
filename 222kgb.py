#!/usr/bin/python

from BinomialPattern import *

k = 2

f1 = patternFromString222k ("1112*1211-1111*1212",k)
f2 = patternFromString222k ("1122*1221-1121*1222",k)
f3 = patternFromString222k ("2112*2211-2111*2212",k)
f4 = patternFromString222k ("2122*2221-2121*2222",k)

g1 = patternFromString222k ("1121*2111-1111*2121",k)
g2 = patternFromString222k ("1122*2112-1112*2122",k)
g3 = patternFromString222k ("1221*2211-1211*2221",k)
g4 = patternFromString222k ("1222*2212-1212*2222",k)

gens = [f1,f2,f3,f4,g1,g2,g3,g4]

## First level of S-pairs

currentgb = gens[:] # Copy of gens to start

def isReducible (pattern, curgb):
    for g in curgb:
        if pattern.redu(g) == 0:
            return True
    return False

def reduceOnce (p, gb):
    chflag = False
    for g in gb:
        if p.redu(g) == 0:  # Note the side effect
            chflag = True
            p.fixTermOrder()
    return chflag
        
def reduceMax(p, gb):
    while reduceOnce (p,gb):
        pass

def isZero (p):
    l = flatten(p.matrix.getRawList())
    for ll in l:
        if not ll.hasStar():
            if not (int(ll.s) == 0):
                return False
    return True

def gbcycle (gb):
    # Construction of Spairs
    l = len(gb)
    spairs = []
    for i in range(l):
        for j in (range(l-i-1)):
            spa = gb[i].Spair(gb[j+i+1])
            spa.fixTermOrder()
            spairs.append(spa)
    # Reduction step
    for sp in spairs:
        reduceMax(sp,gb)
        if not isZero(sp):
            print "New Move:"
            sp.printAsMatrix()
            gb.append(sp)

le = 0 
while (le < len(currentgb)):
    gbcycle(currentgb)
    print "Length of current gb: " + str (len (currentgb))

print "Result : " 
for g in currentgb:
    g.printAsMatrix()
    print ""
