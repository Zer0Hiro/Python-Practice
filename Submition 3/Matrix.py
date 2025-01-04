#    row       col
#ar[index][under index]

#Check sub-matrix in specific coordinates
def an_occurence(mat1,mat2,row,col):
    for r in range(len(mat2)):
        for c in range(len(mat2[0])):
            if mat1[r+row][c+col] != mat2[r][c]:
                return False
    return True

#Print matrix in specific range
def print_sub(mat,row,col):
    for r in range(row):
        for c in range(col):
            print(mat[r][c], end = " ")
        print()

#Check if each part of main matrix devided by row/col will be the same
def is_periodic(mat,row,col):
    #Create matrix 2
    mat2 = []
    flag = True
    #Create sub matrix
    for ir in range(row):
        temp_mat = []
        for ic in range(col):
            temp_mat.append(mat[ir][ic])
        mat2.append(temp_mat)
    #Check if sub matrix equal to the closest sub matrix
    for r in range(0,len(mat),row):
        for c in range(0,len(mat[0]),col):
            if flag != an_occurence(mat, mat2, r, c):
                return False
        return True
    
def main():
   row,col = eval((input("Enter matrix dimensions: ")))
   mat = []
   bestr = 0
   bestc = 0
   true = 0
   print("Enter %d elements"%(row*col))
   for r in range(row):
       temp = []
       for c in range(col):
           temp.append(input())
       mat.append(temp)
   #Start to check if its periodic
   for xr in range(1,len(mat)):
       for xc in range(1,len(mat[0])):
           if is_periodic(mat, xr, xc) != False:
               bestr = xr
               bestc = xc
               true = 1
   if true == 1:
       print("The matrix is periodic.")
       print("The sub-matrix is:")
       return print_sub(mat, bestr, bestc)
   return print("The matrix is not periodic.")
main()
