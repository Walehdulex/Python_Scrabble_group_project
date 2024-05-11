from PartI_Task4 import *
sampl = [2, 3]

def canBeMade(word="", myTiles=[]):
    try:
        valid = True
        tile_copy = myTiles.copy()
        for letter in word:
            if letter in tile_copy:
                tile_copy.remove(letter)
            else:
                valid = False
        return valid
    except TypeError:
        print("Error, this function requires strings for the word param")
        return False
    except AttributeError:
        print("'myTiles' must have a list as its parameter")
        return False



canBeMade(sampl)
print(sampl)

