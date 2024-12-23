def count_words(st):
    count = 0
    if st[0] != " ":
        count += 1
    for i in range(len(st)-2):
        if st[i] == " " and st[i+1] != " ":
                count += 1
    return count

def main():
    st = input("Enter your message: ")
    print(count_words(st))
    
main()