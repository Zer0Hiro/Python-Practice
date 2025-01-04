def no_space(msg):
    for i in range(len(msg)):
        if msg[i] == " ":
            print()
        else:
            print(msg[i], end="")
    print()
 
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