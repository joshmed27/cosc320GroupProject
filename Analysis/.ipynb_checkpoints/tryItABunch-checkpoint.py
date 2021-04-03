import time

def tryItABunch(myFn, startN, endN, stepSize, numTrials):
    
    nValues = []
    tValues = []
    new_tweet="Google plz release your next pixel ASAP!!!! IM SO FRIGGIN IMPATIENT!!1!11!" #Sample text to add to test
    tweet=new_tweet
    
    for n in range(startN, endN, stepSize):
        # run myFn several times and average to get a decent idea.
        runtime = 0
        tweet += (new_tweet)
        for t in range(numTrials):
            start= time.time()
            myFn(tweet)
            end=time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
	        
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues