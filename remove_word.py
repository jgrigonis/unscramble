import os
import sys

WORD_FILE = 'word_files' + os.sep + 'scrabble-lower.txt'

try:
    removed_word = sys.argv[1]
except IndexError:
    print("Must specify a word to remove.")
    quit()

with open(WORD_FILE) as word_file:
    word_list = word_file.readlines()

with open(WORD_FILE, 'w') as word_file:
    for word in word_list:
        if word.strip() != removed_word:
            word_file.write(word)
