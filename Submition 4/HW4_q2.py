# Dmitry Chybisov 342744869
# Yelyzaveta Kytaieva 342794039
from os import lstat


# Sum of every number in list
def sum_lst(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_lst(lst[1:])


# Checks if list is wrapped
# Uses sum_lst function to check summ between first and last index
def is_wrapped_lst(lst):
    if len(lst) <= 2:
        return True
    # If summ of border indexes == to summ of indexes between them
    if lst[0] + lst[-1] == sum_lst(lst[1:-1]):
        return is_wrapped_lst(lst[1:-1])
    return False

# Sort numbers to even and odd numbers
# Creates a list of sorted numbers
# EVEN numbers and then ODD numbers
def even_odd_sort(lst, evenl, oddl):
    if len(lst) == 0:
        return evenl + oddl
    if lst[0] % 2 == 0:
        evenl.append(lst[0])
    else:
        oddl.append(lst[0])
    return even_odd_sort(lst[1:], evenl, oddl)

# Check if lst is sorted
# EVEN on Left
# ODD on Right
def is_even_odd_sorted(lst, index):
    if index == len(lst) - 1:
        return True
    # If odd number is on the left from even number then FALSE
    if lst[index + 1] % 2 == 0 and lst[index] % 2 != 0:
        return False
    return is_even_odd_sorted(lst, index + 1)

# Creates a list from inputs of user
# Fixed amount of inputs
def recursive_input_list(lst, n):
    if n == 0:
        return lst
    lst.append(int(input()))
    return recursive_input_list(lst, n - 1)

# Main Function
# Fixed code
def main():
    n = int(input("Please enter number of elements: "))
    print("Please enter %d integers, separated by new lines: " % n)
    lst = []
    recursive_input_list(lst, n)
    is_wrapped = is_wrapped_lst(lst)
    is_sorted = is_even_odd_sorted(lst, 0)
    print(lst, end=" is ")
    if not is_wrapped:
        print("not", end=" ")
    print("wrapped and is", end=" ")
    if not is_sorted:
        print("not", end=" ")
    print("even odd sorted")
    lst = even_odd_sort(lst, [], [])
    print("Even odd sorted list: ", end="")
    print(lst)
    if not is_even_odd_sorted(lst, 0):
        print("There is a bug")


main()
