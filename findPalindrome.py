def isPalindrome(word):
    wLen=len(word)
    mid = 0
    mid=int(round((wLen/2)))+1
    isPalin = True

# Long manual method
    # for counter in range(0, mid):
    #   if word[counter] != word[(wLen-1)-counter]:
    #       isPalin = False
    #       break

# short fancy method
    if list(word) == list(reversed(word)):
       return True

# even shorter fancier method, not really readable
    # if word == word[::-1]:
    #    return True
    # return isPalin


