import argparse
import os


WORD_FILE = 'word_files' + os.sep + 'scrabble-lower.txt'
REMOVE = 'remove.txt'
FOUND = 'found.txt'

def check_words(scrambled, min):
    """
    Find all the words in the word list that are longer than the min.
    Return those words in the found_words list.
    """
    found_words = []
    with open(WORD_FILE) as words:
        word_list = words.readlines()
    for word in word_list:
        word = word.strip()
        if is_word_in_scramble(word, scrambled):
            if len(word) >= min:
                found_words.append(word)
    return found_words


def is_word_in_scramble(word, scramble):
    """
    True if the word can be created from the scramble letters.
    False otherwise.
    """
    scramble_list = list(scramble)
    for letter in word.strip():
        if letter not in scramble_list:
            return False
        else:
            scramble_list.remove(letter)
    return True


def create_remove_files(found_words):
    """
    Create the remove file and a copy.
    """
    try:
        os.remove(REMOVE)
    except FileNotFoundError:
        pass
    try:
        os.remove(FOUND)
    except FileNotFoundError:
        pass
    for word in found_words:
        with open(REMOVE, 'a') as remove_file:
            remove_file.write(word)
            remove_file.write('\n')
        with open(FOUND, 'a') as found_file:
            found_file.write(word)
            found_file.write('\n')  
        print(word)


def parse_args():
    """Get the arguments from the command line."""
    parser = argparse.ArgumentParser(description='Find all words in the scrambled string')
    parser.add_argument('scrambled', help='The scrambled string.')
    parser.add_argument('-min', type=int, default=3)
    args = parser.parse_args()
    return args


def main():
    """Main entry function."""
    args = parse_args()
    found_words = check_words(args.scrambled, args.min)
    create_remove_files(found_words)
    

if __name__ == '__main__':
    main()
