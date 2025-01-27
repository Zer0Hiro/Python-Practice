# Closest numbers sorter
def bubble(lst):
    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


# Find the biggest number and put it at the end of list
def max_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        maximum = 0
        for x in range(1, n - i):
            if lst[x] > lst[maximum]:
                maximum = x
        lst[n - 1 - i], lst[maximum] = lst[maximum], lst[n - 1 - i]
    return lst


# Sorted list expansion
def insertionSort(lst):
    for i in range(1, len(lst)):
        num = lst[i]
        x = i - 1
        while x >= 0 and num < lst[x]:
            lst[x + 1] = lst[x]
            x -= 1
        lst[x + 1] = num
    return lst


#########################################
# Connect 2 sorted lists

def lstAppend(lst, result):
    for i in range(len(lst)):
        result.append(lst[i])
    return result


def sumlst(lst1, lst2):
    result = []
    x, y = 0,0
    while x < len(lst1) and y < len(lst2):
        if lst1[x] < lst2[y]:
            result.append(lst1[x])
            x += 1
        else:
            result.append(lst2[y])
            y += 1
    if x == len(lst1):
        lstAppend(lst2[y:], result)
    else:
        lstAppend(lst1[x:], result)
    return result


print(sumlst([2, 5, 6], [1, 3, 5, 7, 8, 11]))
