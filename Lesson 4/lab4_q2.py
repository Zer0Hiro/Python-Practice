def main():
    num = int(input("Please enter a 4-digits natural number: "))
    if num < 0:
        print("%d isn't a natural number."%num)
    elif num < 1000 or num > 9999:
        print("%d isn't a 4-digits number."%num)
    else:
        units = num%10
        tens = (num//10)%10
        hund = (num//100)%10
        thousand = num//1000
        #Check if previous number higher or lower than the next 
        first_dif = tens - units 
        second_dif = hund - tens
        third_dif = thousand - hund
        #Check what sequence is it
        #If all digits are the same
        if units == tens == hund == thousand:
            print("All digits are the same.")
        #Increasing sequences    
        elif units >= tens >= hund >= thousand:
            if first_dif == second_dif == third_dif:
                print("Increasing arithmetic sequence.")
            else:
                print("Increasing sequence.")
        #Decreasing sequences    
        elif units <= tens <= hund <= thousand:
            if third_dif == second_dif == first_dif:
                print("Decreasing arithmetic sequence.")
            else:
                print("Decreasing sequence.")
        #Any other sequences
        else:
            print("Not increasing and not decreasing.")
main()