#Check if sum of every number in specific row is equal to the index of the row
def index_eual(mat,row):
    summ = 0
    for r in mat[row]:
        summ += r
    if summ == row:
        return True
    return False

#Check if every number in main diagonal is > 0
def diagonal(mat):
    index = 0
    for i in mat:
        if i[index] < 0:
            return False
        index += 1
    return True

#Creates new matrix and print back if its legal or illegal 
def main():
    print("Please enter the matrix elements:")
    matrix = []
    flag = True
    #Create matrix
    for r in range(5):
        temp = []
        for c in range(5):
            temp.append(int(input()))
        matrix.append(temp)
        
    #Print created matrix
    print("The matrix is:")
    for z in range(len(matrix)):
        if index_eual(matrix, z) != True:
           flag = False 
        for i in matrix[z]:
            print("%4d"%i, end = "")
        print()
        
    #If legal checker
    if flag == False or diagonal(matrix) == False:
        return print("The matrix is illegal!")
    return print("The matrix is legal!")
main()