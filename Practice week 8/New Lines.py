#Removes any spaces from string and writes each word as a new line
def no_space(msg):
    for i in range(len(msg)):
        if msg[i] == " ":
            print()
        else:
            print(msg[i], end="")
    print()

#Gets the string and check if its empty,
#If not call for no_space()
def main():
    n = 0
    while n == 0:
        msg = input("Enter a string, please: ")
        if len(msg) == n:
            print("Finish")
            n = 1
        else:
            no_space(msg)
            
main()