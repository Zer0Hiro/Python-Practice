def list_inc(a):
    if len(a) < 2:
        return True
    return (a[0] <= a[1]) and list_inc(a[1:])

def main():
    print(list_inc([1,3,2,4,5,6,7,8]))

main()