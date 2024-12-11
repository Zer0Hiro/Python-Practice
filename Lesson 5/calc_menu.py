
def average(a,b):
    average = float((a + b)/2) 
    print("The average is: %.2f"%average, end=' ')
    if average%2 != 0:
       print("It is not an integer number.")
    else:
        print("It is an integer number.")
   
def multiply(a,b):
    multi = a*b
    print("The multiplication is: %d"%multi)

def minimum(a,b):
    if a > b:
        print("The minimum is: %d"%b)
    else: 
        print("The minimum is: %d"%a)
        
def maximum(a,b):
    if a > b:
        print("The minimum is: %d"%a)
    else: 
        print("The minimum is: %d"%b)        

def power(a,b):
    if b > 0:
        answer = float(a**b)
        print("%d^%d is:"%(a,b), answer)
    else:
       print("Dividing by zero error") 

def main():
    op = 0
    while op != "q" and op != "Q":
        print("\nOperations Menu:")
        print("a or A : average")
        print("* : multiplication")
        print("m : minimum")
        print("M : maximum")
        print("^ : power")
        print("q or Q : quit")
        op = input("\nEnter a character: ")
        if op != "q" and op != "Q":
            print("Enter two integer numbers.")
            first = int(input("Enter the first integer: "))
            second = int(input("Enter the second integer: "))
            if op == "a" or op == "A":  
                average(first,second)
            elif op == "*":
                multiply(first, second)
            elif op == "m":
                minimum(first,second)
            elif op == "M":
                maximum(first,second)
            elif op == "^":
                power(first,second)
    print("Finish")
    
main()