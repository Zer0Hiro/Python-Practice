def counter(num):
    count = 0
    for i in range(2,num):
         if num%i == 0:
            count +=1
    return count

def main():
    number = int(input("Write the number: "))
    print("Amount of dividers:",counter(number))
    if counter(number)%2 != 0:
        print("Pefect Square")
    else:
        print("Not Perfect Square")
    
main()
