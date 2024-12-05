def main():
    a,b,c = eval(input("Please insert triangle sides:"))
    print("a = %.1f, b = %.1f, c = %.1f"%(a,b,c))
    prm = a + b + c
    print("Perimeter = %.3f"%(prm))
    prm = (a + b + c)/2
    area = (prm * (prm-a) * (prm-b) * (prm-c))**(1/2)
    print("Area = %.3f"%(area))

main()