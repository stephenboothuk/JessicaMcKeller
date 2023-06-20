import scrabble
import string

for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            exists=True
            break
    if exists == False:
        print("No english words contain a double " + letter)


