def bubble(lst):
    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


def max_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        maximum = 0
        for x in range(1, n - i):
            if lst[x] > lst[maximum]:
                maximum = x
        lst[n - 1 - i], lst[maximum] = lst[maximum], lst[n - 1 - i]
    return lst


print(max_sort([1, 5, 2, 7, 3, 9]))
