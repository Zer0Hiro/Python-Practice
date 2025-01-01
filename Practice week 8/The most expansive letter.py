#Makes all letters in string uppercase
def UpperCase(msg):
    msg_lst = []
    for i in msg:
        if i != " " and ord(i) >= 97:
            msg_lst.append(chr(ord(i)-32))
        else:
            msg_lst.append(i)                
    return msg_lst

#Checks which number is bigger ex.(a = 1, b = 2... z = 26)
def counter(msg):
    lst = UpperCase(msg)
    #Counts amount of letters
    count = 0
    maximum = 0
    minimum = 90
    for i in range(len(lst)):
        if ord(lst[i]) >= 65 and ord(lst[i]) <=90:
            count += 1
            if maximum < ord(lst[i]):
                maximum = ord(lst[i])
            if minimum > ord(lst[i]):
                minimum = ord(lst[i])
    #If there is no letters
    if count == 0:
        return print("There were no letters")
    #returns answer
    return print("Largest and smallest letters are:",chr(maximum),chr(minimum))

def main():
    msg = input("Enter your sentence: ")    
    counter(msg)

main()