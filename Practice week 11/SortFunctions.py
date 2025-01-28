def inserter(lst, num):
    n = len(lst)
    lst.append(lst[n - 1] + 1)
    i = len(lst) - 2
    while i >= 0 and lst[i] > num:
        lst[i + 1] = lst[i]
        i -= 1
    lst[i + 1] = num
    return lst


# print(inserter([10, 12, 13, 14, 15, 18, 20], 21))

def csort(lst):
    mlst = [0] * 101
    for x in lst:
        mlst[x] += 1
    i = 0
    x = 0
    while i <= len(mlst) - 1:
        if mlst[i] > 0:
            mlst[i] -= 1
            lst[x] = i
            x += 1
        else:
            i += 1
    return lst


# print(csort([2, 1, 0, 5, 5, 1, 5, 4]))

def ident(lst):
    lst.sort()
    for i in range(len(lst)):
        if lst[i] == lst[i + 1]:
            return True
    return False

# print(ident([4,8,1,9,14,1]))

def triple(lst):
    result = []
    for i in range(len(lst)-2):
        result.append(lst[i]+lst[i+1]+lst[i+2])
    return ident(result)

# print(triple([1,2,3,5,6,7,8,9,0,3,2,1]))

