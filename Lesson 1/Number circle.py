def main():
    num = int(input("input the number: "))
    units = num%10
    tens = (num%100)//10
    hundreds = num//100
    new_number = (units + 1)%10 + (tens + 1)%10*10 + (hundreds + 1)%10*100
    print(new_number)
main()

# Get some number
# Make each number next in the circle
# Write ther new number 


