def sum_num(num):
    if num < 10:
        return num
    return num%10 + sum_num(num//10)

def main():
    num = int(input("Enter a number: "))
    print(sum_num(num))

main()