def main():
    elements = int(input("Enter the number of elements in the sequence: "))
    print("Enter the elements of the sequence:")  
    x = int(input())
    y = int(input())
    dif = y-x
    
    for i in range (elements-2):
        x = y
        y = int(input())
        
        if y-x != dif:
            status = 0
        else:
            status = 1
    
    if status == 1:
        print("Arithemtic Sequence")
    else:
        print("Not arithemtic Sequence")

main()        