#Counts same digits in both numbers at the same place
def count_same_digit(num1,num2):
    if num1 == 0 or num2 == 0:
        return 0
    if num1%10 == num2%10:
        return 1 + count_same_digit(num1//10,num2//10)
    return count_same_digit(num1//10,num2//10)

print(count_same_digit(13145,33145))
#Check if number is polidrom
def polindrom(a):
    if len(a) <= 1:
        return True
    return a[0] == a[-1] and polindrom(a[1:-1])

print(polindrom([1,0,1,0,1,1,0,0,1]))

