def main():
    x = float(input("Please insert x: "))
    num = x + (x**(1/3) + x**2)**(1/2)
    print("%.2f+(%.2f^(1/3)+%.2f^2)^0.5=%.2f"%(x,x,x,num))
    
main()
