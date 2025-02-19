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

def rec_prefix(s,pref):
    if len(pref) == 0 or len(s) == 0:
        return 0
    if pref[0] == s[0]:
        return  1 + rec_prefix(s[1:], pref[1:])
    else:
        return 0

# print(rec_prefix("","aby"))

def cntMaxSub(s,sub):
    temp = 0
    count = 0
    for i in range(len(s)):
        temp = rec_prefix(s[i:],sub)
        if temp > count:
            count = temp
    return count

# print(cntMaxSub("uabacad","abcdefg"))

# ---------------------------------------------------------
# QUESTION 4

def is_packed(lst):
    mx = max(lst)
    mn = min(lst)
    testl = []
    for x in range(mn,mx+1):
        testl.append(x)
    for num in testl:
        if num not in lst:
            return False
    return True

print(is_packed([2,-1, -2, 4, 1, 0, 2]))

