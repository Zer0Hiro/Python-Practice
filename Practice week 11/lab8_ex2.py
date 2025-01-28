# n+nlogn => O(nlogn)
# Sorts list and creates the biggest possible number
def biggest_num(lst):
    lst.sort()
    num = 0
    for i in range(len(lst) - 1, -1, -1):
        num = lst[i] + 10 * num
    return num


# Gets integers and creates a list
# Prints the biggest number possible from this numbers
def main():
    lst = []
    i = 0
    print("Enter digits:")
    while i != -1:
        i = int(input())
        if i != -1:
            lst.append(i)
    if len(lst) == 0 and i == -1:
        print("Input Error")
    else:
        print("The largest number is: ", biggest_num(lst))


main()

