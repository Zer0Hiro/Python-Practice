def my_find(txt,st):
    flag = 0
    for i in range(len(txt)-1):
        if txt[i] == st[0]:
            for x in range(len(st)):
                if st[x] != txt[i+x]:
                    flag = 0
                else:
                    flag = 1
        if flag == 1:
            return i

def main():
    txt = input("Your text is:")
    st = input("You search for:")
    print(my_find(txt,st))

main()