def main():
    # 2 5 1
    # 1 2 5
    a,b,c = eval(input("input numbers: "))
    #first number check
    if a > b:
        temp = a
        a = b
        b = temp
    if a > c:
        temp = a
        a = c
        c = temp
    if b > c:
        temp = b
        b = c
        c = temp
    print(a,b,c)

main()