def summ(num):
    total = 0
    number = 0
    while num != 0:    
        number = num%10
        total += number
        num //= 10
    return total

def main():
    prev_checker = 0
    checker = 0
    biggest = 0
    n = 0
    while n != -1:
        n = int(input("Enter the number, stop with -1: "))
        if n != -1:
            checker = summ(n)
            print("Checker",checker)
            print(prev_checker)
            if checker >= prev_checker:
                biggest = n
            prev_checker = checker
    print("Number %d has the largest sum of digits: %d"%(biggest,checker))

main()