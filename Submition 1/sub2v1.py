#Divide numbers and check each one if its lower than 6
#Try to connect numbers 
#Dmitry Chybisov 342744869
#Yelyzaveta Kytaieva 342794039
def main():
    num_check = 0
    firstnum_storage = 0
    secondnum_storage = 0
    finalnum = 0
    true_num = 0
    num_sum = 0
    not_recorded = 0
    num_count = 0
    #Getting numbers
    firstnum, secondnum = eval(input("Insert two numbers in base 7: "))
    #Start Checker
    while num_check != 1:
        #Get first units from each number
        firstnum_storage = firstnum%10
        secondnum_storage = secondnum%10
        #Count sum of units of both numbers + 1 if previous units were >=7
        num_sum = (firstnum_storage + secondnum_storage) + not_recorded
        #Reset recorder for next loop
        not_recorded = 0
        #Remove units from number, prepare them for next loop
        firstnum //= 10
        secondnum //= 10
        #Condition checker
        if firstnum_storage > 6 or secondnum_storage > 6:
            num_check = 1
            print("Illegal input!")
        else:
            #Group of 7 checker
            if num_sum >= 7:
                finalnum = num_sum%7
                not_recorded = 1
            else:
                finalnum = num_sum
            true_num = finalnum*(10**num_count) + true_num
            num_count += 1     
            #End of loop
            if firstnum == 0 and secondnum == 0:
                #If last loop summ >= 7 add additional number
                if not_recorded == 1:
                    true_num = 1*(10**num_count) + true_num
                num_check = 1
                print("The sum is the 7-base number",true_num)
main()