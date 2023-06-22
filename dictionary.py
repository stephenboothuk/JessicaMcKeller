# Create dictionary
ice_cream = {"Alice": "Chocolate", "Bob": "Strawberry", "Cara": "Mint Choc Chip"}

# Display it
print(ice_cream)
# add an item by assinging a new value to a new key
ice_cream["Eve"] = "Rum Raisin"
# Display with the new item
print(ice_cream)

# Change an item, keys must be unique so assigning a new value to an existing key changes the value for that key
ice_cream["Bob"] = "Vanilla"
# Display with changed item
print(ice_cream)

# Create empty dictionary
phone_numbers = {}
print(phone_numbers)
# Display type
print(type(phone_numbers))
