#Create list from number
def create_list(number):
    ls = []
    while number != 0:
        ls.append(number%10)
        number //= 10
    return ls

#Reverse list so it looks like normal number
def reverse(num):
    a = len(num)
    #Reverse of list
    for i in range(int(a/2)):
        #Ex. a, b = b, a
        num[i], num[a-i-1] = num[a-i-1], num[i]
    return num

#Just both prev functions together for easier usage
def ready_list(number):
    num_list = create_list(number)
    r_list = reverse(num_list) 
    return r_list

#Final number sum
def final_number(lst):
    length = len(lst)
    final_num = 0
    for x in range(length):
        final_num += lst[x]*10**(length-1-x)
    return(final_num)

#Moves every number to the next index in a row
def clockwise_shift(number):
    rev_list = ready_list(number)
    length = len(rev_list)
    #Goes backwards from higher to lower so it moves clockwise and not ccwise
    for i in range(1,length):
        #Same logic as in reverse but now its closest pairs
        rev_list[i-1], rev_list[i] = rev_list[i], rev_list[i-1]
    return rev_list

#Additional instruction (Just clockwise_shift but with n>=0 repeats)
def clockwise_shift_n(number, amount):
    num = number
    for x in range(amount):
        num_ls = clockwise_shift(num)
        num = final_number(num_ls)
    return final_number(num_ls)

#Gets numbers and creates list from them
def build_list():
    number = int(input("Enter integer numbers > 0, end with -1\n"))
    n_lst = [number]
    while number != -1:
        number = int(input())
        n_lst.append(number)
    return n_lst

#Print the initial numbers from list in one line
def print_list(lst):
    print("The initial list is: ", end="")
    for i in range(len(lst)-1):
        if i != len(lst)-2:
            print(lst[i], end=",")
        else:
            print(lst[i], end="")
    print()

#Activates clockwise function that moves number index of number(i) times 
def shift_all(lst):
    print("The list after it's items clockwise shifting is: ", end="")
    print(lst[0], end=",")
    for i in range(1,len(lst)-1):
        if i != len(lst)-2:
            print(clockwise_shift_n(lst[i],i), end=",")
        else:
            print(clockwise_shift_n(lst[i],i), end="")
            
#Use everything together   
def main():
    lst = build_list()
    print_list(lst)
    shift_all(lst)
    
main()
