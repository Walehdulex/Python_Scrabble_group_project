def check_word(word):
    pass

letter_scores = {}
tile_amounts = {}
dictionary = []

with open("scores.txt", "r") as scores:
    score_list = scores.readlines()
    for score in score_list:
        index = score_list.index(score)
        score_list[index] = score.replace("\n", "").split(" ")
    for score_item in score_list:
        letter_scores[score_item[0]] = int(score_item[1])
        tile_amounts[score_item[0]] = 0

with open("tiles.txt", "r") as tile_file:
    tile_letters = tile_file.readlines()
    for letter in tile_letters:
        index = tile_letters.index(letter)
        tile_letters[index] = letter.replace("\n", "").split(" ")

    for letter in tile_letters:
        tile_amounts[letter[0]] += 1

print(tile_amounts)

with open("dictionary.txt") as dic:
    for word in dic.readlines():
        stripped = word.replace("\n", "")
        dictionary.append(stripped)


