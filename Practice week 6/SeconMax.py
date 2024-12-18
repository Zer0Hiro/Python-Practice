def second_max(ls):
    first = ls[0]
    final = ls[0]
    for i in range(1,len(ls)):
        if ls[i] > first:
            final = first
            first = ls[i]
            
    return final

ls = [5, 8]
print(second_max(ls))
            