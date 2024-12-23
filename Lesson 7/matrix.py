def create_matrix(rows,cols):
    M = []
    for i in range(rows):
        row = []
        for x in range(cols):
            row.append(int(input()))
        M.append(row)
    return M
        
def print_matrix(matrix):
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            print("%3d"%matrix[i][x], end = "")
        print()

def index_nxn(n):
    

def main():
    rows,cols = eval(input("How many rows, columns?: "))
    if rows == cols:
        n = rows
        print("nXn matrix")
    print_matrix(create_matrix(rows,cols))
    
main()