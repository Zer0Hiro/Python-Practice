def sum_even(a):
    if a == []:
        return 0
    elif a[0]%2 == 0:
        return 1 + sum_even(a[1:])
    return sum_even(a[1:])

