import time
import random

#O (m+n+n graph)

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
                
            for k in range(len(sample)):
                sample[k]
                
            end=time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
	        
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues