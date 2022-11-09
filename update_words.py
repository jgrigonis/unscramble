import os
import sys

REMOVE = 'remove.txt'
FOUND = 'found.txt'
CONFIRMED = 'confirmed.txt'
WORD_FILE = 'word_files' + os.sep + 'scrabble-lower.txt'

with open(REMOVE) as remove_file:
    remove_list = remove_file.readlines()

with open(WORD_FILE) as word_file:
    word_list = word_file.readlines()

with open(FOUND) as found_file:
    found_list = found_file.readlines()

with open(WORD_FILE, 'w') as word_file:
    for word in word_list:
        if word not in remove_list:
            word_file.write(word)
        else:
            print(word)

with open(CONFIRMED) as confirmed_file:
    confirmed_list = confirmed_file.readlines()

confirmed_add_list = list(set(found_list) - set(remove_list))
with open(CONFIRMED, 'a') as confirmed_file:
    for word in confirmed_add_list:
        if word not in confirmed_list:
            confirmed_file.write(word)
