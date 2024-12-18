def main():
    n = 0
    ls = []
    summ = 0
    while n != -1:
        n = int(input("Input number: "))
        if n != -1:
            ls.append(n)
    for i in ls:
        summ += i
    print(summ)

main()

