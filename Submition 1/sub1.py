# Input checker every < 0 except -1 "Illegal data!"
# Counter if delta is the same

# Dmitry Chybisov 342744869
# Yelyzaveta Kytaieva 342794039
def main():
    delta = 0
    saved_delta = 0
    length = 1
    length_check = 0
    start_check = 0
    delta_check = 0
    counter = 0
    # Get first number and check if this possible
    firstnum = int(input("Insert 1st number: "))
    if firstnum <= 0:
        print("Illegal data!")
    else:
        secondnum = int(input("Insert next number, end with -1: "))
        if secondnum != -1 and secondnum > 0:
            length += 1
        start = firstnum
        # Series checker
        while secondnum != -1 and secondnum > 0:
            # If delta is True
            delta = secondnum - firstnum
            # Information storage
            if delta != saved_delta:
                if length_check < length:
                    length_check = length - 1
                    delta_check = saved_delta
                    start_check = start
                length = 2
                start = firstnum
            # Save previous variables for the next loop
            saved_delta = delta
            firstnum = secondnum
            secondnum = int(input("Insert next number, end with -1: "))
            counter += 1
            if secondnum != -1 and secondnum > 0:
                length += 1
        # Check which series is bigger?
        if length_check >= length:
            start = start_check
            length = length_check
            saved_delta = delta_check
        # Results
        if secondnum <= 0 and secondnum != -1:
            print("Illegal data!")
        elif counter == 0:
            print("Longest mathematical series start with %d, length of %d" % (start, length))
        else:
            print("Longest mathematical series start with %d, delta of %d, length of %d" % (start, saved_delta, length))


main()
