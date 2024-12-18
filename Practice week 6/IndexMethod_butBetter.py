def first_index(ls, num):
    for i in range(len(ls)):
        if ls[i] == num:
            return i
    return -1
        