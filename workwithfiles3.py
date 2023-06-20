# Open scores file for reading
f = open("scores.txt", "r")

# Create Dictionary
participants = {}

for line in f:
    # Format of line is key, value
    # Remove trailing space and split on a comma
    # populare two element list
    entry = line.strip().split(",")
    participants[entry[0]] = entry[1]
    print(entry[0] + " : " + entry[1])

f.close()

print(participants)

