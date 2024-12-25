def digit_count(num):
    count = [0]*10
    if num < 0:
        num *= -1
    if num == 0:
        count[0] = 1
    while num != 0:
        count[num%10] += 1
        num //= 10
    return count

def appear(lst):
    for i in range(len(lst)):
        if lst[i] != 0:
            print("The digit %d appears %d times"%(i,lst[i]))

def frequency(lst):
    freq = 0
    for i in range(len(lst)):
        if lst[i] >= freq:
            freq = lst[i]
    print("The most frequent digit/s is/are:", end="")
    for z in range(len(lst)):
        if lst[z] == freq:
            print(z,end=" ")
    print()
    print("It occurs times %d"%freq)

def main():
    flag = 1
    while flag != 0:   
        number = int(input("Enter integer: "))
        lst = digit_count(number)
        appear(lst)
        frequency(lst)
        if number == 0:
            flag = 0
    
main()