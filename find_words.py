import argparse
import os

WORD_FILE = 'curated_words.txt'
#WORD_FILE = 'words_alpha.txt'


def check_words(scrambled, min):
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
    scramble_list = list(scramble)
    for letter in word.strip():
        if letter not in scramble_list:
            return False
        else:
            scramble_list.remove(letter)
    return True


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
    try:
        os.remove('remove.txt')
    except FileNotFoundError:
        pass
    for word in found_words:
        with open('remove.txt', 'a') as remove_file:
            remove_file.write(word)
            remove_file.write('\n')
        print(word)


if __name__ == '__main__':
    main()
