# Transforms string to integer
def check_num(str):
    if len(str) == 0:
        return 0
    #String to number using ASCII decimal
    num = ord(str[len(str) - 1]) - ord("0")
    return num + 10 * check_num(str[:len(str) - 1])

#Check if there is only numbers
def legal(str):
    for i in str:
        if not 48 <= ord(i) <= 57:
            return False
    return True

# Gets the string from user
# Print if the string is legal or illegal
# If legal prints string and number that transformed from the string
def main():
    str = input("Please enter a string:")
    if legal(str):
        print('The string "%s" corresponds to the number %d.' %(str, check_num(str)))
    else:
        print("The string is illegal!")

main()