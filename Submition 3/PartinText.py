#Dmitry Chybisov 342744869
#Yelyzaveta Kytaieva 342794039
#Counts how many times requested part(part) appears in text
def count_occurrences(text, part):
    count = 0
    l = len(part) 
    for i in range(len(text)):
        #Check if part that we need equal to part in text
        if part == text[i:i+l]:
            count += 1     
    return count

#Counts which part from the list (lst) appears most of the time    
def max_occurrences(text,lst):
    maximum = 0
    index = 0
    for x in range(len(lst)):
       count = count_occurrences(text, lst[x])
       #Storage
       if count > maximum:
           maximum = count
           index = x
       elif count == maximum:
           if lst[index] >= lst[x]:
               index = x
    return lst[index] 

#Main function, gets main string and amount of parts at the end shows which part appears most of the time
def main():
    string = input("Enter a string: ")
    amount = int(input("Enter the list length: "))
    parts = []  
    #Creates list of parts
    print("Enter %d strings:"%amount)
    for i in range(amount):
        parts.append(input())
    #Output of the final calculations
    print('The most repeated string is "%s"'%max_occurrences(string,parts))
    
main()