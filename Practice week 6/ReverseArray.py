def reverse():
    ls = [1,2,3,4,5,6,7,8,]
    
    a = len(ls)
    for i in range(int(a/2)):
        ls[i], ls[a-i-1] = ls[a-i-1], ls[i]
    print(ls)
reverse()