def reverse():
    ls = [-1,-2,-3,-4,5,-6,7,8,]
    
    a = len(ls)
    for i in range(int(a/2)):
        if ls[i] < 0:
            for x in range(a):
                if x > 0:
                    ls[i], ls[a-i-1] = ls[a-x-1], ls[x]
    print(ls)
reverse()