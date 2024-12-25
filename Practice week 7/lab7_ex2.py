def time_list(n):
    tlst = []
    for i in range(n):
        print()
        tlst.append(float(input("%d. Enter time: "%(i+1))))
    return tlst

def my_avg(lst,n):
    avg = 0
    for i in range(n):
        avg += lst[i]
    avg /= len(lst)
    return avg

def below(lst,avg):
    count = 0
    for i in range(len(lst)):
        if lst[i] < avg:
            count += 1
    print("The number of runners, running below average time is %d."%count)
    
def main():
    runners = int(input("Enter number of runners: "))
    t_lst = time_list(runners)
    t_avg = my_avg(t_lst,runners)
    print("Time average is %.2f."%(t_avg))
    below(t_lst,t_avg)
    
main()