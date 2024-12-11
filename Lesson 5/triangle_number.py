def main():
    num = 0
    amount = int(input("Enter a natural number: "))
    for i in range(1,amount+1):
        num += i
    print("The triangle number in location %d is: %d"%(amount,num))
    
main()