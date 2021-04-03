import time
from random import choice

#O (m+n+n graph)

def tryItABunch3(numTrials):
    nVals = [2**k for k in range(9)] # let's try it at a bunch of powers of 2, we'll see why later...
    nVals += [k*10 for k in range(10)]
    nVals += [k*50 for k in range(2,11)]# plus some spaced-out points...
    nVals.sort() # put them in order
    
    nValues = []
    tValues = []
    for n in range(148, 10000, 74):
        # run myFn several times and average to get a decent idea.
        runtime = 0
        for t in range(numTrials):
            lst = [ choice(range(10)) for i in range(n) ] # generate a random list of length n
            lst2 = [ choice(range(10)) for i in range(n) ] # generate a random list of length n
            start = time.time()
            n2_algorithm(lst,lst2)
            end = time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues

def n2_algorithm(items, items2):
    for first in items:
        item2 = first
    for second in items:
        item3 = second
    for third in items2:
        item4 = third