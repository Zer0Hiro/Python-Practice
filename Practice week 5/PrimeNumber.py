import math

def is_prime(num):
    amount = int(math.sqrt(num))
    for i in range(2,amount+1):
        if num%i == 0:
            return True
    return False

def main():
    n = int(input("What's your number: "))
    if is_prime(n) == False:
        print("Prime number")
    else:
        print("Not Prime number")
        
main()