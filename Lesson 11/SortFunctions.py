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


print(insertionSort([1, 5, 2, 7, 3, 9]))
