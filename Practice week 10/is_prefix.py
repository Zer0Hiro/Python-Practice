# Check if the prefix is the part of the string
# And also is the first part of the string
def is_prefix(str, pref):
    # If string is shorter than prefix then False
    if len(str) < len(pref):
        return False

    if len(pref) == 0:
        return True
    if str[0] == pref[0]:
        return is_prefix(str[1:], pref[1:])
    return False


# Gets the string and the prefix for the string
# Prints back if this is actually a prefix of the string
def main():
    string = input("Enter a string:")
    pref = input("Enter another string:")
    if is_prefix(string, pref):
        print("%s is a prefix of %s" % (pref, string))
    else:
        print("%s is not a prefix of %s" % (pref, string))


main()
