def main():
    children = int(input("Number of children: "))
    salary = int(input("Monthly salary: "))
    military = input("Military, or civil service(enter character Y, or y for yes, otherwise any other character)? ").lower()
    if salary > 17500:
        mg = salary*0.35
        print("The mortgage is approved with monthly payment of %0.2f."%mg)
    elif (military == "y" and salary >= 15000) or (children >= 5 and salary >= 14000):
        mg = salary*0.25
        print("The mortgage is approved with monthly payment of %0.2f."%mg)
    else:
        print("Sorry, the mortgage is not approved.")
main()