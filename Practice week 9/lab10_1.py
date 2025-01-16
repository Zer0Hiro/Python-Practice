#Creates a list equal to amount of letters in english
# Every letter has its own index
# If letter is Uppercase recount the ascii number of it
#Returns the most repeatable number
def freq(str):
    count = [0] * 26
    for i in str:
        letter = ord(i)
        #Uppercase check
        if letter >= 65 and letter <= 90:
            letter += 32
        if letter >= 97 and letter <= 122:
            count[letter - 97] += 1
    max = 0
    best = 0
    #Find most amount of repeats
    for x in range(len(count)):
        if count[x] > max:
            max = count[x]
            best = x
    #If no letters in string
    if count == [0] * 26:
        return -1
    #Returns the most repeatable letter
    return chr(best + 97)

#Gets a new string print the answer and if needed stops the program
def main():
    n = 0
    while n != 1:
        str = input("Enter a string, please: ")
        #Exit from the loop
        if str == "Quit" or str == "quit":
            n = 1
        elif freq(str) == -1:
            print(-1)
        else:
            print("The most frequent letter is", freq(str))
    print("Thank you for exploring strings and complexity")


main()
