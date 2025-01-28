# Adds number to sorted position
def add_lst(lst, x):
    n = len(lst) - 1
    if len(lst) == 0:
        lst.append(x)
        return lst
    # Tries to fit x between numbers in list
    if x <= lst[n]:
        return add_lst(lst[:n], x) + lst[n:]
    elif x >= lst[0]:
        lst.append(x)
        return lst

# Gets 5 elements and number that user wants to add to list
def main():
    lst = []
    print("Enter elements:")
    for i in range(5):
        lst.append(int(input()))
    print("The list:", lst)
    # Enter the number that user want to add to the list
    num = int(input("Enter new number: "))
    print("The New List:", add_lst(lst, num))

main()
