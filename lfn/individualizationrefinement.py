from lfn.colorrefinement import *
from util import *

def individualizationref(dict):
    length = len(dict.values)
    print(length + " vertices in dictionary")
    for key in dict.keys():
        values = dict.get(key)
        D = []
        I = []
        for value in values:
            if value < length:
                D.append(value)
            else:
                I.append(value)
    print(D)
    print(I)


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
