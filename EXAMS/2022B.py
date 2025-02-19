#QUESTION 2
def is_abun(num):
    mx = num // 2
    count = 0
    for i in range(1, mx + 1):
        if num % i == 0:
            count += i
    if count > num:
        return True
    else:
        return False

def is_ab_mat(mat):
    x = 0
    for row in mat:
        if not is_abun(row[0+x]) or not is_abun(row[-1-x]):
            return False
        x += 1
    return True

# ---------------------------------------------------------
# QUESTION 3

