def power_rec(a, n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    z = power_rec(a, n // 2)
    if n % 2 == 0:
        return z*z
    return z*z*a


print(power_rec(2, 4))
