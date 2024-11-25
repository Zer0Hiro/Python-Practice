#Get the number
#Devide to 20 10 5 and 1
#Take % of number by 20 then 10 then 5 and 1
#Print everything

def main():
    money = int(input("Enter sum of money in $: "))
    bills_20 = (money)//20
    bills_10 = (money%20)//10
    bills_5 = ((money%20)%10)//5
    bills_1 = (((money%20)%10)%5)//1
    print("%d bills(s) of 20$\n%d bills(s) of 10$"%(bills_20,bills_10))
    print("%d bills(s) of 5$\n%d bills(s) of 1$"%(bills_5,bills_1))

main()
    