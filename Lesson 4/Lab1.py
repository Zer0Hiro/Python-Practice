def main():
    num = int(input("Enter number: "))
    print("\nNumber", "Square", "Cube", sep = "    ")
    print("%4d %7d %10d"%(num, num**2, num**3))
    num += 1
    print("%4d %7d %10d"%(num, num**2, num**3))
    num += 1
    print("%4d %7d %10d"%(num, num**2, num**3))
    num += 1
    print("%4d %7d %10d"%(num, num**2, num**3))
    num += 1
    print("%4d %7d %10d"%(num, num**2, num**3))
    
main()