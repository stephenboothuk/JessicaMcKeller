# define the function
def greeting(name):
    print("Hello " + name)

def sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return(total)

def starts_with_a_vowel(word):
    if word[0] in "AEIOUaeiou":
        return(True)
    else:
        return(False)

def filter_to_initial_vowel(word_list):
    vowel_list = []
    for word in word_list:
        if starts_with_a_vowel(word):
            vowel_list.append(word)
    return(vowel_list)

names = ["Alice", "Bob", "Cara", "Dave", "Edith"]


greeting("thingie")

prices = [10, 20, 15, 18]

print("Sum of " + str(prices) + " = " + str(sum(prices)))

for word in names:
    print("Does " + word + " start with a vowel? " + str(starts_with_a_vowel(word)))

print("Names that start with a vowel" + str(filter_to_initial_vowel(names)))

