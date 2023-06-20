# Demo using input to quit a loop

while True:
    user_input = input("> ")
    if user_input == "quit":
        print("Bye")
        break
        # exit(1)
    else:
        print(" ")
        print(user_input)
        print(" ")