def main():
    low, high = eval(input("Enter low and high range of numbers divided by 4 and 7: "))
    count = 0
    while low <= high:
        if low%4==0 or low%7==0:
            count += 1 
            print(low)
        low += 1
    print("counter is", count)
        
main()        