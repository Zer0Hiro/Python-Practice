def input_list(n):
    lst = []
    for i in range(n):
        lst.append(int(input("%d. Enter Integer: "%(i+1))))
    return lst
    
def new_list(a,x):
    new_list = []
    for i in range(len(a)):
        if a[i] < x:
            new_list.append(a[i])
    for z in range(len(a)):
        if a[z] >= x:
            new_list.append(a[z])
    return new_list

def main():
    og_list = input_list(7)
    x = int(input("Enter x: "))
    print("Original list: ", og_list)
    print("New list: ", new_list(og_list, x))
    
main()