#Makes all letters in string uppercase
def UpperCase(msg):
    msg_lst = []
    for i in msg:
        if i != " " and ord(i) >= 97:
            msg_lst.append(chr(ord(i)-32))
        else:
            msg_lst.append(i)                
    return msg_lst

#Merge both strings in specific index
def combineStr(F_str,S_str,index):
    S_str = UpperCase(S_str)
    newlst = []
    for x in range(len(F_str)):
        #Merge from index(x)
        if x == index:
            for z in range(len(S_str)):
                newlst.append(S_str[z])
        newlst.append(F_str[x])
    return newlst

#Get 2 strings and position to merge both strings
def main():
    F_str = input("Enter the first string: ")
    S_str = input("Enter the second string: ")
    index = int(input("Enter index x: "))
    if index > (len(F_str)-1):
        return print("Invalid index x")
    
    #Get the combined string and print the answer
    answer = combineStr(F_str, S_str, index)
    print("combined string ", end = '')
    for i in range(len(answer)):
        print(answer[i], end = '')
        
main()
    