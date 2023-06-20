# set up a list of names then print those names using a for loop
names = ["Alice", "Bob", "Cassie", "Diane", "Ellen"]
for name in names:
    print(name)
print(" ")
print("**********************************************************************************************")
print(" ")
# print the name only if it begins with a vowel
for name in names:
    if name[0] in "AEIOUaeiou":
        print(name + " starts with a vowel")

print(" ")
print("**********************************************************************************************")
print(" ")
# Build list of just those names that begin with a vowel
vowel_names = []
for name in names:
    if name[0] in "AEIOUaeiou":
        vowel_names.append(name)

print(vowel_names)

# adding in a for loop
print(" ")
print("**********************************************************************************************")
print(" ")

prices = [1.5, 2.35, 5.99, 16.49]
total = 0
for price in prices:
    total = total + price

print(total)

# or use the built in function sum()
print(sum(prices))

print(" ")
print("**********************************************************************************************")
print(" ")

counter = 0
while counter < 5:
    print("Hello " + str(counter))
    counter = counter + 1

print(" ")
print("**********************************************************************************************")
print(" ")

counter = 0
while True:
    print("Hello " + str(counter))
    counter = counter + 1
    if counter >4:
        break

