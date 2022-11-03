with open('words_alpha.txt') as words:
        word_list = words.readlines()

max = 0
for word in word_list:
    if len(word) > max:
        max= len(word)

print(max)
