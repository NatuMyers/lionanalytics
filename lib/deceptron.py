# -*- coding: utf-8 -*-

#from letters import letters

# negative word array
from arr_negwords import negWords

# action verb array
from arr_actionverbs import actionVerbs

# excl word array
from arr_exclusivewords import exclusiveWords
from arr_exclusivewords import inclusiveWords

# sfpp word array
from arr_sfppwords import sfppWords
from arr_sfppwords import pfppWords


# Translate is useless but will stay for illustrative purposes


def translate(text):
    result = ''
    for char in text: # append the chars in letters to an empty string and return in bassed on the mapping in text
        result += letters[char]
    return result


# (text) is the parameter we give this function in the original python deceptron file
def calcDeceptiveness(text):

    SCORE_CONSTANT = 1000
	
    # array from words that the user just imported
    inputArray = text.split()
    # For some reason, we must return a string.
    
    textLength = len(inputArray)
    
	# negative ---

    negCount = 0
    # count of all negative words
    for i in negWords:
    	negCount += inputArray.count(i)
    	
    #normalize 
    negRate = float( (negCount * SCORE_CONSTANT) /textLength   ) # mult by 1000 so numbers aren't too small
    
    negativeString = "Negative Subconsious Factor:  " + str(int(negRate))
    
    
	# action ---

    actCount = 0
    # count of all negative words
    for i in negWords:
    	actCount += inputArray.count(i)
    	
    #normalize 
    actRate =  float( (actCount * SCORE_CONSTANT) /textLength   )  # mult by 1000 so numbers aren't too small
    
    actionString = "Story Exaggeration Factor:  " + str(int(actRate))
    

	# inclusive ---

    inclusiveCount = 0
    # count of all negative words
    for i in inclusiveWords:
    	inclusiveCount += inputArray.count(i)
    	
    #normalize 
    inclusiveRate =  float( (inclusiveCount * SCORE_CONSTANT) /textLength   )  # mult by 1000 so numbers aren't too small
    
    inclusiveString = "Cognitive Load Factor:  " + str(int(inclusiveRate))
   
    
	# pfpp ---

    pfppCount = 0
    # count of all negative words
    for i in sfppWords:
    	pfppCount += inputArray.count(i)
    	
    #normalize 
    pfppRate =  float( (pfppCount * SCORE_CONSTANT) /textLength   )  # mult by 1000 so numbers aren't too small

    
    pfppString = "Self Avoidance Factor:  " + str(int(pfppRate))
    
    
    # final calc |||----
    if negRate+actRate+inclusiveRate+pfppRate == 0:
    	sumString = "Untracable deception present."
    else:
    	sumString = "Deceptron Rank:  " + str(   int(negRate+actRate+inclusiveRate+pfppRate)    )
    
    
    # combined string
    resultantString = sumString + "<br/><br/>" + negativeString + "<br/>" + actionString + "<br/>" + inclusiveString + "<br/>" + pfppString + "<br/>" 

    return resultantString