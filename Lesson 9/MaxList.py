def max(lst):
    if len(lst) == 0:
        return 0
    elif lst[0] < lst[len(lst)-1]:
        return max(lst[1:])
    elif lst[0] > lst[len(lst)-1]:
        return max(lst[:len(lst)-1])
    return lst[0]

def main():
    lst = [7,3,6,5,26,32,156,22]
    print(max(lst))

main()