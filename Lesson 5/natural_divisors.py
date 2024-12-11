def main():
    num = int(input("Enter a natural number: "))
    if num <=0:
        print("Input is not a natural number")
    else:
        count = 0
        right = 0
        print("The list of natural divisors of %d is: "%num, end='')
        for i in range(1,num+1):
            right = num%i
            if right == 0:
                count += 1
                print(i,end=' ')
        print("\nThe amount of divisors is: %d"%count)
main()
                