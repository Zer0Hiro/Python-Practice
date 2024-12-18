def print_triangle(symbol,amount):
    print("*** Triangle  ***")
    while amount != 0:
        for i in range(amount):
            print(symbol, end=' ')
        print()
        amount -= 1
        
def main():
    letter = input("Enter a letter:")
    integer = int(input("Enter an integer:"))
    print_triangle(letter, integer)

main()    