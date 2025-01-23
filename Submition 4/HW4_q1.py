#Dmitry Chybisov 342744869
#Yelyzaveta Kytaieva 342794039

# Check if string is palindrome
# If yes returns TRUE
def is_palindrome(str, start, stop):
    if str[start] == str[stop]:
        # If start == stop then they are at the same letter
        # "a" is a palindrome then it will always be True

        # If the amount of letters even
        # check if 2 closest letter will also be checked
        if stop - start == 1 or start == stop:
            return True
        if stop == 0:
            return False
        return is_palindrome(str, start + 1, stop - 1)
    return False


# Check if string is part of the list
# If string is a part of the list and
# index in the list is >= to the index returns True
def is_in(str, str_lst, index):
    # Starts to check from the end of the list
    num = len(str_lst) - 1
    if index > num:
        return False
    if index == num:
        return str == str_lst[index]
    if str == str_lst[index]:
        return True
    return is_in(str, str_lst, index + 1)


# Additional function for num_of_palindromes
# Slice with specific size
def palindrome_runner(str, start, end, lst):
    # If end gets to the length of str
    # Then it's out of index range => return lst of the function
    if end == len(str):
        return lst
    # If it's palindrome and is not in the list
    # Add to the list
    if is_palindrome(str, start, end):
        temp = str[start:end + 1]
        if not is_in(temp, lst, 0):
            lst.append(temp)
    return palindrome_runner(str, start + 1, end + 1, lst)


# Creates size of scan for palindrome_runner
def num_of_palindromes(str, start, end, pali_lst):
    # When end is as big as string returns the size of the list
    # list consists under palindrome parts
    if end == len(str):
        return len(pali_lst)
    pali_lst = palindrome_runner(str, start, end, pali_lst)
    return num_of_palindromes(str, start, end + 1, pali_lst)


# Creates a list of str inputs
def recursive_sts_lst_input(lst):
    str = input()
    # Stops with empty string
    if str == "":
        return lst
    lst.append(str)
    return recursive_sts_lst_input(lst)


# Main function
# Fixed code
def main():
    lst = []
    print("Please enter strings, separated by new lines. Enter an empty string for stop inputing: ")
    recursive_sts_lst_input(lst)
    for st in lst:
        palindromes_lst = []
        print("The number of palindroms in'%s' is %d" % (st, num_of_palindromes(st, 0, 0, palindromes_lst)))


main()
