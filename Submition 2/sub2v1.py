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
    for i in range(length-1,0,-1):
        #Same logic as in reverse but now its closest pairs
        rev_list[i-1], rev_list[i] = rev_list[i], rev_list[i-1]
    return rev_list

#Additional instruction (Just clockwise_shift but with n>=0 repeats)
def clockwise_shift_n(number, amount): 
    for x in range(amount):
        num_ls = clockwise_shift(number)
    return final_number(num_ls)

def build_list():
    
def main():
    number = int(input("Enter your number: "))
    
    #n = int(input("How many times do you want to move your numbers? (integer >= 0): "))
    #clockwise_shift(number)
    #print("Number after clockwise shift with %d times equal:"%(n), clockwise_shift_n(number, n))
    
    
main()