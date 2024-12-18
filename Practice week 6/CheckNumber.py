def num_checker(num):
    found  = [False] * 10
    result = []
    while num != 0:
        found[num%10] = True
        num//= 10
    for i in range(len(found)):
        if found[i] == False:
            result.append(i)
            
    return result

def main():
    number = 3284752893475
    print(num_checker(number))
    
main()