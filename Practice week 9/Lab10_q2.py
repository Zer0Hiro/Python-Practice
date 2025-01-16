# Makes a few tests
# If matrix is squared
# If matrix is Extreme
# Return True of False
def check_matrix(matrix):
    # Squared matrix check
    col = len(matrix)
    for i in matrix:
        if len(i) != col:
            return False
    # Extreme Matrix detector
    pos = 0
    for x in matrix:
        if x[pos] < x[col - 1]:
            return False
        pos += 1
        col -= 1
    return True


# Build matrix
def build_matrix(mat):
    for r in mat:
        for c in r:
            print('%4d' % c, end="")
        print()


# Gets a few matrix
# Using functions to check if it's extreme or not and also prints the matrix
def main():
    print('first matrix:')
    m_1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [1, 2, 3, 4, 5]]
    build_matrix(m_1)
    print('is extreme matrix:', check_matrix(m_1))

    print('second matrix:')
    m_2 = [[5, 2, 3, 4, 2], [6, 7, 8, 3, 0], [1, 2, 4, 4, 5], [1, 2, 3, 4, 5]]
    build_matrix(m_2)
    print('is extreme matrix:', check_matrix(m_2))

    print('third matrix:')
    m_3 = [[5, 2, 3, 4, 2], [6, 7, 8, 3, 0], [1, 2, 4, 4, 5], [6, 0, 8, 9, 0], [1, 2, 3, 4, 5]]
    build_matrix(m_3)
    print('is extreme matrix:', check_matrix(m_3))

    print('fourth matrix:')
    m_4 = [[1]]
    build_matrix(m_4)
    print('is extreme matrix:', check_matrix(m_4))


main()
