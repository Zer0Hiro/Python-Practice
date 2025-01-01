#Removes any duplicates using slicing
def dupe_removal(msg):
    updated = []
    for i in range(len(msg)):
        if msg[i:i+1] != msg[i-1:i]:
            updated.append(msg[i])
    return updated
        
def main():
    msg = input("Enter a string, please:")
    upd = dupe_removal(msg)
    #Loop to print everything from list(upd)
    print("After removing all duplicates: ", end='')
    for i in upd:
        print(i,end='')
    
main()