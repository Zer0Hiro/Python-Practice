def main():
    num = int(input("Please enter 4-digits integer:"))
    #Side swap
    rightpart = num%100
    leftpart = num//100
    #New number
    print("New number: %d"%(rightpart*100 + leftpart))
    #Even digits search and count
    #Numbers are from left to right for ex: -> 2 3 5 7
    #If 2357 then firstnum = 2
    firstnum = ((leftpart//10) + 1)%2
    secondnum = (leftpart + 1)%2
    thirdnum = ((rightpart//10) + 1)%2
    fourthnum = (rightpart + 1)%2
    even = firstnum + secondnum + thirdnum + fourthnum
    print("The amount of even digits in the number %04d is %d"%(num, even))
    
main()