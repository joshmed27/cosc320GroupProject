import time
import random

# tryItABunch: runs a function a bunch, and times how long it takes.
#
# Input: myFn: a function which takes as input a string (tweet)
# Output: lists nValues and tValues so that running myFn on a string of length nValues[i] took (on average over numTrials tests) time tValues[i] milliseconds.
#
# Other optional args:
#    - startN: smallest n to test
#    - endN: largest n to test
#    - stepSize: test n's in increments of stepSize between startN and endN
#    - numTrials: for each n tests, do numTrials tests and average them
#    - listMax: the input lists of length n will have values drawn uniformly at random from range(listMax)

def tryItABunch2(startN, endN, stepSize, numTrials):
    nValues = []
    tValues = []
    sample = []

    for n in range(startN, endN, stepSize):
        runtime = 0
        #Appends stepSize amount of numbers to sample
        for k in range(stepSize):
            sample.append(random.randint(1,30))
        
        # numTrials with step size of iterating lists
        for t in range(numTrials):
            start= time.time()
            for k in range(len(sample)):
                sample[k]

            for k in range(len(sample)):
                sample[k]
                
            end=time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
	        
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues