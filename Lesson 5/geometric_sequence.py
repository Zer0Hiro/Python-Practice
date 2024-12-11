def main():
    a1 = int(input("Enter the first element in a geometric sequence: "))
    q = int(input("Enter the quotient of a geometric sequence: "))
    n = int(input("Enter an index / position in a sequence - a natural number: "))
    print("The first %d elements in the sequence are: "%n)
    for i in range(n):
        print(a1, end=' ')
        a1 = a1*q
        
        
main()