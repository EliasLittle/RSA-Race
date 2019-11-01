def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def rho(n, x=2, y=2):
    r = 1
    while r == 1:
        x = (x*x+1) % n
        y_1 = (y*y+1) % n
        y = y_1 * y_1 + 1 % n
        if x > y:
            r = gcd(x-y, n)
        else:
            r = gcd(y-x, n)
    return [r, n//r]


print(rho(32193632777350883))
