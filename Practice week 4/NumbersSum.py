def main():
    number = int(input("Enter the number:"))
    summ = 0
    while number > 0:
        digit = number%10
        summ += digit
        number //= 10
    print("The sum of numbers:", summ)
main()        