#Search for the lowest number in the list
#Using binary search
def minShiftedList(lst,length):
    l = length
    left, right = 0, l - 1
    while l != 0:
        mid = (left + right)//2
        if lst[mid] > lst[left]:
            left = mid
        elif lst[mid] < lst[left]:
            right = mid
        else:
            #+1 because mid will be equal to the biggest number in the list
            return lst[mid+1]
#Creates list of numbers
#Print the smallest number in the list
def main():
    n = 0
    lst = []
    print("Please enter ordered and shifted sequence of numbers (end with -1): ")
    while n != 1:
        a = int(input())
        if a == -1:
            n = 1
        else:
            lst.append(a)
    print("The smallest number is:",minShiftedList(lst,len(lst)))

main()