#Check if string is palindrome
# If yes returns TRUE
def is_palindrome(str, start, stop):
    if str[start] == str[stop]:
        #If start == stop then they are at the same letter
        # "a" is a palindrome then it will always be True
        if start == stop:
            return True
        return is_palindrome(str, start + 1, stop - 1)
    return False


#Check if string is part of the list
#If string is a part of the list and
#index in the list is >= to the index returns True
def is_in(str,str_lst,index):
    #Starts to check from the end of the list
    num = len(str_lst)-1
    if num >= index:
        if str == str_lst[num]:
            return True
        return is_in(str,str_lst[:num],index)
    return False


def num_of_palindromes(str,start,end,pali_lst):
    if is_palindrome(str,start,end) == True:
        if is_in(str,pali_lst,0) != True:
            pali_lst.append(str)



def recursive_sts_lst_input(lst):
    str = input()
    if str == "":
        return lst
    lst.append(str)
    return recursive_sts_lst_input(lst)

def main():
    lst=[]
    print("Please enter strings, separated by new lines. Enter an empty string for stop inputing: ")
    recursive_sts_lst_input(lst)
    for st in lst:
        palindromes_lst=[]
        print("The number of palindroms in'%s' is %d" %(st, num_of_palindromes(st, 0, 0, palindromes_lst)))
main()