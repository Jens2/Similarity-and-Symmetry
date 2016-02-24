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
    countIsomorphism(D, I)


dict = dict({2: [0, 6, 8, 9], 3: [1, 5, 10, 13], 4: [2, 4, 7, 12], 5: [3, 11]})
individualizationref(dict)

def countIsomorphism(D, I):
    if not isBalanced(D, I):
        return 0
    if isBijection(D, I):
        return 1


    # TODO implement

def isBalanced(D, I):

    pass # TODO implement

def isBijection(D, I):

    pass # TODO implement
