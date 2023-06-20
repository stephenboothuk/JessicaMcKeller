import scrabble

def HasAllVowels(word):
    vowels="aeiou"
    for vowel in vowels:
        if vowel not in word:
            return False
    return(True)


for word in scrabble.wordlist:
    if HasAllVowels(word):
        print(word)

