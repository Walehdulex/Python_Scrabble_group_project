from PartI_Task1 import letter_scores, tile_amounts

def onlyEnglishLetters(word):
    """
    A function of Part 1 task 2 of the assignment which checks that a word is english
    """
    valid = True
    for letter in word:
        if letter not in tile_amounts.keys():
            valid = False
    return valid
print(onlyEnglishLetters('HELLO'))

print(onlyEnglishLetters('HE LLO'))

print(onlyEnglishLetters('HE3LLO'))

