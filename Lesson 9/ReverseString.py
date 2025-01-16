def reverse_str(st):
    if st == "":
        return
    reverse_str(st[1:])
    print(st[0], end = "")

def main():
    print(reverse_str("abcd"))

main()