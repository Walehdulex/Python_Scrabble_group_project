from PartI_Task3 import *

def getWordScore(word):
    total_score = 0
    try:
        if onlyEnglishLetters(word):
            for letter in word:
                total_score += getLetterScore(letter)
            return total_score
        else:
            return 0
    except TypeError:
        print("Error, this function requires strings")
        return False

print(getWordScore("AX"))