def main():
    num = int(input("input the number: "))
    units = num%10
    tens = (num%100)//10
    hundreds = num//100
    noteven_num = units%2 + tens%2 + hundreds%2 
    print("Amount of not even numbers is: ", noteven_num)
main()

# Get some number
# Find not evwn number
# Show the amount of not even numbers
