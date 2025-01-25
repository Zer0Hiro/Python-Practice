# Checks if there is no numbers in the string
def is_all_let(str):
    if len(str) == 0:
        return True
    # If str in index 0 == to letter,
    # Call for the function with string that starts from index 1
    if "a" <= str[0] <= "z" or "A" <= str[0] <= "Z":
        return is_all_let(str[1:])
    return False


# Gets the string and sends it to is_all_let function
# Print if legal or not
# letters only == LEGAL else != LEGAL
def main():
    str = input("Please enter a string:")
    if is_all_let(str):
        print("The string is legal.")
    else:
        print("The string is illegal!")


main()
