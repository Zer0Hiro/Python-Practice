def func(lst):
    l = 0
    r = len(lst)-1
    while l < r:
        if ord(lst[l]) < ord(lst[r]):
            lst[l],lst[r] = lst[r],lst[l]
            l += 1
        else:
            r -= 1
    return lst

print(func(["K","f","H","T","m"]))

def seq(lst):
    result = 1
    for i in range(len(lst)-1):
        if lst[i] - lst[i+1] != -1:
            result += 1
    return result

print(seq([-10,-9,-8,-7,-6,3,7,8,9]))