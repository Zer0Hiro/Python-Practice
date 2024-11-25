def main():
    num = int(input("input the number"))
    units = num%10
    tens = (num%100)//10
    hundreds = num//100
    reversed_num = int(units*100 + tens*10 + hundreds)
    print("Original - Reversed:\n %d - %d ="%(num, reversed_num), (num-reversed_num))
main()

# Get some number
# Reverse all numbers
# Original number - Reversed number
