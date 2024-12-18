def isSortedAscending(L):
    for i in range(1,len(L)):
        if L[i] <= L[i-1]:
            return False
    return True

def main():
    L = [1,2,2,4,5,6,7]
    print(isSortedAscending(L))
    
    
main()