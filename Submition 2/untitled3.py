def create_list(number):
    ls = []
    while number != 0:
        ls.append(number%10)
        number //= 10
    return ls

def reverse(num):
    a = len(num)
    for i in range(int(a/2)):
        num[i], num[a-i-1] = num[a-i-1], num[i]
    return num

def ready_list(number):
    num_list = create_list(number)
    r_list = reverse(num_list) 
    return r_list

def clockwise_shift(number):
    rev_list = ready_list(number)
    first = rev_list[0]
    for i in range(1,len(rev_list)):
        rev_list[i-1] = rev_list[i]
    rev_list[len(rev_list)-1] = first
    print(rev_list)

#def clockwise_shift_n(number, amount): 
    
    
def main():
    number = int(input("Enter your number: "))
    #num_list = create_list(number)
    clockwise_shift(number)
    
    
main()