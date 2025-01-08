#Defines which row has the most positive numbers
#If both rows has the same amount of positive numbers the right answer is the lowest index
def most_pos(mat):
    best = 0
    maxi = 0
    for r in range(len(mat)):
        count = 0
        for c in mat[r]:
            if c > 0:
                count += 1
        #Storage of best row
        if count > maxi:
            maxi = count
            best = r
    return best

#Creates new matrix and print which of the rows has most positive numbers
def main():
    mat = []
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns "))
    print("Enter matrix elements:")
    #Creates new matrix
    for r in range(rows):
        temp = []
        for c in range(cols):
            temp.append(int(input())) 
        mat.append(temp)
    print("The entered matrix is:")
    #Prints rows of the matrix
    for x in mat:
        print(x)
    print("The row with the most positive values is: %d"%most_pos(mat))

main()