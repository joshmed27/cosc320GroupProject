import time

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

def tryItABunch(myFn, startN=10, endN=100, stepSize=10, numTrials=20, listMax = 10):
    nValues = []
    tValues = []
    for n in range(startN, endN, stepSize):
        # run myFn several times and average to get a decent idea.
        runtime = 0
        new_tweet= ["AFAIK the earth is flat lol hahaha",

"r u serious,, frodo IS mumble happyfeet??",
"ym, there's no need to feel down",
"there are ppl who still say FTW.. me being one of them :)",
"imo pineapples do not belong on pizza",
"i need a new flick to watch, any suggestions?",
"Google plz release your next pixel ASAP!!!! IM SO FRIGGIN IMPATIENT!!1!11!",
"2day i will buy a laptop from amazon... there goes my bank account qq",
"my bro is literally driving me insane. he's such a bozo",
"minecraft steve in smash..so osm..so much sWaG",
"I always love a good rpg now and then",
"saw a cat the other day, we are now cuddy",
"my cat is such a cutie bestie!!",
"Can you rly call yourself a gamer if u dont play minecraft",
"tfw when no gf ;u;"]

        tweet=""
        for t in range(numTrials):
            tweet = tweet+new_tweet[t][:stepSize]
            start= time.time()
            myFn(tweet)
            end=time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
	        
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues