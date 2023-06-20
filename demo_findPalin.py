import sys
import scrabble
import findPalindrome

longest = 0
longword=""

for word in scrabble.wordlist:
    # print(word, " ", str(len(word)))
    # print(longword, " ", longest)
    if len(word) > longest and findPalindrome.isPalindrome(word) == True:
        longest = len(word)
        longword = word
        # print("Yes ", longword, " ", longest)

print(longword, " is ", longest, " letters long and a palindrome which makes it the longest palindrome.")