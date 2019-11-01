def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def factor(n):
    number = n
    x_fixed = 2
    cycle_size = 2
    x = 2
    factor = 1

    while factor == 1:
        count = 1
        #print(x_fixed, x)
        while count <= cycle_size and factor <= 1:
            x = (x*x + 1) % number
            #print(x)
            factor = gcd(x - x_fixed, number)
            count += 1
        cycle_size *= 2
        x_fixed = x

    return [factor, number//factor]
