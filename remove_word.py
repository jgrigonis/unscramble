import sys

REMOVE = 'remove.txt'
#WORD_FILE = 'curated_words.txt'
WORD_FILE = 'scrabble-lower.txt'

try:
    removed_word = sys.argv[1]
except IndexError:
    removed_word = None

with open(REMOVE) as remove_file:
    remove_list = remove_file.readlines()

with open(WORD_FILE) as word_file:
    word_list = word_file.readlines()

with open(WORD_FILE, 'w') as word_file:
    for word in word_list:
        if removed_word:
            if word.strip() != removed_word:
                word_file.write(word)
        else:
            if word not in remove_list:
                word_file.write(word)
            else:
                print(word)


