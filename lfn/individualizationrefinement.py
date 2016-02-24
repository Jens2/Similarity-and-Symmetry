from lfn.colorrefinement import *
from util import *

def individualizationref(dict):
    arrays = dict.values()
    result = []
    for array in arrays:
        for element in array:
            result.append(element)
    length = len(result)
    D = []
    I = []
    for key in dict.keys():
        vertices = dict.get(key)
        for element in vertices:
            if element < length/2:
                D.append(element)
            else:
                I.append(element)
    # countIsomorphism(D, I)
#

def countIsomorphism(D, I):
    if not isBalanced(dict):
        return 0
    if isBijection(D, I):
        return 1


    # TODO implement

def isBalanced(dict):
    arrays = dict.values()
    result = []
    for array in arrays:
        for element in array:
            result.append(element)

    length = len(result)
    counter = 0
    for key in dict.keys():
        for element in dict.get(key):
            if element < length/2:
                counter+=1
            else:
                counter-=1
    return counter == 0

dict = dict({2: [0, 6, 8, 9], 3: [1, 5, 10, 13], 4: [2, 4, 7, 12], 5: [3, 11]})
print(isBalanced(dict))


def isBijection(D, I):

    pass # TODO implement
