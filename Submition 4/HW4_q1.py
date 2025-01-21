# Check if string is palindrome
# If yes returns TRUE
def is_palindrome(str, start, stop):
    if str[start] == str[stop]:
        # If start == stop then they are at the same letter
        # "a" is a palindrome then it will always be True
        #ABBA
        if stop-start == 1 or start == stop:
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
    if num >= index:
        if str == str_lst[num]:
            return True
        return is_in(str, str_lst[:num], index)
    return False

def palindrome_runner(str,start,end,lst):
    if end == len(str):
        return lst
    if is_palindrome(str, start, end):
        temp = str[start:end + 1]
        if not is_in(temp, lst, 0):
            lst.append(temp)
    return palindrome_runner(str, start + 1, end + 1,lst)


def num_of_palindromes(str, start, end, pali_lst):
    if end == len(str):
        return len(pali_lst)
    pali_lst = palindrome_runner(str,start,end,pali_lst)
    return num_of_palindromes(str,start,end+1,pali_lst)


def recursive_sts_lst_input(lst):
    str = input()
    if str == "":
        return lst
    lst.append(str)
    return recursive_sts_lst_input(lst)


def main():
    lst = []
    print("Please enter strings, separated by new lines. Enter an empty string for stop inputing: ")
    recursive_sts_lst_input(lst)
    for st in lst:
        palindromes_lst = []
        print("The number of palindroms in'%s' is %d" % (st, num_of_palindromes(st, 0, 0, palindromes_lst)))

main()
