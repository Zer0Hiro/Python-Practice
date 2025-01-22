# Check if function is palindrome
# Returns TRUE of FALSE
def is_palindrome(lst):
    if len(lst) == 0:
        return True
    if lst[0] == lst[len(lst) - 1]:
        return is_palindrome(lst[1:len(lst) - 1])
    return False


# Creates a list from number
# Returns new list
def lst_builder(num):
    lst = []
    while num != 0:
        lst.append(num % 10)
        num = num // 10
    return lst


# Get number from user
# Make list from the number
# Print if this number is palindrome or not
def main():
    print("Enter a sequence of natural numbers,end with 0:")
    a = 1
    while a != 0:
        a = int(input())
        if a != 0:
            if is_palindrome(lst_builder(a)):
                print("The list of digits is a Palindrom")
            else:
                print("The list of digits is not a Palindrom")
        else:
            print("FINISH")


main()
