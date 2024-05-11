from PartI_Task5 import *

def is_valid(word, myTiles, dictionary):
    if canBeMade(word, myTiles) and word in dictionary:
        return True
    return False
