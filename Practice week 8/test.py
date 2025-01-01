def no_space(msg):
    for i in range(len(msg)):
        if msg[i] == " ":
            print()
        else:
            print(msg[i], end="")
            