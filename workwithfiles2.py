# Open the file for writing
f = open("scores.txt", "w")

#
while True:
    participant = input("Participant name > ")
    if participant == "quit":
        break
    score = input("Score for " + participant + " > ")
    f.write(participant + ", " + score + "\n")

f.close()

