#enter letter (make input alwats lowercase)
#Change letter to ascii number 
#Take % from number and get 0-25 place of letter
#Get %26 from the (place of number + 1) to get rid of 0
#Add first ascii position (+97 = a)

def main():
    letter = input("Enter letter between 'a' and 'z': ")
    numInASCI = ord(letter)
    numInAlphaBet = numInASCI%97
    nextletter = chr((numInAlphaBet+1)%26+97)
    #negative number in %... it works but not sure how
    previousletter = chr((numInAlphaBet-1)%26+97)
    print("The next letter is: %s"%(nextletter))
    print("The previous letter is: %s"%(previousletter))
    
main()
    