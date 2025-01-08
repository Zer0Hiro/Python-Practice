#Checks if the matrix is perfect:
#Every number appears only once in every row and column
def perfect(matrix):
    #Check if any of the numbers repeats itself in every column and row
    for r in range(len(matrix)):
        rNum = []
        lNum = []
        for c in range(len(matrix)):
            #Rows Checker
            if matrix[r][c] in rNum:
                return False
            rNum.append(matrix[r][c])
            #Lines Checker
            if matrix[c][r] in lNum:
                return False
            lNum.append(matrix[c][r])
        #Same numbers in row and column 
        for i in range(len(matrix)):
            if rNum[i] not in lNum or lNum[i] not in rNum:
                return False
    return True

#Creates the matrix, prints the matrix and says if its perfect or not 
def main():
    flag = 1
    while flag != 0:
        dim = int(input("Enter the matrix dimension: "))
        if dim == 0:
            flag = 0
            return print("Finish")
        print("Enter the entries rowwise:")
        #Create matrix
        mat = []
        for r in range(dim):
            temp = []
            for c in range(dim):
                temp.append(int(input()))
            mat.append(temp)
            
        #Print created matrix
        for i in range(dim):
            for x in range(dim):        
                print ('%6d' %(mat[i][x]),end="")
            print()
        print()
        #Is it perfect or not?
        if perfect(mat) == True:
            print("The Matrix is perfect")
        else:
            print("The Matrix is not perfect")

main()
#print(perfect([[1,3,4],[2,1,3],[3,2,1]]))
