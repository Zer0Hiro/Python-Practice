def main():
    what = input("Enter something: ")
    num = ord(what)
    if num >= 48  and num <= 57:
        print("This is number")
    elif num >= 97 and num <= 122:
        print("This is small letter")
    elif num >= 65 and num <= 90:
        print("This is big letter")
    elif num >= 33 and num <= 47: 
        print("This is character")
    else:
        print("This is something else")
main()